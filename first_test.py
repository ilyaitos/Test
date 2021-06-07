
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dashboard_page import DashboardPage
from launches_page import LaunchesPage

def func_prin(message):
    print(message)

driver = webdriver.Chrome(ChromeDriverManager().install())
dashboard = DashboardPage(driver)
launches = LaunchesPage(driver)


def test_1():
    dashboard.clik_demo()
    dashboard.new_widget()
    dashboard.widget_type(13)
    dashboard.button_next1()
    dashboard.button_demo_filter()
    dashboard.button_next2()
    dashboard.clear_text()
    dashboard.widget_name('jack')
    dashboard.add_button()
    assert dashboard.check('jack')


def test_2():
    launches.clik_launches()
    number_skipped = launches.skipped_main(7)
    number_failed = launches.failed_main(7)
    number_passed = launches.passed_main(7)
    number_total = launches.total_main(7)
    launches.total_click(7)
    passed = 0
    failed = 0
    skipped = 0
    total = 0
    while True:
        total_len = launches.total_score()
        passed_len = launches.score('Passed')
        skipped_len = launches.score('Skipped')
        failed_len = launches.score('Failed')
        button = launches.button_next()
        classes_element = button.get_attribute('class')
        driver.execute_script("arguments[0].click();", button)
        total += total_len
        passed += passed_len
        failed += failed_len
        skipped += skipped_len
        if classes_element == 'pageButton__page-button--OHYKN pageButton__disabled--3-RYj':
            break
    assert number_total == total
    assert number_passed == passed
    assert number_skipped == skipped
    assert number_failed == failed


def test_3():
    launches.clik_launches()
    launches.number_tests()
    assert launches.number_tests() == 10


def test_4():
    dashboard.drop_buttons()
    dashboard.profile()
    dashboard.drop_language()
    dashboard.russian_language()
    dashboard.russian_text()
    assert dashboard.russian_text() == 'Русский'

def test_5():
    dashboard.drop_buttons()
    dashboard.profile()
    dashboard.photo("C:/Users/User/Pictures/zxc.jpg")













