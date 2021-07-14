from selenium.webdriver.common.keys import Keys
from home_page import HomePage

class LocatorsDashboardPage:

    LOCATOR_BUTTON_NEXT = '(//div[@id="modal-root"]//button[@type="button"])[last()]'
    LOCATOR_BUTTON_DEMO_FILTER = '//*[@class="filtersItem__filter-item--1OosV"]'
    LOCATOR_BUTTON_NEW_WIDGET_TYPE = '(//div/button)[2]'
    LOCATOR_BUTTON_WIDGET_TYPE = '(//label[@class="inputRadio__input-radio--1Ayx8"])'
    LOCATOR_WIDGET_NAME = '//input[@placeholder="Enter widget name"]'
    LOCATOR_WIDGET_ADD = '//*[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_BUTTON_DROP_LANGUAGE = '//*[@class="inputDropdown__select-block--2CQf-"]'
    LOCATOR_PHOTO = '//input[@type="file"]'
    LOCATOR_BUTTON_DEMO = "//*[@class='gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs'][text()='{}']"


class DashboardPage(HomePage):

    def clik_demo(self, name):
        clik_demo = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_BUTTON_DEMO.format(name))
        clik_demo.click()

    def new_widget_type(self, name):
        click_button_new_widget = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_BUTTON_NEW_WIDGET_TYPE)
        click_button_new_widget.click()
        buttons_widgets_type = self.driver.find_elements_by_xpath(LocatorsDashboardPage.LOCATOR_BUTTON_WIDGET_TYPE)
        list_widgets = []
        for x in buttons_widgets_type:
            list_widgets += [x.text]
        widget_index = list_widgets.index(name) + 1
        click_button_widget_type = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_BUTTON_WIDGET_TYPE + '[{}]'.format(widget_index))
        click_button_widget_type.click()
        click_button_next = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_BUTTON_NEXT)
        click_button_next.send_keys(Keys.ENTER)



    def click_button_next(self):
        click_button_next = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_BUTTON_NEXT)
        click_button_next.send_keys(Keys.ENTER)


    def click_button_demo_filter(self):
        click_button_demo_filter = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_BUTTON_DEMO_FILTER)
        click_button_demo_filter.click()

    def widget_name(self, name):
        clear_text = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_WIDGET_NAME)
        clear_text.clear()
        widget_name = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_WIDGET_NAME)
        widget_name.send_keys(str(name))

    def click_button_add(self):
        click_button_add = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_WIDGET_ADD)
        click_button_add.click()

    def score_widget(self):
        score_widget = self.driver.find_elements_by_xpath('//*[@class="react-grid-item widgetsGrid__widget-view--dVnmj react-draggable cssTransforms react-resizable"]')#('//*[@class="react-grid-item widgetsGrid__widget-view--dVnmj react-draggable cssTransforms react-resizable"]')
        list = []
        for x in score_widget:
            list += [x.text]
        return score_widget.text


    # def check(self, name):
    #     check = self.driver.find_element_by_xpath("//*[@class='widgetHeader__widget-name-block--7fZoV' and text()='" + str(name) + "']")
    #     return check

    def drop_button_language(self):
        drop_language = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_BUTTON_DROP_LANGUAGE)
        drop_language.click()

    def button_russian_language(self):
        button_russian_language = self.driver.find_element_by_xpath('//*[@class="inputDropdownOption__dropdown-option--3Szk3"][2]')
        button_russian_language.click()

    def russian_text(self):
        russian_text = self.driver.find_element_by_xpath('// span[ @class ="inputDropdown__value--2gB2s"]')
        return russian_text.text

    def download_photo(self, picture):
        download_photo = self.driver.find_element_by_xpath(LocatorsDashboardPage.LOCATOR_PHOTO)
        download_photo.send_keys(picture)