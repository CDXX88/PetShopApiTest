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
        tag_name = None
        response = requests.post(url, json=payload)
        try:
            response_data = response.json()
            tags = response_data.get('tags', [])
            tag_name = tags[0].get('name')
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id'),
            'tag': tag_name
        }

    def post_pet_image(self, pet_id):
        image = self._payloads.pet_image()
        additional_metadata = self._payloads.metadata()
        url = f'{self._urls.base_url}{self._urls.pet_id}{pet_id}{self._urls.pet_upload_image}'
        data = {"additionalMetadata": additional_metadata}
        files = {"file": image}
        response = requests.post(url, data=data, files=files)
        try:
            body = response.json()
        except ValueError:
            body = response.text

        return {
            'body': body,
            'status_code': response.status_code
        }

    def put_pet(self):
        payload = self._payloads.pet_payload()
        url = f'{self._urls.base_url}{self._urls.pet}'
        response = requests.put(url, json=payload)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text

        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

    def get_pet_by_status(self):
        url = f'{self._urls.base_url}{self._urls.pet_find_by_status}'
        status = self._payloads.pet_random_status()
        params = {
            'status': status
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

    def get_pet_by_tags(self, tags):
        url = f'{self._urls.base_url}{self._urls.pet_find_by_tags}'
        params = {
            'tags': tags
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

    def get_pet_by_id(self, pet_id):
        url = f'{self._urls.base_url}{self._urls.pet_id}{pet_id}'
        response = requests.get(url)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

    def post_pet_by_id(self, pet_id):
        url = f'{self._urls.base_url}{self._urls.pet_id}{pet_id}'
        name = self._payloads.pet_name()
        status = self._payloads.pet_random_status()
        params = {
            'name': name,
            'status': status
        }
        response = requests.post(url, params=params)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }

    def delete_pet_by_id(self, pet_id):
        url = f'{self._urls.base_url}{self._urls.pet_id}{pet_id}'
        headers = {
            'api-key': 'special-key'
        }
        response = requests.delete(url, headers=headers)
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text
        return {
            'body': response_data,
            'status_code': response.status_code,
            'pet_id': response_data.get('id')
        }
