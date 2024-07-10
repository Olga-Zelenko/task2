from selenium.webdriver.common.by import By
from framework.base_page.base_page import BasePage
from framework.browser.browser import Browser
from framework.elements.text_box import TextBox


class FramesPage(BasePage):
    __IFRAME_FIRST = (By.XPATH, "//*[@id='frame1']")
    __IFRAME_LAST = (By.XPATH, "//*[@id='frame2']")
    __TEXT_IFRAME = TextBox("//*[@id='sampleHeading']", "Text in frame")
    __UNIQ_ELEM_LOCATOR = "//*[@id='framesWrapper']//*[contains(text(),'Frames')]"

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Nested frames form")

    def switch_iframe_1(self):
        Browser().switch_to_iframe(Browser().get_driver().find_element(*self.__IFRAME_FIRST))

    def getting_text_iframe(self):
        return self.__TEXT_IFRAME.find_element().text

    def switch_iframe_2(self):
        Browser().switch_to_iframe(Browser().get_driver().find_element(*self.__IFRAME_LAST))

    def switch_parent_frame(self):
        Browser().switch_parent_frame()
