import pytest
import selenium
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Фикстура для загрузки сайта в браузере и последующего выхода из браузера
@pytest.fixture(autouse=True)
def testing2():
   pytest.driver = selenium.webdriver.Chrome("/tests/Selenium_example/chromedriver.exe")
   pytest.driver.get("http://petfriends.skillfactory.ru/login")

   # Вводим email
   WebDriverWait(pytest.driver, timeout=10).until(EC.presence_of_element_located((By.ID, "email"))).\
      send_keys("maria_yastr@mail.ru")
   # Вводим пароль
   WebDriverWait(pytest.driver, timeout=10).until(EC.presence_of_element_located((By.ID, "pass"))).\
      send_keys("123456789")
   # Нажимаем на кнопку входа в аккаунт
   WebDriverWait(pytest.driver, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).\
      click()

   yield

   pytest.driver.quit()


class MyPetsTable:
   def setup(self):
      # Задаем переменную для общего количества питомцев из статистики пользователя
      self.find_total_count = WebDriverWait(pytest.driver, timeout=10).\
         until(EC.presence_of_element_located((By.XPATH, "//div[@class='.col-sm-4 left']")))
      self.total_count = int(list(map(str, self.find_total_count.text.split()))[3])

      # Создаем списки из имен, пород и возраста всех питомцев в таблице
      self.names = []
      self.breeds = []
      self.ages = []
      for i in range(self.total_count):
         number = 0
         name = WebDriverWait(pytest.driver, timeout=10).until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, "tr>td")))[number + i * 4].text
         self.names.append(name)
         breed = WebDriverWait(pytest.driver, timeout=10).until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, "tr>td")))[number + 1 + i * 4].text
         self.breeds.append(breed)
         age = WebDriverWait(pytest.driver, timeout=10).until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, "tr>td")))[number + 2 + i * 4].text
         self.ages.append(age)

      return self.total_count, self.names, self.breeds, self.ages


def test_my_pets_table():
   # Заходим на страницу питомцев пользователя
   WebDriverWait(pytest.driver, timeout=10).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))
   WebDriverWait(pytest.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/my_pets']"))).click()

   # 1-я проверка:
   # Считаем количество питомцев в таблице и сравниваем с общим количеством из статистики пользователя
   total_count, names, breeds, ages = MyPetsTable().setup()
   count_pets = len(pytest.driver.find_elements(By.XPATH, "//tbody/tr"))

   try:
      assert count_pets == total_count
      print('Количество питомцев в таблице совпадает с количеством в статистике пользователя')
   except AssertionError as e:
      print('Количество питомцев в таблице НЕ совпадает с количеством в статистике пользователя')

   # 2-я проверка:
   # Считаем количество питомцев, имеющих фото, в таблице
   images = WebDriverWait(pytest.driver, timeout=10).until(EC.presence_of_all_elements_located((By.XPATH, "//th/img")))
   count = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         count += 1

   # Сравниваем полученное количество с половинным значением от общего количества
   # питомцев из статистики пользователя
   try:
      assert count >= total_count/2
      print("У половины и более питомцев есть фото")
   except AssertionError as e:
      print("Более чем у половины питомцев нет фото")

   # 3-я проверка:
   # Проверяем, для всех ли питомцев указано имя, порода и возраст
   try:
      for i in range(len(names)):
         assert names[i] != ''
      print('У всех питомцев указано имя')
   except AssertionError as e:
      print(f'У питомца под номером {i+1} не указано имя.')

   try:
      for i in range(len(breeds)):
         assert breeds[i] != ''
      print('У всех питомцев указана порода')
   except AssertionError as e:
      print(f'У питомца под номером {i+1} не указана порода.')

   try:
      for i in range(len(ages)):
         assert ages[i] != ''
      print('У всех питомцев указан возраст')
   except AssertionError as e:
      print(f'У питомца под номером {i+1} не указан возраст.')

   # 4-я проверка:
   # Считаем количество повторений имен в таблице питомцев и проверяем, что повторений нет
   names_counts = [names.count(x) for x in names]
   try:
      for i in names_counts:
         assert i == 1
      print('Имена питомцев не повторяются')
   except AssertionError as e:
      print(f'У питомца под номером {names_counts.index(i)+1} не уникальное имя.')

   # 5-я проверка:
   # Проверяем, что все питомцы уникальны, нет питомцев с одинаковыми именем, породой и возрастом
   pets = {i: (names[i-1], breeds[i-1], ages[i-1]) for i in range(1, total_count+1)}
   unique_pets = set(pets.values())
   try:
      assert len(pets.values()) == len(unique_pets)
      print('Повторяющихся одинаковых питомцев нет')
   except AssertionError as e:
      print(f'В таблице есть повторяющиеся питомцы, количество - {len(pets.values()) - len(unique_pets)}.')
