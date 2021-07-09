from selenium.webdriver.common.keys import Keys
from home_page import HomePage
#
# class LocatorsLaunchesPage:
#
#     url_main = "//a[@href='#default_personal/launches/all/"
#     LOCATOR_BUTTON_TOTAL = url_main + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']"
#
class LaunchesPage(HomePage):

    def number_tests(self):
        number_tests = self.driver.find_elements_by_xpath("//*[@class='gridRow__grid-row-wrapper--1dI9K']")
        return len(number_tests)

    def total_main(self, number):
        total_main = self.driver.find_element_by_xpath(self.url_main + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']")
        return int(total_main.text)

    def passed_main(self, number):
        passed_main = self.driver.find_element_by_xpath(self.url_main + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED']")
        return int(passed_main.text)

    def failed_main(self, number):
        failed_main = self.driver.find_element_by_xpath(self.url_main + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DFAILED%252CINTERRUPTED']")
        return int(failed_main.text)

    def skipped_main(self, number):
        skipped_main = self.driver.find_element_by_xpath(self.url_main + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DSKIPPED']")
        return int(skipped_main.text)

    def total_click(self, number):
        total_click = self.driver.find_element_by_xpath(self.url_main + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']")
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
