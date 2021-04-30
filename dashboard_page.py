from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.webkitgtk.webdriver import WebDriver


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver


    def clik_demo(self):
        Dashboar = self.driver.find_element_by_xpath('//a[@class ="gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs"]')
        Dashboar.click()




    # def clik_add(self):
    #     add = WebElement
    #     add.click()
    #     neme = WebElement
    #     clik_batton = WebElement
    #
    # def clik_Launches(self):
    #     Launches= WebElement
    #     Launches.click()
