import requests
base_url = 'http://18.184.234.77:8080'


def test_ping():

    pong_response = requests.get(f'{base_url}/ping')
    assert pong_response.status_code == 200

    assert pong_response.text == 'pong'
