from faker import Faker
import random
from PIL import Image
from io import BytesIO

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

    def metadata(self):
        return fake.uuid4()

    def pet_image(self):
        width, height = 100, 100
        color = random.choice(["red", "green", "blue", "purple"])

        img = Image.new("RGB", (width, height), color=color)

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        return "generated.png", buffer, "image/png"

    def pet_random_status(self):
        return random.choice(["available", "pending", "sold"])

    def pet_name(self):
        return fake.name()

