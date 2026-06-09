from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email():
    response = client.delete("/activities/Chess Club/unregister?email=michael@mergington.edu")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Unregistered michael@mergington.edu from Chess Club"
    }


def test_unregister_unknown_participant_returns_404():
    response = client.delete("/activities/Chess Club/unregister?email=unknown@mergington.edu")

    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}
