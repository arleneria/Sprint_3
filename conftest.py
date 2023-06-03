import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from locator import Locators


@pytest.fixture
def driver():
    driver_chrome = webdriver.Chrome()
    driver_chrome.get("https://stellarburgers.nomoreparties.site/")
    yield driver_chrome
    driver_chrome.quit()

@pytest.fixture
def account_login(driver):
    driver.find_element(*Locators.REG_LOGIN_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    driver.find_element(*Locators.EMAIL).send_keys(
        'ekaterina_beloborodova_10_456@ya.ru')
    driver.find_element(*Locators.PASSWORD).send_keys('1234567')
    driver.find_element(*Locators.REG_LOGIN).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
    return driver
