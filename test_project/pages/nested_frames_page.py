from selenium.webdriver.common.by import By
from framework.base_page.base_page import BasePage
from framework.elements.text_box import TextBox
from test_project.forms.left_menu_form import LeftMenuForm
from framework.browser.browser import Browser


class NestedFramesPage(BasePage):
    __IFRAME1_PARENT = (By.XPATH, "//*[@id='frame1']")
    __TEXT_IFRAME1_PARENT = TextBox("//*[contains(text(),'Parent frame')]", "Text in Frame1-parent")
    __IFRAME_CHILD = (By.XPATH, "//iframe[@srcdoc]")
    __TEXT_IFRAME_CHILD = TextBox("//*[contains(text(),'Child Iframe')]", "Text in Frame-child")
    __UNIQ_ELEM_LOCATOR = "//*[@id='framesWrapper']//*[contains(text(),'Nested Frames')]"

    __left_menu = LeftMenuForm()

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Nested frames form")

    def switch_iframe1_parent(self):
        Browser().switch_to_iframe(Browser().get_driver().find_element(*self.__IFRAME1_PARENT))

    def getting_text_iframe1_parent(self):
        return self.__TEXT_IFRAME1_PARENT.find_element().text

    def switch_iframe_child(self):
        Browser().switch_to_iframe(Browser().get_driver().find_element(*self.__IFRAME_CHILD))

    def getting_text_iframe_child(self):
        return self.__TEXT_IFRAME_CHILD.find_element().text

    def switch_parent_frame(self):
        Browser().switch_parent_frame()
