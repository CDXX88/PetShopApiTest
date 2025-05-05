import requests
from services.store.urls import Urls
from services.store.payloads import Payloads


class StoreAPI:

    def __init__(self):
        self._urls = Urls()
        self._payloads = Payloads()

    def get_inventory(self):
        url = f"{self._urls.base_url}{self._urls.inventory_link}"
        response = requests.get(url)
        response_data = response.json()
        return {
            'response_body': response_data,
            'status_code': response.status_code,
        }

    def post_order(self):
        payload = self._payloads.order_payload()
        url = f'{self._urls.base_url}{self._urls.order_link}'
        response = requests.post(url, json=payload)
        response_data = response.json()
        return {
            'response_body': response_data,
            'status_code': response.status_code,
            'order_id': response_data.get('id')
        }

    def get_order_by_id(self, order_id):
        url = f'{self._urls.base_url}{self._urls.order_link}{order_id}'
        response = requests.get(url)
        response_data = response.json()
        return {
            'response_body': response_data,
            'status_code': response.status_code,
        }

    def delete_order_by_id(self, order_id):
        url = f'{self._urls.base_url}{self._urls.order_link}{order_id}'
        response = requests.delete(url)
        response_data = response.json()
        return {
            'response_body': response_data,
            'status_code': response.status_code,
        }

