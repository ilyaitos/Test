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

def test_1():
    name = 'jack'
    dashboard.clik_demo("DEMO DASHBOARD")
    dashboard.new_widget_type('Launches duration chart')#['Launch statistics chart', 'Overall statistics', 'Launches duration chart', 'Launch execution and issue statistic', 'Project activity panel', 'Test-cases growth trend chart', 'Investigated percentage of launches', 'Launches table', 'Unique bugs table', 'Most failed test-cases table (TOP-20)', 'Failed cases trend chart', 'Non-passed test-cases trend chart', 'Different launches comparison chart', 'Passing rate per launch', 'Passing rate summary', 'Flaky test cases table (TOP-20)', 'Cumulative trend chart', 'Most popular pattern table (TOP-20)', 'Component health check', 'Component health check (table view)']
    dashboard.click_button_demo_filter()
    dashboard.click_button_next()
    dashboard.widget_name(name)
    dashboard.click_button_add()
    score = dashboard.score_widget()
    assert score.count(name) == 1

#
# def test_2():
#     demo_api_tests_number = 7
#     launches.click_button_launches()
#     number_skipped = launches.skipped_main(demo_api_tests_number)
#     number_failed = launches.failed_main(demo_api_tests_number)
#     number_passed = launches.passed_main(demo_api_tests_number)
#     number_total = launches.total_main(demo_api_tests_number)
#     launches.total_main_click(demo_api_tests_number)
#     quantity_tests = launches.test_score()
#     assert number_passed == quantity_tests['passed']
#     assert number_failed == quantity_tests['failed']
#     assert number_skipped == quantity_tests['skipped']
#     assert number_total == quantity_tests['total']
#
# def test_3():
#     launches.click_button_launches()
#     quantity = launches.quantity_tests()
#     assert quantity == 10
#
# def test_4():
#     dashboard.click_button_profile()
#     dashboard.drop_button_language()
#     dashboard.button_russian_language()
#     language_text = dashboard.russian_text()
#     assert language_text == 'Русский'
#
# def test_5():
#     dashboard.click_button_profile()
#     dashboard.download_photo("C:/Users/User/Pictures/zxc.jpg")
#
#
# def test_5():