from config.base_test import BaseTest

class TestStore(BaseTest):

    def test_get_inventory(self):
        response = self.store_api.get_inventory()
        assert response['status_code'] == 200, "Status code must be 200"
        assert isinstance(response['response_body'], dict), "Response body must be a dictionary"
        assert 'sold' in response['response_body'], "Key 'sold' must be present in inventory response"

    def test_post_order(self):
        response = self.store_api.post_order()
        assert response['status_code'] == 200, "Order creation should return status code 200"
        assert isinstance(response['order_id'], int), "order_id must be an integer"
        assert response['response_body']['status'] in ['placed', 'approved', 'delivered'], "Unexpected order status value"

    def test_get_order_by_id(self):
        created = self.store_api.post_order()
        order_id = created['order_id']

        response = self.store_api.get_order_by_id(order_id)
        assert response['status_code'] == 200, "Fetching order should return status code 200"
        assert response['response_body']['id'] == order_id, "Returned order ID does not match the requested one"

    def test_delete_order_by_id(self):
        created = self.store_api.post_order()
        order_id = created['order_id']

        delete_response = self.store_api.delete_order_by_id(order_id)
        assert delete_response['status_code'] == 200, "Order deletion should return status code 200"

        get_response = self.store_api.get_order_by_id(order_id)
        assert get_response['status_code'] == 404, "Deleted order should return status code 404 when fetched"