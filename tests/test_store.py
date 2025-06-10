import pytest
from config.base_test import BaseTest

class TestStore(BaseTest):

    def test_get_inventory(self):
        response = self.store_api.get_inventory()
        assert response['status_code'] == 200, "Status code must be 200"

    def test_post_order(self):
        response = self.store_api.post_order()
        assert response['status_code'] == 200, "Order creation should return status code 200"

    @pytest.mark.unstable
    @pytest.mark.xfail(reason="Can fail on remote")
    def test_get_order_by_id(self):
        created = self.store_api.post_order()
        order_id = created['order_id']

        response = self.store_api.get_order_by_id(order_id)
        assert response['status_code'] == 200, "Fetching order should return status code 200"

    @pytest.mark.unstable
    @pytest.mark.xfail(reason="Can fail on remote")
    def test_delete_order_by_id(self):
        created = self.store_api.post_order()
        order_id = created['order_id']

        delete_response = self.store_api.delete_order_by_id(order_id)
        assert delete_response['status_code'] == 200, "Order deletion should return status code 200"