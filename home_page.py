from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LocatorsHomePage:

    url_main_pages = '//a[@href="#default_personal/'

    LOCATOR_BUTTON_LAUNCHES = url_main_pages + 'launches"]'
    LOCATOR_BUTTON_FILTERS = url_main_pages + 'filters"]'
    LOCATOR_BUTTON_DASHBOARD = url_main_pages + 'dashboard"][@class="sidebarButton__nav-link--2TC0L sidebarButton__active--3dvg_"]'
    LOCATOR_BUTTON_USERDEBUG = url_main_pages + 'userdebug/all"]'
    LOCATOR_BUTTON_PROJECT_MEMBERS = url_main_pages + 'members"]'
    LOCATOR_BUTTON_SETTINGS = url_main_pages + 'settings"]'
    LOCATOR_BUTTON_DROP = '//*[@class="userBlock__menu-icon--_7G3G"]'
    LOCATOR_BUTTON_PROFILE = '//a[@href="#user-profile"][@class="userBlock__menu-item--6Fruf"]'
    LOCATOR_BUTTON_API = '//a[@href="#api"]'
    LOCATOR_BUTTON_LOGOUT = '//div[@class="userBlock__menu-item--6Fruf"]'
    LOCATOR_BUTTON_DEFAULT_PERSONAL_1 = '//div[@class="projectSelector__current-project-name--2mlA_"]'
    LOCATOR_BUTTON_DEFAULT_PERSONAL_2 = '//div[@class="projectSelector__projects-list--8H9vo projectSelector__shown--mUoaC"]'

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.url_main = "//a[@href='#default_personal/launches/all/"

    def click_button_dashboard(self):
        click_button_dashboard = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_DASHBOARD)
        click_button_dashboard.click()

    def click_button_launches(self):
        click_button_launches = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_LAUNCHES)
        click_button_launches.click()

    def click_button_filters(self):
        click_button_filters = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_FILTERS)
        click_button_filters.click()

    def click_button_userdebug(self):
        click_button_userdebug = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_USERDEBUG)
        click_button_userdebug.click()

    def click_button_project_members(self):
        click_button_project_members = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_PROJECT_MEMBERS)
        click_button_project_members.click()

    def click_button_settings(self):
        click_button_settings = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_SETTINGS)
        click_button_settings.click()

    def click_button_profile(self):
        click_drop_buttons = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_DROP)
        click_drop_buttons.click()
        click_button_profile = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_PROFILE)
        click_button_profile.click()
        
    def click_button_api(self):
        click_drop_buttons = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_DROP)
        click_drop_buttons.click()
        click_button_api = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_API)
        click_button_api.click()

    def click_button_logout(self):
        click_drop_buttons = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_DROP)
        click_drop_buttons.click()
        click_button_logout = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_LOGOUT)
        click_button_logout.click()

    def click_button_default_personal(self):
        click_button_default1 = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_DEFAULT_PERSONAL_1)
        click_button_default1.click()
        click_button_default2 = self.driver.find_element_by_xpath(LocatorsHomePage.LOCATOR_BUTTON_DEFAULT_PERSONAL_2)
        click_button_default2.click()
