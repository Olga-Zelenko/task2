from .base_page import BasePage
from framework.button_element import Button
from framework.container_element import Container
from browser_class import Browser


class AlertsPage(BasePage):
    __BTN_CLICK_ALERT = ("//*[@id='alertButton']", "Click Button to see alert")
    __BTN_CLICK_CONFIRM_BOX = (
        "//*[@id='confirmButton']",
        "Click button to appear confirm box",
    )
    __MESSAGE_CONFIRM_BOX = (
        "//*[@id='confirmResult']",
        "Message about selected in confirm box",
    )
    __BTN_CLICK_PROMPT_BOX = (
        "//*[@id='promtButton']",
        "Click button to see prompt box",
    )
    __MESSAGE_PROMPT_BOX = (
        "//*[@id='promptResult']",
        "Message about entered in prompt box",
    )

    def __init__(self):
        super().__init__("//*[@id='javascriptAlertsWrapper']", "Alerts form")

    def click_btn_to_see_alert(self):
        Button(*self.__BTN_CLICK_ALERT).click_element()

    def click_btn_confirm_box(self):
        Button(*self.__BTN_CLICK_CONFIRM_BOX).click_element()

    def getting_text_message_confirm_box(self):
        return Container(*self.__MESSAGE_CONFIRM_BOX).getting_text_element()

    def click_btn_prompt_box(self):
        Button(*self.__BTN_CLICK_PROMPT_BOX).click_element()

    def getting_text_message_prompt_box(self):
        return Container(*self.__MESSAGE_PROMPT_BOX).getting_text_element()

    def getting_text_alert(self) -> str:
        return Browser().switch_alert().text

    def accept_alert(self) -> None:
        Browser().switch_alert().accept()

    def getting_list_frame(self) -> list:
        return Browser().window_handles()

    def send_keys_alert(self, text) -> None:
        Browser().switch_alert().send_keys(text)
