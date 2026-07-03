def test_get_activities_returns_expected_structure(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    chess = payload["Chess Club"]
    assert set(chess.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(chess["participants"], list)


def test_get_activities_reflects_signup_and_unregister_within_same_flow(client):
    # Arrange
    activity_name = "Science Club"
    email = "aaa-flow@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup", params={"email": email})
    activities_after_signup = client.get("/activities")
    unregister_response = client.delete(
        f"/activities/{activity_name}/signup", params={"email": email}
    )
    activities_after_unregister = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200

    participants_after_signup = activities_after_signup.json()[
        activity_name]["participants"]
    participants_after_unregister = activities_after_unregister.json()[
        activity_name]["participants"]

    assert email in participants_after_signup
    assert email not in participants_after_unregister
