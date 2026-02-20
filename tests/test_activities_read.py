def test_get_activities_returns_activity_mapping(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert expected_activity in payload
    assert {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }.issubset(payload[expected_activity])
