import pytest
from selenium.webdriver.remote.webelement import WebElement
from first_test import driver

link = "http://localhost:8080/"

@pytest.fixture(autouse=True, scope="module")
def login():
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(link)
    login: WebElement = driver.find_element_by_xpath(
        "//*[@class='inputOutside__input--1Sg9p'][@type='text']").send_keys('default')
    password: WebElement = driver.find_element_by_xpath(
        "//*[@class='inputOutside__input--1Sg9p'][@type='password']").send_keys('1q2w3e')
    ingress: WebElement = driver.find_element_by_xpath("//*[@type='submit']").click()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def start_page():
    driver.get(link + "ui/#default_personal/dashboard")