from .base_page import BasePage
from framework.button_element import ButtonElement


class MainPage(BasePage):
    def __init__(self):
        super().__init__(
            "//*[contains(@class,'category-cards')]", "Uniq element - Category cards"
        )

    __Alerts_frame_btn = ButtonElement(
        "//*[contains(text(),'Alerts')]//ancestor::*[contains(@class, 'top-card')]",
        "Section 'Alerts, Frame & Windows'",
    )
    __Elements_btn = ButtonElement(
        "//*[contains(text(),'Elements')]//ancestor::*[contains(@class, 'top-card')]",
        "Section 'Elements'",
    )

    def click_alerts_frame_btn(self):
        self.__Alerts_frame_btn.click_element()

    def click_elements_btn(self):
        self.__Elements_btn.click_element()
