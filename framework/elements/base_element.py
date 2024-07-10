from selenium.webdriver.remote.webelement import WebElement
from framework.browser.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from framework.logger.logger import BaseLogger


class BaseElement:
    def __init__(self, locator: str, name: str, by=By.XPATH):
        self.by = by
        self.locator = locator
        self.name = name

    def find_element(self) -> WebElement:
        return Browser().get_driver().find_element(self.by, self.locator)

    def find_elements(self) -> list[WebElement]:
        return Browser().get_driver().find_elements(self.by, self.locator)

    def is_displayed(self) -> bool:
        BaseLogger.info(f"Проверяем видимость элемента {self.name}")
        return self.find_element().is_displayed()

    def click_element(self):
        BaseLogger.info(f"Кликаем на {self.name}")
        self.find_element().click()

    def getting_text_element(self) -> str:
        BaseLogger.info(f"Получаем текст элемента {self.name}")
        return self.find_element().text

    def wait_visibility_element(self) -> [bool, str]:
        try:
            Browser().wait().until(EC.visibility_of_element_located((self.by, self.locator)))
        except TimeoutError:
            BaseLogger.error("Элемент не виден на странице!")

    def wait_invisibility_element(self) -> [bool, str]:
        try:
            Browser().wait().until(EC.invisibility_of_element_located((self.by, self.locator)))
        except TimeoutError:
            BaseLogger.error("Элемент виден на странице!")

    def get_attribute(self, name_attribute: str) -> str:
        return self.find_element().get_attribute(name_attribute)

    def getting_list_text_elements(self) -> list[str]:
        BaseLogger.info(f"Получаем список текста элементов {self.name}")
        list_text = []
        for element in self.find_elements():
            list_text.append(element.text)
        BaseLogger.info(f"Список текста элементов {self.name}: {list_text}")
        return list_text
