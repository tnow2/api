import pytest
import requests
import endpoints
from faker import Faker

from models.account import Account

fake = Faker()


def test_get_accounts_list(new_account):
    response = requests.get(endpoints.accounts)
    assert response.status_code == 200

    response_dict = response.json()
    accounts_list = response_dict['accounts']
    names_list = [a['name'] for a in accounts_list]
    print(names_list)
    assert new_account.name in names_list


def test_create_account(new_account):
    list_params = {'account': new_account.name}
    filtered_list_response = requests.get(endpoints.accounts, params=list_params)
    assert filtered_list_response.status_code == 200
    assert new_account.name in filtered_list_response.text


def test_delete_account(new_account):
    new_account.delete()

    account_params = {'account': new_account.name}
    filtered_list_response = requests.get(endpoints.accounts, params=account_params)
    assert filtered_list_response.status_code == 404


def test_account_balance(new_account):
    assert new_account.get_balance() == 1000



@pytest.fixture()
def new_account():
    account = Account()
    account.create()
    return account
