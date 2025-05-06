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

    def post_pet_image(self, pet_id):
        image = self._payloads.pet_image()
        additional_metadata = self._payloads.metadata()
        url = f'{self._urls.base_url}{self._urls.pet}{pet_id}{self._urls.pet_upload_image}'
        files = {
            "additionalMetadata": additional_metadata,
            "file": image
        }
        response = requests.post(url, files=files)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

    def put_pet(self, payload):
        payload = ''
        url = f'{self._urls.base_url}{self._urls.pet}'
        response = requests.put(url, json=payload)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

    def get_pet_by_status(self, pet_status): ## here heed to check how to use query param
        url = f'{self._urls.base_url}{self._urls.pet_find_by_status}'
        response = requests.get(url)
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

    def post_pet_by_id(self, pet_id):
        url = f'{self._urls.base_url}{self._urls.pet_id}{pet_id}'
        response = requests.post(url)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

    def delete_pet_by_id(self, api_key, pet_id):
        url = f'{self._urls.base_url}{self._urls.pet_id}{pet_id}'
        response = requests.delete(url, headers=api_key)
        response_data = response.json()
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }