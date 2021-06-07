from selenium.webdriver.common.keys import Keys


class LaunchesPage:

    def __init__(self, driver):
        self.driver = driver

    def clik_launches(self):
        clik_launches = self.driver.find_element_by_xpath('//a[@href="#default_personal/launches"]')
        clik_launches.click()

    def number_tests(self):
        number_tests = self.driver.find_elements_by_xpath("//*[@class='gridRow__grid-row-wrapper--1dI9K']")
        return len(number_tests)

    def total_main(self, number):
        total_main = self.driver.find_element_by_xpath("//a[@href='#default_personal/launches/all/" + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']")
        return int(total_main.text)

    def passed_main(self, number):
        passed_main = self.driver.find_element_by_xpath("//*[@href='#default_personal/launches/all/" + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED']")
        return int(passed_main.text)

    def failed_main(self, number):
        failed_main = self.driver.find_element_by_xpath("//*[@href='#default_personal/launches/all/" + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DFAILED%252CINTERRUPTED']")
        return int(failed_main.text)

    def skipped_main(self, number):
        skipped_main = self.driver.find_element_by_xpath("//*[@href='#default_personal/launches/all/" + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DSKIPPED']")
        return int(skipped_main.text)

    def total_click(self, number ):
        total_click = self.driver.find_element_by_xpath("//a[@href='#default_personal/launches/all/" + str(number) + "?item0Params=filter.eq.hasStats%3Dtrue%26filter.eq.hasChildren%3Dfalse%26filter.in.type%3DSTEP%26filter.in.status%3DPASSED%252CFAILED%252CSKIPPED%252CINTERRUPTED']")
        total_click.send_keys(Keys.ENTER)

    def score(self, title): # Passed,Skipped,Failed
        score = self.driver.find_elements_by_xpath("//span[text()='" + title + "'] [@class='itemInfo__mobile-status--1qoKx']")
        return  len(score)

    def total_score(self):
        total_score = self.driver.find_elements_by_xpath("//*[@class='gridRow__grid-row--1pS-5']")
        return len(total_score)

    def button_next(self):
        button_next = self.driver.find_element_by_css_selector('.pageButtons__page-buttons--uRADS ''.pageButton__page-button--OHYKN:nth-child(6)')
        return button_next
