from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators


class TestClickOnPersonalAccount:
    def test_click(self, account_login):
        driver = account_login
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        driver.find_element(*Locators.REG_LK).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'