from faker import Faker
import random

fake = Faker()

class Payloads:

    def pet_payload(self):
        return {
            "id": random.randint(1, 10),
            "category": {
                "id": random.randint(1, 10),
                "name": fake.word()
            },
            "name": fake.first_name(),
            "photoUrls": [
                fake.image_url()
            ],
            "tags": [
                {
                    "id": random.randint(1, 10),
                    "name": fake.word()
                }
            ],
            "status": random.choice(["available", "pending", "sold"])
        }