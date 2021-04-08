import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from dashboard_page import DashboardPage

def func_prin(message):
    print(message)


driver = webdriver.Chrome()


@pytest.fixture(autouse=True, scope="module")
def login(request):
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://localhost:8080/")
    login: WebElement = driver.find_element_by_xpath(
        "//*[@class='inputOutside__input--1Sg9p'][@type='text']").send_keys('default')
    password: WebElement = driver.find_element_by_xpath(
        "//*[@class='inputOutside__input--1Sg9p'][@type='password']").send_keys('1q2w3e')
    ingress: WebElement = driver.find_element_by_xpath("//*[@type='submit']").click()
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def start_page():
    driver.get("http://localhost:8080/ui/#default_personal/dashboard")


# waituntil - element visible, exist, displayed - conditions, wait custom conditions
#
# def test_first():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8080/ui/#login")
#    elem: WebElement = driver.find_element(by=By.XPATH, value="//input")
#    assert elem.is_displayed()


def test_1():
    dashbord_page = DashboardPage()
    dashbord_page.driver = driver
    dashbord_page.clik_demo()
