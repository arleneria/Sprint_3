from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators


class TestFromAccountToConstructor:
    def test_transition_click_on_constructor(self, account_login):
        driver = account_login
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        driver.find_element(*Locators.REG_LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/label[text()="Имя"]')))
        driver.find_element(*Locators.REG_CONSTR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transition_click_on_logo(self, account_login):
        driver = account_login
        driver.find_element(*Locators.REG_LK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/label[text()="Имя"]')))
        driver.find_element(*Locators.REG_LOGO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
