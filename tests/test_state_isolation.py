def test_state_mutation_occurs_within_test(client):
    # Arrange
    activity_name = "Debate Team"
    email = "isolation@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup", params={"email": email})
    activities_response = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    participants = activities_response.json()[activity_name]["participants"]
    assert email in participants


def test_state_is_reset_between_tests(client):
    # Arrange
    activity_name = "Debate Team"
    leaked_email = "isolation@mergington.edu"

    # Act
    activities_response = client.get("/activities")

    # Assert
    participants = activities_response.json()[activity_name]["participants"]
    assert leaked_email not in participants
