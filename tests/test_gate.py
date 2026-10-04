from fastapi.testclient import TestClient
from mlops.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'alias': 'champion', 'tests_passed': True, 'image': 'ml-api@sha256:1', 'image_digest': 'sha256:1'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'alias': 'champion', 'tests_passed': True, 'image': 'ml-api:latest'}).json()
    assert bad["passed"] is False
    assert "image_tag_latest" in bad["failed"]
