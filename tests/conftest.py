import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from helper import *
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    # Создаем опции для Chrome
    options = Options()
    options.add_argument("--window-size=1200,600")  # Задаем размер окна

    # Инициализируем драйвер (путь к нему должен быть в PATH)
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)

    yield driver
    driver.quit()

@pytest.fixture
def open_registration_window(driver):
    #open registration window
    driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_FORM_LINK).click()
    yield driver

@pytest.fixture
def driver_with_account(open_registration_window):
    email, password = generate_registration_data()
    name = generate_name()
    driver = open_registration_window
    driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)
    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_ENTRANCE))
    yield driver



