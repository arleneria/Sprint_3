from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators


class TestRegistration:
    def test_registration(self, driver):

        driver.find_element(*Locators.REG_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        driver.find_element(*Locators.REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Регистрация"]')))
        driver.find_element(By.XPATH, './/label[text()="Имя"]/parent::div/input').send_keys('Ekaterina')
        driver.find_element(By.XPATH, './/label[text()="Email"]/parent::div/input').send_keys('egygviyad1fv4d516@ya.ru')
        driver.find_element(By.XPATH, './/label[text()="Пароль"]/parent::div/input').send_keys('1234567')
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_wrong_password(self, driver):
        driver.find_element(*Locators.REG_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        driver.find_element(*Locators.REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Регистрация"]')))
        driver.find_element(By.XPATH, './/label[text()="Имя"]/parent::div/input').send_keys('Ekaterina')
        driver.find_element(By.XPATH, './/label[text()="Email"]/parent::div/input').send_keys('egygvydvdffv456@ya.ru')
        driver.find_element(By.XPATH, './/label[text()="Пароль"]/parent::div/input').send_keys('1')
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
        WebDriverWait(driver, 3)
        assert 'input_status_error' in driver.find_element(By.XPATH, './/label[text()="Пароль"]/parent::div').get_attribute('class')
