import os
from api.api import PetFriends
from api.settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_invalid_user(email='email@mail.com', password='invalid_password'):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_all_pets_with_invalid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key['key'] = auth_key['key'] + '000'
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403
    assert 'pets' not in result


def test_add_new_pet_with_invalid_photofile_in_data(name='1', animal_type='2', age='3',
                                             pet_photo='images\\1.txt'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    print(result)
    assert status != 200    #должен быть по документации в Swagger, но тест не проходит
    assert 'data:' not in result['pet_photo']   #если первое сравнение сделать status == 200,
                                                # то тест выполняется


def test_add_new_pet_with_invalid_key(name='dog1', animal_type='dog', age='2',
                                             pet_photo='images\suslik1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key['key'] = auth_key['key'] + '000'
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403
    assert name not in result


def test_add_new_pet_simple_with_invalid_data(name=1, animal_type=2, age=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name=name, animal_type=animal_type, age=age)
    print(result)
    assert status != 200    #должен быть по документации в Swagger, но тест не проходит
    assert name not in result   #если первое сравнение сделать status == 200,
                                # то тест выполняется


def test_add_new_pet_simple_with_invalid_key(name='cat1', animal_type='cat', age=1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key['key'] = auth_key['key'] + '000'
    status, result = pf.add_new_pet_simple(auth_key, name=name, animal_type=animal_type, age=age)
    assert status == 403
    assert name not in result


def test_add_photo_of_pet_with_invalid_data(pet_photo='images\\1.txt'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_simple(auth_key, name='cat1', animal_type='cat', age=1)
        _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status != 200
    assert 'pet_photo' not in result


def test_add_photo_of_pet_with_invalid_key(pet_photo='images\cat1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_simple(auth_key, name='cat1', animal_type='cat', age=1)
        _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = my_pets['pets'][0]['id']
    auth_key['key'] = auth_key['key'] + '000'
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 403
    assert 'pet_photo' not in result


def test_delete_my_pet_with_invalid_key():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets_before = pf.get_list_of_pets(auth_key, filter='my_pets')
    if len(my_pets_before['pets']) == 0:
        pf.add_new_pet_simple(auth_key, name='cat1', animal_type='cat', age=1)
        _, my_pets_before = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = my_pets_before['pets'][0]['id']
    auth_key['key'] = auth_key['key'] + '000'
    status, _ = pf.delete_my_pet(auth_key, pet_id)
    auth_key['key'] = auth_key['key'][:-3]
    _, my_pets_after = pf.get_list_of_pets(auth_key, filter='my_pets')
    assert status == 403
    assert my_pets_after == my_pets_before


def test_update_my_pet_info_with_invalid_data(new_name='', new_animal_type='', new_age=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_simple(auth_key, name='cat1', animal_type='cat', age=1)
        _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_my_pet_info(auth_key, pet_id, new_name, new_animal_type, new_age)
    print(result)
    assert status != 200    #должен быть по документации в Swagger, но тест не проходит
    assert new_name not in result   #если первое сравнение сделать status == 200,
                                    # то тест выполняется


def test_update_my_pet_info_with_invalid_key(new_name='hamster1',
                                                    new_animal_type='hamster', new_age=3):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_simple(auth_key, name='cat1', animal_type='cat', age=1)
        _, my_pets = pf.get_list_of_pets(auth_key, filter='my_pets')
    pet_id = my_pets['pets'][0]['id']
    auth_key['key'] = auth_key['key'] + '000'
    status, result = pf.update_my_pet_info(auth_key, pet_id, new_name, new_animal_type, new_age)
    assert status == 403
    assert new_name not in result
