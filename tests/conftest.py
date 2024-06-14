from driver import *
import pytest
from logger import logger


@pytest.fixture(autouse=True)
def setup_and_close_browser():
    logger.info(f"Настраиваем окно браузера {settings.browser()}")
    driver.maximize_window()
    logger.info(f"Открываем в браузере страницу {settings.url_main_page()}")
    driver.get(settings.url_main_page())
    yield driver
    FactoryBrowser.create_browser(settings.browser()).close_browser()
