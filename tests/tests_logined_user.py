from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from selenium.webdriver.support.wait import WebDriverWait

class TestLoginedUser:

    def test_entrance_personal_account(self, driver_logined):
        driver = driver_logined
        driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))

        result = driver.current_url
        expected = personal_account_site
        assert expected == result

    def test_transition_to_constructor(self,driver_logined):
        driver = driver_logined

        driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUKTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUKT_YOUR_BURGER))

        result = driver.current_url
        expected = main_site
        assert result == expected

    def test_transition_by_logo(self, driver_logined):
        driver = driver_logined

        driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()

        result = driver.current_url
        expected = main_site
        assert result == expected

    def test_exit_account(self, driver_logined):
        driver = driver_logined

        driver.find_element(*Locators.ENTRANCE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_ENTRANCE))

        result = driver.current_url
        expected = login_site
        assert result == expected


