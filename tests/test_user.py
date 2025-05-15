from config.base_test import BaseTest

class TestUsers(BaseTest):

    def test_post_user(self):
        response = self.user_api.post_user()
        assert response['status_code'] == 200, "Test should return status code 200"

    def test_get_user_by_user_name(self):
        create = self.user_api.post_user()
        username = create['username']
        response = self.user_api.get_user_by_user_name(username)
        assert response['status_code'] == 200, "Test should return status code 200"

    def test_post_user_create_with_list(self):
        response = self.user_api.post_user_create_with_list()
        assert response['status_code'] == 200, "Test should return status code 200"

    def test_get_user_login(self):
        create = self.user_api.post_user()
        username = create['username']
        password = create['password']
        response = self.user_api.get_user_login(username, password)
        assert response['status_code'] == 200, "Test should return status code 200"

    def test_put_user_by_user_name(self):
        create = self.user_api.post_user()
        username = create['username']
        response = self.user_api.put_user_by_user_name(username)
        assert response['status_code'] == 200, "Test should return status code 200"

    def test_delete_user_by_user_name(self):
        create = self.user_api.post_user()
        username = create['username']
        response = self.user_api.delete_user_by_user_name(username)
        assert response['status_code'] == 200, "Test should return status code 200"

    def test_get_user_logout(self):
        response = self.user_api.get_user_logout()
        assert response['status_code'] == 200, "Test should return status code 200"