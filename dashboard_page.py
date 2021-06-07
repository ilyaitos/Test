

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    def clik_demo(self):
        clik_demo = self.driver.find_element_by_xpath('//*[@class="gridCell__grid-cell--3e2mS '
                                                    'gridCell__align-left--2beIG ''dashboardTable__name--1sWJs"]')
        clik_demo.click()

    def new_widget(self):
        new_widget = self.driver.find_element_by_xpath('(//div/button)[2]')
        new_widget.click()

    def widget_type(self, number):  # 1-20
        widget_type = self.driver.find_element_by_xpath('(//label)[' + str(number) + ']')
        widget_type.click()

    def button_next1(self):
        button_next1 = self.driver.find_element_by_xpath('//*[@class="ghostButton__icon--2rRly ghostButton__icon-at-right--3Ui7m"]')
        self.driver.execute_script("arguments[0].click();", button_next1)

    def button_demo_filter(self):
        button_demo_filter = self.driver.find_element_by_xpath('//*[@class="filtersItem__filter-item--1OosV"]')
        button_demo_filter.click()

    def clear_text(self):
        clear_text = self.driver.find_element_by_xpath('//input[@placeholder="Enter widget name"]')
        clear_text.clear()

    def widget_name(self, name):
        widget_name = self.driver.find_element_by_xpath('//input[@placeholder="Enter widget name"]')
        widget_name.send_keys(str(name))

    def button_next2(self):
        button_next2 = self.driver.find_element_by_xpath('//*[@class="ghostButton__icon--2rRly ghostButton__icon-at-right--3Ui7m"]')
        button_next2.click()

    def add_button(self):
        add_button = self.driver.find_element_by_xpath('//*[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]')
        add_button.click()

    def check(self, name):
        check = self.driver.find_element_by_xpath("//*[@class='widgetHeader__widget-name-block--7fZoV' and text()='" + str(name) + "']")
        return check

    def drop_buttons(self):
        drop_buttons = self.driver.find_element_by_xpath('//*[@class="userBlock__menu-icon--_7G3G"]')
        drop_buttons.click()

    def profile(self):
        profile = self.driver.find_element_by_xpath('//a[@href="#user-profile"][@class="userBlock__menu-item--6Fruf"]')
        profile.click()

    def drop_language(self):
        drop_language = self.driver.find_element_by_xpath('//*[@class="inputDropdown__select-block--2CQf-"]')
        drop_language.click()

    def russian_language(self):
        russian_language = self.driver.find_element_by_xpath('//*[@class="inputDropdownOption__dropdown-option--3Szk3"][2]')
        russian_language.click()

    def russian_text(self):
        russian_text = self.driver.find_element_by_xpath('// span[ @class ="inputDropdown__value--2gB2s"]')
        return russian_text.text

    def photo(self, picture):
        photo = self.driver.find_element_by_xpath('//input[@type="file"]')
        photo.send_keys(picture)