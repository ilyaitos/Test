import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import os

def func_prin(message):
    print(message)


#waituntil - element visible, exist, displayed - conditions, wait custom conditions
# def test_first():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8080/ui/#login")
#    elem: WebElement = driver.find_element(by=By.XPATH, value="//input")
#    assert elem.is_displayed()


def test_1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://localhost:8080/")
    login: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='text']").send_keys('default')
    password: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='password']").send_keys('1q2w3e')
    ingress: WebElement = driver.find_element_by_xpath("//*[@type='submit']").click()
    demo: WebElement = driver.find_element_by_xpath('//*[@class="gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs"]').send_keys(Keys.ENTER)
    widget: WebElement = driver.find_element_by_css_selector('#app > div > div > div > div.layout__content--2bbWd > div.scrollWrapper__scroll-component--3vuv7 > div.scrollWrapper__scrolling-content--XWgeG.scrollWrapper__with-footer--25_wC > div > div.layout__page-container--qkF50 > div > div.pageLayout__page-content--2R36V > div > div.dashboardItemPage__buttons-container--28m3K > div:nth-child(1) > button:nth-child(1) > span').click()
    ingress1: WebElement = driver.find_element_by_css_selector('#modal-root > div > div.widgetWizardModal__scrolling-content--6_VX4 > div > div.scrollWrapper__scrolling-content--XWgeG > div > div.widgetWizardContent__widget-wizard-content--1dJGf > div.wizardControlsSection__wizard-controls-section--3I-Ac > div.wizardControlsSection__controls-wrapper--2-h9- > form > div > div:nth-child(15) > label > span.inputRadio__children-container--32kGF').click()
    ingress2: WebElement = driver.find_element_by_css_selector('#modal-root > div > div.widgetWizardModal__scrolling-content--6_VX4 > div > div.scrollWrapper__scrolling-content--XWgeG > div > div.widgetWizardContent__widget-wizard-content--1dJGf > div.wizardControlsSection__wizard-controls-section--3I-Ac > div.wizardControlsSection__buttons-block--1F7VD > div > button > span')
    driver.execute_script("arguments[0].click();", ingress2)
    ingress3: WebElement = driver.find_element_by_xpath('//input[@aria-autocomplete="list"]').send_keys('DEMO_FILTER')
    ingress4: WebElement = driver.find_element_by_xpath('//*[@class="ghostButton__icon--2rRly ghostButton__icon-at-right--3Ui7m"]').click()
    ingress5: WebElement = driver.find_element_by_xpath('//*[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]').click()
    print('widget is added')


def test_2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://localhost:8080/")
    login: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='text']").send_keys('default')
    password: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='password']").send_keys('1q2w3e')
    ingress: WebElement = driver.find_element_by_xpath("//*[@type='submit']").click()
    launches: WebElement = driver.find_element_by_xpath('//a[@href="#default_personal/launches"]').click()
    total_1: WebElement = int(driver.find_element_by_xpath("//a[@href='#default_personal/launches/all/7?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']").text)
    total_click: WebElement = driver.find_element_by_xpath("//a[@href='#default_personal/launches/all/7?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']").send_keys(Keys.ENTER)

    element_more: WebElement = driver.find_element_by_xpath('//*[@class="pageSizeControl__size-text--2f_I6"]')
    driver.execute_script("arguments[0].click();", element_more)

    element_more_300: WebElement = driver.find_element_by_xpath("//*[@class='input__input--3DC8i type-text']").send_keys('300', Keys.ENTER)
    passed = len(driver.find_elements_by_xpath("//*[@class='gridRow__grid-row-wrapper--1dI9K']"))
    failed = len(driver.find_elements_by_xpath("//*[@class='gridRow__grid-row-wrapper--1dI9K stepGrid__failed--2d38k']"))
    #skipped =
    total = passed + failed
    if total == total_1:
        print('true')
    else:
        print('false')



def test_3():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://localhost:8080/")
    login: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='text']").send_keys('default')
    password: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='password']").send_keys('1q2w3e')
    ingress: WebElement = driver.find_element_by_xpath("//*[@type='submit']").click()
    launches: WebElement = driver.find_element_by_xpath('//a[@href="#default_personal/launches"]').click()
    total_1 = len(driver.find_elements_by_xpath("//*[@class='gridRow__grid-row-wrapper--1dI9K']"))

    if total_1 == 10:
        print(total_1, 'from 10')
    else:
        print('false')

def test_4():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://localhost:8080/")
    login: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='text']").send_keys('default')
    password: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='password']").send_keys('1q2w3e')
    ingress: WebElement = driver.find_element_by_xpath("//*[@type='submit']").click()
    ingress1: WebElement = driver.find_element_by_xpath('//*[@class="userBlock__menu-icon--_7G3G"]').click()
    ingress2: WebElement = driver.find_element_by_xpath('//a[@href="#user-profile"][@class="userBlock__menu-item--6Fruf"]').click()
    ingress3: WebElement = driver.find_element_by_xpath('//*[@class="inputDropdown__select-block--2CQf-"]').click()
    ingress4: WebElement = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div[3][@class="inputDropdownOption__dropdown-option--3Szk3"]').click()
    print('language changed')



def test_5():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://localhost:8080/")
    login: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='text']").send_keys('default')
    password: WebElement = driver.find_element_by_xpath("//*[@class='inputOutside__input--1Sg9p'][@type='password']").send_keys('1q2w3e')
    ingress: WebElement = driver.find_element_by_xpath("//*[@type='submit']").click()
    ingress1: WebElement = driver.find_element_by_xpath('//*[@class="userBlock__menu-icon--_7G3G"]').click()
    ingress2: WebElement = driver.find_element_by_xpath('//a[@href="#user-profile"][@class="userBlock__menu-item--6Fruf"]').click()
    ingress3: WebElement = driver.find_element_by_xpath('//input[@type="file"]').send_keys("C:/Users/User/Pictures/zxc.jpg")
    time.sleep(10)










   