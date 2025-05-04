from faker import Faker
import random
from datetime import datetime

fake = Faker()

class Payloads:

    def order_payload(self):
        return {
            "id": random.randint(1, 10),
            "petId": random.randint(1, 10),
            "quantity": random.randint(1, 10),
            "shipDate": datetime.now().isoformat(),
            "status": random.choice(["placed", "approved", "delivered"]),
            "complete": fake.boolean()
        }
