from selenium import webdriver
from test_project.data.pars_data_dict import ParsingData
from framework.logger.logger import BaseLogger


class FactoryBrowser:

    @staticmethod
    def create_browser(browser_name: str = ParsingData.CHROME, page: str = ParsingData.URL_MAIN_PAGE):
        """Запускает определённый вид браузера в зависимости от указанного в настройках (Chrome/Firefox)"""
        BaseLogger.info(f"Выбираем браузер для запуска - {browser_name}")
        if browser_name == ParsingData.CHROME:
            options = webdriver.ChromeOptions()
            options.add_argument(ParsingData.OPTION_INCOGNITO_CHROME)
            options.add_argument(ParsingData.OPTION_FULL_SCREEN)
            driver = webdriver.Chrome(options=options)
        elif browser_name == ParsingData.FIREFOX:
            options = webdriver.FirefoxOptions()
            options.add_argument(ParsingData.OPTION_INCOGNITO_FIREFOX)
            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Передан некорректный браузер {browser_name}")
        return driver
