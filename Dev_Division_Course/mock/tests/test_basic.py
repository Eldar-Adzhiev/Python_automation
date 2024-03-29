import requests
import settings
from mocks.surname_mock import SURNAME_DATA

url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'


def test_add_get_user():
    resp = requests.post(f'{url}/add_user', json={'name': 'Ilya'})
    user_id_from_add = resp.json()['user_id']

    resp = requests.get(f'{url}/get_user/Ilya')
    user_id_from_get = resp.json()['user_id']

    assert user_id_from_add == user_id_from_get


def test_add_existent_user():
    requests.post(f'{url}/add_user', json={'name': 'Vasya'})
    resp = requests.post(f'{url}/add_user', json={'name': 'Vasya'})

    assert resp.status_code == 400


def test_get_non_existent_user():
    resp = requests.get(f'{url}/Masha')

    assert resp.status_code == 404


def test_with_age():
    requests.post(f'{url}/add_user', json={'name': 'Stepan'})

    resp = requests.get(f'{url}/get_user/Stepan')
    age = resp.json()['age']
    print(age)
    assert isinstance(age, int)
    assert 0 <= age <= 100


def test_has_surname():
    requests.post(f'{url}/add_user', json={'name': 'Olya'})
    SURNAME_DATA['Olya'] = 'OLOLOEVA'

    resp = requests.get(f'{url}/get_user/Olya')
    surname = resp.json()['surname']

    assert surname == 'OLOLOEVA'
