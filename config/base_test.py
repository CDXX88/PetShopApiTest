from services.store.api_methods import StoreAPI
from services.pet.api_methods import PetAPI
from services.user.api_methods import UserAPI

class BaseTest:

    def setup_method(self):
        self.store_api = StoreAPI()
        self.pet_api = PetAPI()
        self.user_api = UserAPI()
