import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from typing import Final

from tests.pages.main_page import MainPage

# URL для Selenium Grid и базовый URL сайта
SELENIUM_GRID_URL: Final = os.getenv("SELENIUM_GRID_URL", "http://localhost:4444")
BASE_URL: Final = os.getenv(
    "BASE_URL", "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
)
LOCAL_RUN: Final = os.getenv("LOCAL_RUN", "false").lower() == "true"


@pytest.fixture
def driver(request):
    """
    Фикстура для инициализации веб-драйвера Chrome.
    В зависимости от флага LOCAL_RUN будет запускать браузер через Selenium Grid или локально.
    """
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    if LOCAL_RUN:
        logger.info("Запуск браузера локально.")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        logger.info("Запуск браузера через Selenium Grid.")
        driver = webdriver.Remote(
            command_executor=SELENIUM_GRID_URL,
            options=chrome_options,
        )

    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()


@pytest.fixture
def open_website_and_clear(driver):
    """
    Фикстура для открытия сайта, очистки localStorage, sessionStorage и cookies.
    """
    logger.info(f"Ожидаем открытие {BASE_URL}")
    driver.get(BASE_URL)
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.delete_all_cookies()
    yield driver

@pytest.fixture
def login_logout(open_website_and_clear):
    page = MainPage(open_website_and_clear)
    page.login()
    yield open_website_and_clear
    page.logout()
    logger.info(f"Отчёт allure: http://localhost:4040")