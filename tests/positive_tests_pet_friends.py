import os
from api.api import PetFriends
from api.settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data_and_key(name='dog1', animal_type='dog', age='2',
                                             pet_photo='images\suslik1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_simple_with_valid_data_and_key(name='cat1', animal_type='cat', age=1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name=name, animal_type=animal_type, age=age)
    assert status == 200
    assert result['name'] == name


def test_add_photo_of_pet_with_valid_data_and_key(pet_photo='images\cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_simple(auth_key, name='cat1', animal_type='cat', age=1)
        _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert 'data:image/jpeg' in result['pet_photo']


def test_delete_my_pet_with_valid_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_simple(auth_key, name='cat1', animal_type='cat', age=1)
        _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_my_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    assert status == 200
    assert pet_id not in my_pets.values()


def test_update_my_pet_info_with_valid_data_and_key(new_name='hamster1',
                                                    new_animal_type='hamster', new_age=3):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_simple(auth_key, name='cat1', animal_type='cat', age=1)
        _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_my_pet_info(auth_key, pet_id, new_name, new_animal_type, new_age)
    assert status == 200
    assert result['name'] == new_name
