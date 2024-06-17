from browser_class import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from logger import logger


class BaseElement:
    def __init__(self, locator: str, name: str, by=By.XPATH):
        self.locator = locator
        self.name = name
        self.by = by

    def find_element(self):
        logger.info(f"Ищем на странице элемент {self.name}")
        Browser().wait().until(EC.presence_of_element_located((self.by, self.locator)))
        return Browser().find_element(self.by, self.locator)

    def find_elements(self):
        logger.info(f"Ищем на странице элементы {self.name}")
        Browser().wait().until(EC.presence_of_element_located((self.by, self.locator)))
        return Browser().find_elements(self.by, self.locator)

    def is_displayed(self):
        logger.info(f"Проверяем видимость элемента {self.name}")
        return self.find_element().is_displayed()

    def click_element(self):
        logger.info(f"Кликаем на {self.name}")
        self.find_element().click()

    def submit_element(self):
        logger.info(f"Отправляем заполненную форму нажатием на {self.name}")
        self.find_element().submit()

    def getting_text_element(self):
        logger.info(f"Получаем текст элемента {self.name}")
        return self.find_element().text

    def wait_visibility_element(self):
        logger.info(f"Ожидаем, что элемент {self.name} виден на странице")
        Browser().wait().until(
            EC.visibility_of_element_located((self.by, self.locator))
        )

    def wait_invisibility_element(self):
        logger.info(f"Ожидаем, что элемент {self.name} не виден на странице")
        Browser().wait().until(
            EC.invisibility_of_element_located((self.by, self.locator))
        )

    def get_attribute(self, name_attribute: str) -> str:
        logger.info(f"Получаем значение атрибута {name_attribute} элемента {self.name}")
        return self.find_element().get_attribute(name_attribute)

    def getting_list_text_elements(self):
        logger.info(f"Получаем список текста элементов {self.name}")
        list_text = []
        for element in self.find_elements():
            list_text.append(element.text)
        logger.info(f"Список текста элементов {self.name}: {list_text}")
        return list_text
