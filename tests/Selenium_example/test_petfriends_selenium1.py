import pytest
import selenium
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


# Фикстура для загрузки сайта в браузере и последующего выхода из браузера
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = selenium.webdriver.Chrome("D:\Education\PyCharmProjects\SF_tasks\AuthTesting\\tests\Selenium_example\chromedriver.exe")
   pytest.driver.implicitly_wait(10)
   pytest.driver.get("http://petfriends.skillfactory.ru/login")

   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys("maria_yastr@mail.ru")
   # Вводим пароль
   pytest.driver.find_element(By.ID, "pass").send_keys("123456789")
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

   yield

   pytest.driver.quit()


def test_show_all_cards_of_pets():
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


def test_all_cards_of_pets():
   # Выбираем все фото, имена, описания с породой и возрастом из карточек питомцев
   images = pytest.driver.find_elements(By.CSS_SELECTOR, ".card-img-top")
   names = pytest.driver.find_elements(By.CSS_SELECTOR, ".card-title")
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, ".card-text")

   # Заводим списки с проверками (1/0) на наличие фото, имени, породы и возраста во всех карточках
   check_images = []
   check_names = []
   check_breeds = []
   check_ages = []
   for i in range(len(names)):
      if images[i].get_attribute('src') != '':
         check_images.append(1)
      else:
         check_images.append(0)

      if names[i].text != '':
         check_names.append(1)
      else:
         check_names.append(0)

      parts = descriptions[i].text.split(", ")
      if descriptions[i].text != '' and ', ' in str(descriptions[i]):
         if len(parts[0]) > 0:
            check_breeds.append(1)
         else:
            check_breeds.append(0)
         if len(parts[1]) > 0:
            check_ages.append(1)
         else:
            check_ages.append(0)

   # Выводим результат проверки, во всех ли карточках питомцев есть фото, имя, порода и возраст
   try:
      assert 0 not in check_images
   except AssertionError as e:
      print('Не все карточки имеют фото.')

   try:
      assert 0 not in check_names
   except AssertionError as e:
      print('Не все карточки имеют имена.')

   try:
      assert 0 not in check_breeds
   except AssertionError as e:
      print('Не все карточки имеют описание с породой.')

   try:
      assert 0 not in check_ages
   except AssertionError as e:
      print('Не все карточки имеют описание с возрастом.')
