from selenium.webdriver.common.keys import Keys
from home_page import HomePage

class LocatorsLaunchesPage:

    url_main = "//a[@href='#default_personal/launches/all/{}?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3"

    LOCATOR_TOTAL = url_main +   "DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']"
    LOCATOR_PASSED = url_main +  "DPASSED']"
    LOCATOR_FAILED = url_main +  "DFAILED%252CINTERRUPTED']"
    LOCATOR_SKIPPED = url_main + "DSKIPPED']"



class LaunchesPage(HomePage):

    def quantity_tests(self):
        quantity_tests = self.driver.find_elements_by_xpath("//*[@class='gridRow__grid-row-wrapper--1dI9K']")
        return len(quantity_tests)

    def total_main(self, number):
        total_main = self.driver.find_element_by_xpath(LocatorsLaunchesPage.LOCATOR_TOTAL.format(number))
        return int(total_main.text)

    def passed_main(self, number):
        passed_main = self.driver.find_element_by_xpath(LocatorsLaunchesPage.LOCATOR_PASSED.format(number))
        return int(passed_main.text)

    def failed_main(self, number):
        failed_main = self.driver.find_element_by_xpath(LocatorsLaunchesPage.LOCATOR_FAILED.format(number))
        return int(failed_main.text)

    def skipped_main(self, number):
        skipped_main = self.driver.find_element_by_xpath(LocatorsLaunchesPage.LOCATOR_SKIPPED.format(number))
        return int(skipped_main.text)

    def total_main_click(self, number):
        total_click = self.driver.find_element_by_xpath(LocatorsLaunchesPage.LOCATOR_TOTAL.format(number))
        total_click.send_keys(Keys.ENTER)

    def test_score(self):
        passed = 0
        failed = 0
        skipped = 0
        total = 0
        while True:
            total_len = len(self.driver.find_elements_by_xpath("//*[@class='gridRow__grid-row--1pS-5']"))
            passed_len = len(self.driver.find_elements_by_xpath("//span[text()='Passed'] [@class='itemInfo__mobile-status--1qoKx']"))
            skipped_len = len(self.driver.find_elements_by_xpath("//span[text()='Skipped'] [@class='itemInfo__mobile-status--1qoKx']"))
            failed_len = len(self.driver.find_elements_by_xpath("//span[text()='Failed'] [@class='itemInfo__mobile-status--1qoKx']"))
            button = self.driver.find_element_by_css_selector('.pageButtons__page-buttons--uRADS ''.pageButton__page-button--OHYKN:nth-child(6)')
            classes_element = button.get_attribute('class')
            self.driver.execute_script("arguments[0].click();", button)
            total += total_len
            passed += passed_len
            failed += failed_len
            skipped += skipped_len
            if classes_element == 'pageButton__page-button--OHYKN pageButton__disabled--3-RYj':
                break
        return {'passed': passed, 'failed':failed, 'skipped':skipped, 'total':total}
