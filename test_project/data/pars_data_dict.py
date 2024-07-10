from framework.utilities.pars_config import ParsConfig

data = ParsConfig("test_project\data\config.json").parsing_config()


class ParsingData:
    """Обрабатывает данные из config-словаря"""
    URL_MAIN_PAGE = data["url_main_page"]
    TIMEOUT = data["timeout"]
    MAX_LEN_SRT = data["max_len_srt"]
    CHROME = data["chrome"]
    FIREFOX = data["firefox"]
    OPTION_INCOGNITO_CHROME = data["option_incognito_chrome"]
    OPTION_INCOGNITO_FIREFOX = data["option_incognito_firefox"]
    OPTION_FULL_SCREEN = data["option_full_screen"]
