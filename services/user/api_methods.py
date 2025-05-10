import requests

from services.user.payloads import Payloads
from services.user.urls import Urls


class UserAPI:

    def __init__(self):
        self.urls = Urls()
        self.payloads = Payloads()

    def post_user(self):
        url = f'{self.urls.base_url}{self.urls.user}'
        payload = self.payloads.user_payload()
        username = payload.get('username')
        password = payload.get('password')
        response = requests.post(url, json=payload)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code,
            'username': username,
            'password': password
        }

    def post_user_create_with_list(self):
        url = f'{self.urls.base_url}{self.urls.user_with_array}'
        payload = self.payloads.user_list_payload()
        response = requests.post(url, json=payload)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def get_user_login(self, username, password):
        url = f'{self.urls.base_url}{self.urls.user_login}'
        params = {
            'username': username,
            'password': password
        }
        response = requests.post(url, params=params)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def get_user_by_user_name(self, username):
        url = f'{self.urls.base_url}{self.urls.user_by_username}'
        params = {
            'username': username
        }
        response = requests.get(url, params=params)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def put_user_by_user_name(self, username):
        url = f'{self.urls.base_url}{self.urls.user_by_username}'
        params = {
            'username': username
        }
        response = requests.get(url, params=params)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def delete_user_by_user_name(self, username):
        url = f'{self.urls.base_url}{self.urls.user_by_username}'
        params = {
            'username': username
        }
        response = requests.get(url, params=params)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code
        }

    def get_user_logout(self):
        url = f'{self.urls.base_url}{self.urls.user_logout}'
        response = requests.post(url)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code
        }


if __name__ == '__main__':
    api = UserAPI()
    method = api.post_user()
    print(method['username'])
    print(method['password'])

