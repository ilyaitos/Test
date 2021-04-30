import pytest
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


def func_prin(message):
    print(message)


def test_first():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/")
    elem: WebElement = driver.find_element(by=By.XPATH, value="//input")
    assert elem.is_displayed()



# waituntil - element visible, exist, displayed - conditions, wait custom conditions