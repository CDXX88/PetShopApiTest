from services.store.api_methods import StoreAPI
from services.pet.api_methods import PetAPI

class BaseTest:

    def setup_method(self):
        self.store_api = StoreAPI()
        self.pet_api = PetAPI()
