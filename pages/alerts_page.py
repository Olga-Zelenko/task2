from .base_page import BasePage
from framework.button_element import Button
from framework.container_element import Container


class AlertsPage(BasePage):
    def __init__(self):
        super().__init__("//*[@id='javascriptAlertsWrapper']", "Alerts form")

    __BTN_CLICK_ALERT = Button("//*[@id='alertButton']", "Click Button to see alert")
    __BTN_CLICK_CONFIRM_BOX = Button(
        "//*[@id='confirmButton']", "Click button to appear confirm box"
    )
    __MESSAGE_CONFIRM_BOX = Container(
        "//*[@id='confirmResult']", "Message about selected in confirm box"
    )
    __BTN_CLICK_PROMPT_BOX = Button(
        "//*[@id='promtButton']", "Click button to see prompt box"
    )
    __MESSAGE_PROMPT_BOX = Container(
        "//*[@id='promptResult']", "Message about entered in prompt box"
    )

    def click_btn_to_see_alert(self):
        self.__BTN_CLICK_ALERT.click_element()

    def click_btn_confirm_box(self):
        self.__BTN_CLICK_CONFIRM_BOX.click_element()

    def getting_text_message_confirm_box(self):
        return self.__MESSAGE_CONFIRM_BOX.getting_text_element()

    def click_btn_prompt_box(self):
        self.__BTN_CLICK_PROMPT_BOX.click_element()

    def getting_text_message_prompt_box(self):
        return self.__MESSAGE_PROMPT_BOX.getting_text_element()
