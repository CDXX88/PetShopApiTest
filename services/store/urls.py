import os
class Urls:

    stage = os.getenv('STAGE', 'REMOTE').upper()

    if stage == 'DOCKER':
        base_url = 'http://localhost:8080/api/v3'
    elif stage == 'REMOTE':
        base_url = 'http://petstore.swagger.io/v2/pet'

    inventory = '/store/inventory/' ## Returns pet inventories by status
    order = '/store/order/' ## Place an order for a pet



