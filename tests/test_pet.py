import pytest
from config.base_test import BaseTest

class TestPet(BaseTest):

    def test_post_pet(self):
        response = self.pet_api.post_pet()
        assert response['status_code'] == 200, 'Status code must be 200'

    @pytest.mark.unstable
    @pytest.mark.xfail(reason="Can fail on mock")
    def test_post_pet_image(self):
        created = self.pet_api.post_pet()
        pet_id = created['pet_id']

        response = self.pet_api.post_pet_image(pet_id)
        assert response['status_code'] == 200, 'Status code must be 200'

    def test_put_pet(self):
        response = self.pet_api.post_pet()
        assert response['status_code'] == 200, 'Status code must be 200'

    def test_get_pet_by_status(self):
        response = self.pet_api.get_pet_by_status()
        assert response['status_code'] == 200, 'Status code must be 200'

    def test_get_pet_by_tags(self):
        response = self.pet_api.get_pet_by_status()
        assert response['status_code'] == 200, 'Status code must be 200'

    def test_get_pet_by_id(self):
        created = self.pet_api.post_pet()
        pet_id = created['pet_id']

        response = self.pet_api.get_pet_by_id(pet_id)
        assert response['status_code'] == 200, 'Status code must be 200'

    def test_post_pet_by_id(self):
        created = self.pet_api.post_pet()
        pet_id = created['pet_id']

        response = self.pet_api.post_pet_by_id(pet_id)
        assert response['status_code'] == 200, 'Status code must be 200'

    @pytest.mark.unstable
    @pytest.mark.xfail(reason="Can fail on mock")
    def test_delete_pet_by_id(self):
        created = self.pet_api.post_pet()
        pet_id = created['pet_id']

        response = self.pet_api.delete_pet_by_id(pet_id)
        assert response['status_code'] == 200, 'Status code must be 200'