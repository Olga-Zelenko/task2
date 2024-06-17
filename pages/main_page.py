from .base_page import BasePage
from framework.button_element import Button


class MainPage(BasePage):
    __ALERTS_FRAME_BTN = (
        "//*[contains(text(),'Alerts')]//ancestor::*[contains(@class, 'top-card')]",
        "Section 'Alerts, Frame & Windows'",
    )
    __ELEMENTS_BTN = (
        "//*[contains(text(),'Elements')]//ancestor::*[contains(@class, 'top-card')]",
        "Section 'Elements'",
    )

    def __init__(self):
        super().__init__(
            "//*[contains(@class,'category-cards')]", "Uniq element - Category cards"
        )

    def click_alerts_frame_btn(self):
        Button(*self.__ALERTS_FRAME_BTN).click_element()

    def click_elements_btn(self):
        Button(*self.__ELEMENTS_BTN).click_element()
