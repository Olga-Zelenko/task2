from .base_page import BasePage
from browser_class import Browser
from framework.container_element import Container
from framework.iframe_element import Iframe


class FramesPage(BasePage):
    __IFRAME1 = ("//*[@id='frame1']", "Frame 1")
    __IFRAME2 = ("//*[@id='frame2']", "Frame 2")
    __TEXT_IFRAME = ("//*[@id='sampleHeading']", "Text in frame")

    def __init__(self):
        super().__init__(
            "//*[@id='framesWrapper']//*[contains(text(),'Frames')]",
            "Nested frames form",
        )

    def switch_iframe_1(self):
        Browser().switch_to_iframe(Iframe(*self.__IFRAME1).find_element())

    def getting_text_iframe_1(self):
        return Container(*self.__TEXT_IFRAME).find_element().text

    def switch_iframe_2(self):
        Browser().switch_to_iframe(Iframe(*self.__IFRAME2).find_element())

    def switch_parent_frame(self):
        Browser().switch_parent_frame()
