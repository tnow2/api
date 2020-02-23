import requests
from faker import Faker

base_url = 'http://18.184.234.77:8080'
fake = Faker()


def test_get_accounts_list():
    response = requests.get(f'{base_url}/accounts')
    assert response.status_code == 200

    response_dict = response.json()
    accounts_list = response_dict['accounts']
    names_list = [a['name'] for a in accounts_list]
    print(names_list)
    assert 'Łukasz' in names_list


def test_create_account():
    random_name = fake.uuid4()
    body = {
        "name": random_name
    }
    create_account_response = requests.put(f'{base_url}/accounts/create', json=body)
    assert create_account_response.status_code == 201

    list_params = {'account': random_name}
    filtered_list_response = requests.get(f'{base_url}/accounts', params=list_params)
    assert filtered_list_response.status_code == 200
    assert random_name in filtered_list_response.text
