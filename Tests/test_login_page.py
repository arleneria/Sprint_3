
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators


class TestLogin:
    def test_login_account(self, driver):

        driver.find_element(*Locators.REG_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))

        driver.find_element(*Locators.EMAIL).send_keys('ekaterina_beloborodova_10_456@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('1234567')
        driver.find_element(*Locators.REG_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_personal_account(self, driver):

        driver.find_element(*Locators.REG_LK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        driver.find_element(*Locators.EMAIL).send_keys(
            'ekaterina_beloborodova_10_456@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('1234567')
        driver.find_element(*Locators.REG_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_login_registration_form(self, driver):
        driver.find_element(*Locators.REG_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        driver.find_element(*Locators.REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Регистрация"]')))
        driver.find_element(*Locators.REG_LOGIN_A).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))


        driver.find_element(*Locators.EMAIL).send_keys(
            'ekaterina_beloborodova_10_456@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('1234567')
        driver.find_element(*Locators.REG_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_login_from_restore_password(self, driver):
        driver.find_element(*Locators.REG_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        driver.find_element(*Locators.RESTOR_PAS).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Восстановление пароля"]')))
        driver.find_element(*Locators.REG_LOGIN_A).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))

        driver.find_element(*Locators.EMAIL).send_keys(
            'ekaterina_beloborodova_10_456@ya.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('1234567')
        driver.find_element(*Locators.REG_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
