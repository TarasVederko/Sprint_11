from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import *
from helper import generate_registration_data, generate_name, generate_email
from locators import Locators
from curl import *

class TestRegistrationWithNewCredential:

    def test_registration(self, open_registration_window):

        #arrange
        email, password = generate_registration_data()
        name = generate_name()
        driver = open_registration_window
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

        # act
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_ENTRANCE))
        result = driver.curret_url
        expected = login_site

        # assert
        assert result == expected

    def test_registration_no_name(self, open_registration_window):
        # arrange
        email, password = generate_registration_data()
        driver = open_registration_window
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)

        # act
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        result = driver.current_url
        expected = reg_site

        # assert
        assert result == expected

    def test_registration_short_password(self, open_registration_window):
        # arrange
        name = generate_name()
        email = generate_email()
        driver = open_registration_window
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(short_password)

        # act
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # assert
        assert driver.find_element(*Locators.SHORT_PASSWORD).text == 'Некорректный пароль'
        assert driver.current_url == reg_site

class TestEntranceToPersonalCabinet:

     def test_entrance_through_button_on_main(self, driver_with_account):
         driver = driver_with_account
         driver.find_element(*Locators.BUTTON_ENTRANCE).click()
         driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTRANCE).send_keys(email)
         driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ENTRANCE).send_keys(password)

         driver.find_element(*Locators.BUTTON_ENTRANCE).click()
         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))

         assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()

     def test_entrance_through_cabinet(self,driver_with_account):
         driver = driver_with_account
         driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON).click()
         driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTRANCE).send_keys(email)
         driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ENTRANCE).send_keys(password)

         driver.find_element(*Locators.BUTTON_ENTRANCE).click()
         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))

         assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()

     def test_entrance_through_registration_form(self, driver_with_account):
         driver = driver_with_account

         driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON).click()
         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REGISTRATION_BUTTON_IN_ENTRANCE_FORM))

         driver.find_element(*Locators.REGISTRATION_BUTTON_IN_ENTRANCE_FORM).click()
         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTRANCE_ACCOUNT_BUTTON_IN_REGISTRATION_FORM))

         driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON_IN_REGISTRATION_FORM).click()
         driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTRANCE).send_keys(email)
         driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ENTRANCE).send_keys(password)

         driver.find_element(*Locators.BUTTON_ENTRANCE).click()
         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))

         assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()

     def test_entrance_trough_frogot_password(self, driver_with_account):
         driver = driver_with_account

         driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON).click()
         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_RECOVER_PASSWORD))

         driver.find_element(*Locators.BUTTON_RECOVER_PASSWORD).click()
         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTRANCE_ACCOUNT_BUTTON_IN_REGISTRATION_FORM))

         driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON_IN_REGISTRATION_FORM).click()
         driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTRANCE).send_keys(email)
         driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ENTRANCE).send_keys(password)

         driver.find_element(*Locators.BUTTON_ENTRANCE).click()
         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))

         assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()











