import pytest
from framework.logger.logger import BaseLogger
from framework.browser.browser import Browser
from test_project.data.pars_data_dict import ParsingData


@pytest.fixture(autouse=True)
def setup_and_close_browser():
    BaseLogger.info("Запускаем браузер")
    driver = Browser.get_browser()
    driver.setup_driver()
    driver.maximize_window()
    BaseLogger.info(f"Открываем главную страницу {ParsingData.URL_MAIN_PAGE}")
    driver.go_to_page(ParsingData.URL_MAIN_PAGE)
    yield driver
    BaseLogger.info("Закрываем браузер")
    driver.close_browser()
