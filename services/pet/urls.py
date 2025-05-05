class Urls:

    base_url = 'https://petstore.swagger.io/v2'

    pet = '/pet' ## add a new pet to the store and update an existing pet, used in put_pet and post_pet
    pet_id = '/pet/' ## user in delete, update, get_by_id
    pet_find_by_status = '/pet/findByStatus' ## finds ets by status
    pet_upload_image = '/pet/{petId}/uploadImage' ## uploads and image (need to think how to rework or use url