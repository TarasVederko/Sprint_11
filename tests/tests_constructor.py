from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestContsractor:

    def test_buns_section_activation(self, driver):
        souce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.SOUCE_BUTTON))
        )
        souce_tab.click()

        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.BREAD_BUTTON))
        )
        buns_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (Locators.ACTIVE_BREAD_BUTTON))
        )
        assert active_tab.is_displayed(), "Таб 'Булки' не стал активным"



    def test_souce_section_activation(self, driver):
        souce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.SOUCE_BUTTON))
        )
        souce_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (Locators.ACTIVE_SOUCE_BUTTON))
        )
        assert active_tab.is_displayed(), "Таб 'Соусы' не стал активным"

    def test_topping_section_activation(self, driver):
        topping_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.TOPPING_BUTTON))
        )
        topping_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (Locators.ACTIVE_TOPPING_BUTTON))
        )
        assert active_tab.is_displayed(), "Таб 'Начинки' не стал активным"