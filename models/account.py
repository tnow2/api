import endpoints
import requests
from faker import Faker

fake = Faker()


class Account:
    def __init__(self):
        self.name = fake.uuid4()
        self.balance = None

    def create(self):
        body = {"name": self.name}
        create_account_response = requests.put(endpoints.accounts_create, json=body)
        assert create_account_response.status_code == 201

    def delete(self):
        account_params = {'account': self.name}
        delete_response = requests.delete(endpoints.accounts_delete, params=account_params)
        assert delete_response.status_code == 200

    def pay(self):
        pass

    def withdraw(self):
        pass

    def get_balance(self):
        list_params = {'account': account_name}
        filtered_list_response = requests.get(endpoints.accounts, params=list_params)
        assert filtered_list_response.json()['accounts'][0]['balance']['accountBalance'] == 1000


if __name__ == '__main__':
    account = Account()
    print(account.name)
    account.create()
    account.delete()
