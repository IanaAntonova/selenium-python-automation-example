import requests
import pytest


@pytest.mark.rickandmorty
def test_parameters_query_request():
    name = "Rick"
    status = "Alive"
    res = requests.get("https://rickandmortyapi.com/api/character", params={"name": name, "status": status})
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json; charset=utf-8"
    json_data = res.json()
    assert json_data['results'][0]['name'] == "Rick Sanchez"
    assert json_data['results'][0]['id'] == 1
    assert json_data['results'][0]['species'] == "Human"
    assert json_data['results'][0]['status'] == "Alive"
    assert json_data['info']['pages'] == 2
