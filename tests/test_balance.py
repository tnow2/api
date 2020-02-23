import pytest
import requests
import endpoints
from faker import Faker

fake = Faker()


def test_create_account(account_name):
    list_params = {'account': account_name}
    filtered_list_response = requests.get(endpoints.accounts, params=list_params)
    assert filtered_list_response.status_code == 200
    assert account_name in filtered_list_response.text


def test_balance(account_name):
    list_params = {'account': account_name}
    filtered_list_response = requests.get(endpoints.accounts, params=list_params)
    assert filtered_list_response.json()['accounts'][0]['balance']['accountBalance'] == 1000


@pytest.fixture()
def account_name():
    random_name = fake.uuid4()
    body = {
        "name": random_name
    }
    create_account_response = requests.put(endpoints.accounts_create, json=body)
    assert create_account_response.status_code == 201
    return random_name
