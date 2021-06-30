from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dashboard_page import DashboardPage
from launches_page import LaunchesPage

def func_prin(message):
    print(message)

driver = webdriver.Chrome(ChromeDriverManager().install())
dashboard = DashboardPage(driver)
launches = LaunchesPage(driver)

#
# def test_1():
#     dashboard.clik_demo()
#     dashboard.new_widget()
#     dashboard.widget_type(13)
#     dashboard.button_next1()
#     dashboard.button_demo_filter()
#     dashboard.button_next2()
#     dashboard.clear_text()
#     dashboard.widget_name('jack')
#     dashboard.add_button()
#     assert dashboard.check('jack')


def test_2():
    demo_api_tests_number = 7
    launches.click_button_launches()
    number_skipped = launches.skipped_main(demo_api_tests_number)
    number_failed = launches.failed_main(demo_api_tests_number)
    number_passed = launches.passed_main(demo_api_tests_number)
    number_total = launches.total_main(demo_api_tests_number)
    launches.total_click(demo_api_tests_number)
    quantity_tests = launches.test_score()
    assert number_passed == quantity_tests['passed']
    assert number_failed == quantity_tests['failed']
    assert number_skipped == quantity_tests['skipped']
    assert number_total == quantity_tests['total']

#
# def test_3():
#     launches.click_button_launches()
#     launches.number_tests()
#     assert launches.number_tests() == 10
#
#
# def test_4():
#     dashboard.click_drop_buttons()
#     dashboard.click_button_profile()
#     dashboard.drop_language()
#     dashboard.russian_language()
#     dashboard.russian_text()
#     assert dashboard.russian_text() == 'Русский'
#
# def test_5():
#     dashboard.click_drop_buttons()
#     dashboard.click_button_profile()
#     dashboard.photo("C:/Users/User/Pictures/zxc.jpg")


















