

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = '//a[@href="#default_personal/'
        self.url_main = "//a[@href='#default_personal/launches/all/"

    def click_button_dashboard(self):
        click_button_dashboard = self.driver.find_element_by_xpath(self.url + 'dashboard"][@class="sidebarButton__nav-link--2TC0L sidebarButton__active--3dvg_"]')
        click_button_dashboard.click()

    def click_button_launches(self):
        click_button_launches = self.driver.find_element_by_xpath(self.url +'launches"]')
        click_button_launches.click()

    def click_button_filters(self):
        click_button_filters = self.driver.find_element_by_xpath(self.url + 'filters"]')
        click_button_filters.click()

    def click_button_userdebug(self):
        click_button_userdebug = self.driver.find_element_by_xpath(self.url + 'userdebug/all"]')
        click_button_userdebug.click()

    def click_button_members(self):
        click_button_members = self.driver.find_element_by_xpath(self.url + 'members"]')
        click_button_members.click()

    def click_button_settings(self):
        click_button_settings = self.driver.find_element_by_xpath(self.url + 'settings"]')
        click_button_settings.click()

    def click_drop_buttons(self):
        click_drop_buttons = self.driver.find_element_by_xpath('//*[@class="userBlock__menu-icon--_7G3G"]')
        click_drop_buttons.click()

    def click_button_profile(self):
        click_button_profile = self.driver.find_element_by_xpath('//a[@href="#user-profile"][@class="userBlock__menu-item--6Fruf"]')
        click_button_profile.click()
        
    def click_button_api(self):
        click_button_api = self.driver.find_element_by_xpath('//a[@href="#api"]')
        click_button_api.click()

    def click_button_logout(self):
        click_button_logout = self.driver.find_element_by_xpath('//div[@class="userBlock__menu-item--6Fruf"] ')
        click_button_logout.click()

    def click_button_default_personal(self):
        click_button_default1 = self.driver.find_element_by_xpath('//div[@class="projectSelector__current-project-name--2mlA_"]')
        click_button_default1.click()
        click_button_default2 = self.driver.find_element_by_xpath('//div[@class="projectSelector__projects-list--8H9vo projectSelector__shown--mUoaC"]')
        click_button_default2.click()
