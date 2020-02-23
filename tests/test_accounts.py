import requests
import endpoints
from faker import Faker
fake = Faker()


def test_get_accounts_list():
    expected_name = _create_account()

    response = requests.get(endpoints.accounts)
    assert response.status_code == 200

    response_dict = response.json()
    accounts_list = response_dict['accounts']
    names_list = [a['name'] for a in accounts_list]
    print(names_list)
    assert expected_name in names_list


def test_create_account():
    expected_name = _create_account()

    list_params = {'account': expected_name}
    filtered_list_response = requests.get(endpoints.accounts, params=list_params)
    assert filtered_list_response.status_code == 200
    assert expected_name in filtered_list_response.text


def _create_account():
    random_name = fake.uuid4()
    body = {
        "name": random_name
    }
    create_account_response = requests.put(endpoints.accounts_create, json=body)
    assert create_account_response.status_code == 201
    return random_name
