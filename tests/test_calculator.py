import requests
import random

base_url = 'http://18.184.234.77:8080'


def test_add_numbers():
    first_number, second_number = random.randint(1, 1000), random.randint(1, 1000)
    expected_result = first_number + second_number
    body = {
        "firstNumber": first_number,
        "secondNumber": second_number
    }
    add_numbers_response = requests.post(f'{base_url}/add', json=body)
    assert add_numbers_response.status_code == 200

    result_dict = add_numbers_response.json()['result']
    actual_result = result_dict['result']
    assert actual_result == expected_result
