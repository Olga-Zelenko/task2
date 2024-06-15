from .base_page import BasePage
from framework.container_element import ContainerElement
from framework.iframe_element import IframeElement
from forms_pages.left_menu_form import LeftMenuForm


class NestedFramesPage(BasePage):
    def __init__(self):
        super().__init__(
            "//*[@id='framesWrapper']//*[contains(text(),'Nested Frames')]",
            "Nested frames form",
        )

    left_menu = LeftMenuForm()

    __Iframe1_Parent = IframeElement("//*[@id='frame1']", "Frame 1 - parent")
    __Text_iframe1_parent = ContainerElement(
        "//*[contains(text(),'Parent frame')]", "Text in Frame1-parent"
    )
    __Iframe_child = IframeElement("//iframe[@srcdoc]", "Iframe Child")
    __Text_iframe_child = ContainerElement(
        "//*[contains(text(),'Child Iframe')]", "Text in Frame-child"
    )

    def switch_iframe1_parent(self):
        self.__Iframe1_Parent.find_and_switch_to_iframe()

    def getting_text_iframe1_parent(self):
        return self.__Text_iframe1_parent.getting_text_element()

    def switch_iframe_child(self):
        self.__Iframe_child.find_and_switch_to_iframe()

    def getting_text_iframe_child(self):
        return self.__Text_iframe_child.getting_text_element()
