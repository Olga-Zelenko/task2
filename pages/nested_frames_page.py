from .base_page import BasePage
from framework.container_element import Container
from forms_pages.left_menu_form import LeftMenuForm
from browser_class import Browser
from framework.iframe_element import Iframe


class NestedFramesPage(BasePage):
    __IFRAME1_PARENT = ("//*[@id='frame1']", "Frame 1 - parent")
    __TEXT_IFRAME1_PARENT = (
        "//*[contains(text(),'Parent frame')]",
        "Text in Frame1-parent",
    )
    __IFRAME_CHILD = ("//iframe[@srcdoc]", "Iframe Child")
    __TEXT_IFRAME_CHILD = (
        "//*[contains(text(),'Child Iframe')]",
        "Text in Frame-child",
    )

    __left_menu = LeftMenuForm()

    @property
    def left_menu(self):
        return self.__left_menu

    def __init__(self):
        super().__init__(
            "//*[@id='framesWrapper']//*[contains(text(),'Nested Frames')]",
            "Nested frames form",
        )

    def switch_iframe1_parent(self):
        Browser().switch_to_iframe(Iframe(*self.__IFRAME1_PARENT).find_element())

    def getting_text_iframe1_parent(self):
        return Container(*self.__TEXT_IFRAME1_PARENT).find_element().text

    def switch_iframe_child(self):
        Browser().switch_to_iframe(Iframe(*self.__IFRAME_CHILD).find_element())

    def getting_text_iframe_child(self):
        return Container(*self.__TEXT_IFRAME_CHILD).find_element().text

    def switch_parent_frame(self):
        Browser().switch_parent_frame()
