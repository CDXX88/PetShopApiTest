class Urls:

    base_url = 'http://petshop-api-tests:8080'

    pet = '/pet' ## add a new pet to the store and update an existing pet, used in put_pet and post_pet
    pet_id = '/pet/' ## used in delete, update, get_by_id
    pet_find_by_status = '/pet/findByStatus' ## finds pets by status
    pet_upload_image = '/uploadImage' ## uploads and image
    pet_find_by_tags = '/pet/findByTags' ## searching pet by tag