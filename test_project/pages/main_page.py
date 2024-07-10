from framework.base_page.base_page import BasePage
from framework.elements.button import Button
from framework.browser.browser import Browser


class MainPage(BasePage):
    __ALERTS_FRAME_BTN = Button("//*[contains(text(),'Alerts')]//ancestor::*[contains(@class, 'top-card')]",
                                "Section 'Alerts, Frame & Windows'")
    __ELEMENTS_BTN = Button("//*[contains(text(),'Elements')]//ancestor::*[contains(@class, 'top-card')]",
                            "Section 'Elements'")
    __UNIQ_ELEM_LOCATOR = "//*[contains(@class,'category-cards')]"

    def __init__(self):
        super().__init__(self.__UNIQ_ELEM_LOCATOR, "Uniq element - Category cards")

    def click_alerts_frame_btn(self):
        self.__ALERTS_FRAME_BTN.click_element()

    def click_elements_btn(self):
        self.__ELEMENTS_BTN.click_element()

    def switch_to_window(self, name_window):
        return Browser().get_driver().switch_to.window(name_window)
