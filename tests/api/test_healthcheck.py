import json


def test_healthcheck_database_up(api_test_client, mocker):
    mocker.patch("banking.api.healthcheck.db.engine.execute")
    result = api_test_client.get("/api/healthcheck")
    data = json.loads(result.data.decode("utf-8"))
    assert data == {"status": "up"}


def test_healthcheck_database_down(api_test_client, mocker):
    mocker.patch("banking.api.healthcheck.db.engine.execute", side_effect=Exception)
    result = api_test_client.get("/api/healthcheck")
    data = json.loads(result.data.decode("utf-8"))
    assert data == {"status": "down"}
