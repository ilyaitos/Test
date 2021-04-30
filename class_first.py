from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class ClassFirstTest:

    def __init__(self, driver):
        self.driver = driver

    def launches(self):
        launches: WebElement = self.driver.find_element_by_xpath('//a[@href="#default_personal/launches"]')
        launches.click()

    def drop_buttons(self):
        drop_buttons: WebElement = self.driver.find_element_by_xpath('//*[@class="userBlock__menu-icon--_7G3G"]')
        drop_buttons.click()

    def PROFILE(self):
        PROFILE: WebElement = self.driver.find_element_by_xpath('//a[@href="#user-profile"][@class="userBlock__menu-item--6Fruf"]')
        PROFILE.click()