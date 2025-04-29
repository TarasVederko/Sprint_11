from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestContsractor:

    def test_buns_section_activation(self, driver):
        souce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))
        )
        souce_tab.click()

        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Булки']"))
        )
        buns_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Булки']"))
        )
        assert active_tab.is_displayed(), "Таб 'Булки' не стал активным"



    def test_souce_section_activation(self, driver):
        souce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))
        )
        souce_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Соусы']"))
        )
        assert active_tab.is_displayed(), "Таб 'Соусы' не стал активным"

    def test_topping_section_activation(self, driver):
        topping_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))
        )
        topping_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Начинки']"))
        )
        assert active_tab.is_displayed(), "Таб 'Начинки' не стал активным"