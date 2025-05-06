import requests

from services.pet.payloads import Payloads
from services.pet.urls import Urls

class PetAPI:

    def __init__(self):
        self._payloads = Payloads()
        self._urls = Urls()

    def post_pet(self):
        payload = self._payloads.pet_payload()
        url = f'{self._urls.base_url}{self._urls.pet}'
        response = requests.post(url, json=payload)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

    def put_pet_by_id(self, payload):
        payload = ''
        url = f'{self._urls.base_url}{self._urls.pet}'
        response = requests.put(url, json=payload)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

    def get_pet_by_id(self, pet_id):
        url = f'{self._urls.base_url}{self._urls.pet_id}{pet_id}'
        response = requests.get(url)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

if __name__ == '__main__':
    post_pet = PetAPI().post_pet()
    print(post_pet['status_code'])
