from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver import driver, wait
from selenium.webdriver.common.alert import Alert
from logger import logger
from urllib.parse import urlparse


class BasePage(object):

    def __init__(self, locator_uniq_el: str, name_uniq_el: str):
        logger.info(f"Инициализируем страницу {self.__class__.__name__}")
        self.locator_uniq_el = locator_uniq_el
        self.name_uniq_el = name_uniq_el
        self.by = By.XPATH

    def is_open_page(self) -> bool:
        logger.info(f"Проверяем, что страница {self.__class__.__name__} открылась")
        wait.until(EC.presence_of_element_located((self.by, self.locator_uniq_el)))
        return driver.find_element(self.by, self.locator_uniq_el).is_displayed()

    @staticmethod
    def scroll_down(offset=0) -> None:
        if offset:
            driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    @staticmethod
    def scroll_up(offset=0) -> None:
        if offset:
            driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    @staticmethod
    def switch_alert() -> Alert:
        logger.info(f"Переключаемся на всплывающее окно")
        return driver.switch_to.alert

    def getting_text_alert(self) -> str:
        logger.info(f"Получаем текст всплывающего окна")
        return self.switch_alert().text

    def accept_alert(self) -> None:
        logger.info(f"Подтверждаем сообщение всплывающего окна")
        self.switch_alert().accept()

    @staticmethod
    def getting_list_frame() -> list:
        logger.info(f"Получаем список всех окон текущей страницы")
        return driver.window_handles

    def send_keys_alert(self, text) -> None:
        logger.info(f"Отправляем сообщение '{text}' в всплывающее окно")
        self.switch_alert().send_keys(text)

    @staticmethod
    def switch_parent_frame() -> None:
        logger.info(f"Переключаемся на parent frame")
        return driver.switch_to.parent_frame()

    @staticmethod
    def current_window_handle() -> str:
        window_handle = driver.current_window_handle
        logger.info(f"Текущий window_handle - {window_handle}")
        return window_handle

    @staticmethod
    def window_handles() -> list[str]:
        window_handles = driver.window_handles
        logger.info(f"Список window_handles - {window_handles}")
        return window_handles

    @staticmethod
    def switch_to_window(name_window):
        logger.info(f"Переключаемся на новый window_handles")
        return driver.switch_to.window(name_window)

    @staticmethod
    def current_url() -> str:
        current_url = driver.current_url
        logger.info(f"Получаем текущий url страницы - '{current_url}'")
        return current_url

    def get_relative_link(self):
        url = urlparse(self.current_url())
        relative_link = url.path
        logger.info(f"Получаем относительную ссылку текущего url - '{relative_link}'")
        return relative_link

    @staticmethod
    def close_current_window():
        logger.info(f"Закрываем текущую вкладку")
        driver.close()

    def check_new_window_open(self, action) -> bool:
        list_window_handles_before = self.window_handles()
        logger.info(f"Проверяем, что открылась новая вкладка")
        action()
        list_window_handles_after = self.window_handles()
        return len(list_window_handles_after) - len(list_window_handles_before) == 1
