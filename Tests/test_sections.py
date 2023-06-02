from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator import Locators


class TestSections:
    def test_section_with_bread(self, account_login):
        driver = account_login
        driver.find_element(*Locators.SOUS).click()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.BREAD).click()
        name_class = driver.find_element(*Locators.BREAD).get_attribute('class')
        assert name_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_section_with_sous(self, account_login):
        driver = account_login
        driver.find_element(*Locators.SOUS).click()
        WebDriverWait(driver, 3)
        name_class = driver.find_element(*Locators.SOUS).get_attribute('class')
        assert name_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


    def test_section_with_filling(self, account_login):
        driver = account_login
        driver.find_element(*Locators.FILLING).click()
        WebDriverWait(driver, 3)
        name_class = driver.find_element(*Locators.FILLING).get_attribute('class')
        assert name_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'