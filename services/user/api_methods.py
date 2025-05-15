import requests

from services.user.payloads import Payloads
from services.user.urls import Urls


class UserAPI:

    def __init__(self):
        self._urls = Urls()
        self._payloads = Payloads()

    def post_user(self):
        url = f'{self._urls.base_url}{self._urls.user}'
        payload = self._payloads.user_payload()
        username = payload.get('username')
        password = payload.get('password')
        response = requests.post(url, json=payload)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code,
            'username': username,
            'password': password
        }

    def post_user_create_with_list(self):
        url = f'{self._urls.base_url}{self._urls.user_with_array}'
        payload = self._payloads.user_list_payload()
        response = requests.post(url, json=payload)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def get_user_login(self, username, password):
        url = f'{self._urls.base_url}{self._urls.user_login}'
        params = {
            'username': username,
            'password': password
        }
        response = requests.get(url, params=params)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def get_user_by_user_name(self, username):
        url = f'{self._urls.base_url}{self._urls.user_by_username}{username}'
        response = requests.get(url)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def put_user_by_user_name(self, username):
        url = f'{self._urls.base_url}{self._urls.user_by_username}{username}'
        response = requests.put(url, json=self._payloads.user_payload())
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def delete_user_by_user_name(self, username):
        url = f'{self._urls.base_url}{self._urls.user_by_username}{username}'
        response = requests.delete(url)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def get_user_logout(self):
        url = f'{self._urls.base_url}{self._urls.user_logout}'
        response = requests.get(url)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code
        }