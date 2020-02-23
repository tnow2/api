import pytest
import requests
import endpoints
from faker import Faker

fake = Faker()


def test_get_accounts_list(account_name):
    response = requests.get(endpoints.accounts)
    assert response.status_code == 200

    response_dict = response.json()
    accounts_list = response_dict['accounts']
    names_list = [a['name'] for a in accounts_list]
    print(names_list)
    assert account_name in names_list


def test_create_account(account_name):
    list_params = {'account': account_name}
    filtered_list_response = requests.get(endpoints.accounts, params=list_params)
    assert filtered_list_response.status_code == 200
    assert account_name in filtered_list_response.text


def test_delete_account(account_name):
    account_params = {'account': account_name}

    delete_response = requests.delete(endpoints.accounts_delete, params=account_params)
    assert delete_response.status_code == 200

    filtered_list_response = requests.get(endpoints.accounts, params=account_params)
    assert filtered_list_response.status_code == 404


@pytest.fixture()
def account_name():
    random_name = fake.uuid4()
    body = {
        "name": random_name
    }
    create_account_response = requests.put(endpoints.accounts_create, json=body)
    assert create_account_response.status_code == 201
    return random_name
