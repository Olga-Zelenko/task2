from .base_page import BasePage
from framework.container_element import ContainerElement
from framework.iframe_element import IframeElement


class FramesPage(BasePage):
    def __init__(self):
        super().__init__(
            "//*[@id='framesWrapper']//*[contains(text(),'Frames')]",
            "Nested frames form",
        )

    __Iframe1 = IframeElement("//*[@id='frame1']", "Frame 1")
    __Iframe2 = IframeElement("//*[@id='frame2']", "Frame 2")
    __Text_iframe = ContainerElement("//*[@id='sampleHeading']", "Text in frame")

    def switch_iframe_1(self):
        self.__Iframe1.find_and_switch_to_iframe()

    def getting_text_iframe_1(self):
        return self.__Text_iframe.getting_text_element()

    def switch_iframe_2(self):
        self.__Iframe2.find_and_switch_to_iframe()

    def getting_text_iframe_2(self):
        return self.__Text_iframe.getting_text_element()
