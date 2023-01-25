import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        """Метод задает базовый URL сайта"""
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email: str, password: str) -> 'json':
        """Метод делает запрос к API сервера и возвращает статус запроса и результат
         в формате json с уникальным ключем пользователя, найденного по указанным email и паролю"""
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: 'json', filter: str="") -> 'json':
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате json:
        в виде списка всех питомцев. Варианты фильтра: '' - список всех питомцев на сайте,
        'my_pets' - список всех добавленных пользователем питомцев"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: 'json', name: str, animal_type: str, age: str, pet_photo: str) -> 'json':
        """Метод направляет POST-запрос на сервер с данными о новом питомце и возвращает статус запроса
        и результат в формате json в виде характеристик добавленного питомца."""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet_simple(self, auth_key: 'json', name: str, animal_type: str, age: int) -> 'json':
        """Метод направляет POST-запрос на сервер с данными о новом питомце без добавления фото
        и возвращает статус запроса и результат в формате json в виде характеристик добавленного питомца."""
        data = {
                'name': name,
                'animal_type': animal_type,
                'age': age,
                }
        headers = {'auth_key': auth_key['key']}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_photo_of_pet(self, auth_key: 'json', pet_id: str, pet_photo: str) -> 'json':
        """Метод направляет POST-запрос на сервер с файлом фото и позволяет добавить/изменить фото
        у существующего питомца с заданным ID. Метод возвращает статус запроса и результат в формате json
        в виде новых характеристик питомца."""
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + f'api/pets/set_photo/{pet_id}', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_my_pet(self, auth_key: 'json', pet_id: str) -> 'json':
        """Метод отправляет запрос на сервер об удалении питомца с заданным ID и возвращает статус и результат
        запроса в формате json (*в результате приходит пустая строка)."""
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + f'api/pets/{pet_id}', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_my_pet_info(self, auth_key: 'json', pet_id: str, new_name: str, new_animal_type: str,
                           new_age: int) -> 'json':
        """Метод отправляет запрос на сервер об изменении данных питомца с заданным ID и возвращает
        статус запроса и результат запроса в формате json с новыми характеристиками питомца."""
        data = {
                'name': new_name,
                'animal_type': new_animal_type,
                'age': new_age
            }
        headers = {'auth_key': auth_key['key']}
        res = requests.put(self.base_url + f'api/pets/{pet_id}', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
