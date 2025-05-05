from services.store.api_methods import StoreAPI

class BaseTest:

    def setup_method(self):
        self.store_api = StoreAPI()
