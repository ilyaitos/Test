import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


def func_prin(message):
    print(message)

driver = webdriver.Chrome()

@pytest.fixture(scope="module")
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

@pytest.fixture()
def start_page():
    driver.get("http://localhost:8080/ui/#default_personal/dashboard")


# waituntil - element visible, exist, displayed - conditions, wait custom conditions
#
# def test_first():
#    driver = webdriver.Chrome()
#    driver.get("http://localhost:8080/ui/#login")
#    elem: WebElement = driver.find_element(by=By.XPATH, value="//input")
#    assert elem.is_displayed()


def test_1(start_page, login):
    demo: WebElement = driver.find_element_by_xpath('//*[@class="gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs"]').send_keys(Keys.ENTER)
    widget: WebElement = driver.find_element_by_xpath('(//div/button)[2]').click()
    button_passing: WebElement = driver.find_element_by_xpath('(//label)[14]').click()
    button_next_step: WebElement = driver.find_element_by_xpath('(//div/button)[7]')
    driver.execute_script("arguments[0].click();", button_next_step)
    DEMO_FILTER: WebElement = driver.find_element_by_xpath('//input[@aria-autocomplete="list"]').send_keys('DEMO_FILTER')
    button_next_step_DEMO_FILTER: WebElement = driver.find_element_by_xpath('//*[@class="ghostButton__icon--2rRly ghostButton__icon-at-right--3Ui7m"]').click()
    ADD_NEW_WIDGET: WebElement = driver.find_element_by_xpath('//*[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]').click()
    assert driver.find_element_by_xpath('//*[@class="noDataAvailable__no-data-available--3EH6v"]')


def test_2(start_page, login):
    launches: WebElement = driver.find_element_by_xpath('//a[@href="#default_personal/launches"]').click()
    skipped_main: WebElement = int(driver.find_element_by_xpath('//*[@href="#default_personal/launches/all/7?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DSKIPPED"]').text)
    failed_main: WebElement = int(driver.find_element_by_xpath('//*[@href="#default_personal/launches/all/7?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DFAILED%252CINTERRUPTED"]').text)
    passed_main: WebElement = int(driver.find_element_by_xpath("//*[@href='#default_personal/launches/all/7?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED']").text)
    total_main: WebElement = int(driver.find_element_by_xpath("//a[@href='#default_personal/launches/all/7?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']").text)
    total_click: WebElement = driver.find_element_by_xpath("//a[@href='#default_personal/launches/all/7?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren""%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED""']").send_keys(Keys.ENTER)
    passed = 0
    failed = 0
    skipped = 0
    total = 0
    while True:
        total_len = len(driver.find_elements_by_xpath("//*[@class='gridRow__grid-row--1pS-5']"))
        skipped_len = len(driver.find_elements_by_xpath("//span[text()='Skipped'][@class='itemInfo__mobile-status--1qoKx']"))
        failed_len = len(driver.find_elements_by_xpath("//*[@class='gridRow__grid-row-wrapper--1dI9K stepGrid__failed--2d38k']"))
        passed_len = len(driver.find_elements_by_xpath("//span[text()='Passed'] [@class='itemInfo__mobile-status--1qoKx']"))

        button: WebElement = driver.find_element_by_css_selector('.pageButtons__page-buttons--uRADS '
                                                                    '.pageButton__page-button--OHYKN:nth-child(6)')
        classes_element = button.get_attribute('class')
        driver.execute_script("arguments[0].click();", button)
        total += total_len
        passed += passed_len
        failed += failed_len
        skipped += skipped_len
        if classes_element == 'pageButton__page-button--OHYKN pageButton__disabled--3-RYj':
            break
    assert total_main == total
    assert passed_main == passed
    assert skipped_main == skipped
    assert failed_main == failed


def test_3(start_page, login):
    launches: WebElement = driver.find_element_by_xpath('//a[@href="#default_personal/launches"]').click()
    total = len(driver.find_elements_by_xpath("//*[@class='gridRow__grid-row-wrapper--1dI9K']"))
    assert total == 10


def test_4(start_page, login):
    drop_buttons: WebElement = driver.find_element_by_xpath('//*[@class="userBlock__menu-icon--_7G3G"]').click()
    PROFILE: WebElement = driver.find_element_by_xpath('//a[@href="#user-profile"][@class="userBlock__menu-item--6Fruf"]').click()
    Language: WebElement = driver.find_element_by_xpath('//*[@class="inputDropdown__select-block--2CQf-"]').click()
    Russian: WebElement = driver.find_element_by_xpath('//*[@class="inputDropdownOption__dropdown-option--3Szk3"][2]').click()
    Russian_text: WebElement = driver.find_element_by_xpath('// span[ @class ="inputDropdown__value--2gB2s"]').text
    assert Russian_text == 'Русский'


def test_5(start_page, login):
    drop_buttons: WebElement = driver.find_element_by_xpath('//*[@class="userBlock__menu-icon--_7G3G"]').click()
    PROFILE: WebElement = driver.find_element_by_xpath('//a[@href="#user-profile"][@class="userBlock__menu-item--6Fruf"]').click()
    Photo: WebElement = driver.find_element_by_xpath('//input[@type="file"]').send_keys("C:/Users/User/Pictures/zxc.jpg")












