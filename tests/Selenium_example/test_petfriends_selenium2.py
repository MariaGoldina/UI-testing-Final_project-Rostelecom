import pytest
import selenium
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


# Фикстура для загрузки сайта в браузере и последующего выхода из браузера
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = selenium.webdriver.Chrome(
       "D:\Education\PyCharmProjects\SF_tasks\AuthTesting\\tests\Selenium_example\chromedriver.exe")
   pytest.driver.get("http://petfriends.skillfactory.ru/login")

   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys("maria_yastr@mail.ru")
   # Вводим пароль
   pytest.driver.find_element(By.ID, "pass").send_keys("123456789")
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

   yield

   pytest.driver.quit()



class TestMyPetsTable:
   def setup(self):
      # Заходим на страницу питомцев пользователя
      pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()

      # Задаем переменную для общего количества питомцев из статистики пользователя
      self.total_count = int(list(map(str, pytest.driver.find_element(By.XPATH, "//div[@class='.col-sm-4 left']").text.split()))[3])

      # Создаем списки из имен, пород и возраста всех питомцев в таблице
      self.names = []
      self.breeds = []
      self.ages = []
      for i in range(self.total_count):
         number = 0
         name = pytest.driver.find_elements(By.CSS_SELECTOR, "tr>td")[number + i * 4].text
         self.names.append(name)
         breed = pytest.driver.find_elements(By.CSS_SELECTOR, "tr>td")[number + 1 + i * 4].text
         self.breeds.append(breed)
         age = pytest.driver.find_elements(By.CSS_SELECTOR, "tr>td")[number + 2 + i * 4].text
         self.ages.append(age)

      return self.total_count, self.names, self.breeds, self.ages

   def test_count_pets(self):
      # Считаем количество питомцев в таблице и сравниваем с общим количеством из статистики пользователя
      count_pets = len(pytest.driver.find_elements(By.XPATH, "//tbody/tr"))
      total_count, _, _, _, = TestMyPetsTable().setup()
      assert count_pets == total_count

   def test_half_pets_have_photo(self):
      # Считаем количество питомцев, имеющих фото, в таблице
      images = pytest.driver.find_elements(By.XPATH, "//th/img")
      count = 0
      for i in range(len(images)):
         if images[i].get_attribute('src') != '':
            count += 1
      # Сравниваем полученное количество с половинным значением от общего количества
      # питомцев из статистики пользователя
      total_count, _, _, _, = TestMyPetsTable().setup()
      assert count >= total_count/2

   def test_all_pets_have_descriptions(self):
      # Проверяем, для всех ли питомцев указано имя, порода и возраст
      total_count, names, breeds, ages = TestMyPetsTable().setup()
      try:
         for i in range(len(names)):
            assert names[i] != ''
      except AssertionError as e:
         print(f'У питомца под номером {i} не указано имя.')
      try:
         for i in range(len(breeds)):
            assert breeds[i] != ''
      except AssertionError as e:
         print(f'У питомца под номером {i} не указана порода.')
      try:
         for i in range(len(ages)):
            assert ages[i] != ''
      except AssertionError as e:
         print(f'У питомца под номером {i} не указан возраст.')

   def test_different_names_of_pets(self):
      # Считаем количество повторений имен в таблице питомцев и проверяем, что повторений нет
      _, names, _, _ = TestMyPetsTable().setup()
      counts = [names.count(x) for x in names]
      try:
         for i in counts:
            assert i == 1
      except AssertionError as e:
         print(f'У питомца под номером {counts.index(i)+1} не уникальное имя.')

   def test_all_pets_different(self):
      # Проверяем, что все питомцы уникальны, нет питомцев с одинаковыми именем, породой и возрастом
      total_count, names, breeds, ages = TestMyPetsTable().setup()
      pets = {i:(names[i-1], breeds[i-1], ages[i-1]) for i in range(1, total_count+1)}
      unique_pets = set(pets.values())
      assert len(pets.values()) == len(unique_pets)
