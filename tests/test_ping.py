import requests
import endpoints


def test_ping():
    pong_response = requests.get(endpoints.ping)
    assert pong_response.status_code == 200
    assert pong_response.text == 'pong'


def test_ping_as_json():
    headers_dict = {
        'Accept': 'application/json'
    }
    pong_response = requests.get(endpoints.ping, headers=headers_dict)
    assert pong_response.status_code == 200
    response_dict = pong_response.json()
    assert response_dict['reply'] == 'pong!'
