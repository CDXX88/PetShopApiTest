from faker import Faker
import random
import json

fake = Faker()

class Payloads:

    def user_payload(self):
        return {
            "id": random.randint(1, 1000),
            "username": fake.user_name(),
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(length=10),
            "phone": fake.phone_number(),
            "userStatus": random.choice([0, 1])
        }

    def user_list_payload(self):
        counter = random.randint(1, 10)
        users_array = []
        for i in range(1, counter):
            users_array.append(self.user_payload())
        return users_array

# if __name__ == '__main__':
#     payload = Payloads()
#     list_ = payload.user_list_payload()
#     print(json.dumps(list_, indent=2))