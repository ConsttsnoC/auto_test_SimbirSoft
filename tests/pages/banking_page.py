import allure
import pytest
from loguru import logger
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.csv_helper import HelpCsv
from .main_page import MainPage


class BankingPage(MainPage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.help_csv = HelpCsv(driver)

    @allure.step("Авторизация и внесение / списание депозита")
    def authorize_and_manage_deposit(self):
        """
        Метод для выполнения авторизации пользователя, внесения и списания депозита,
        где сумма депозита равна числу Фибоначчи для текущего дня месяца + 1.
        """
        try:
            logger.info("Начало процесса внесения депозита")
            self.making_deposit()
            logger.info("Начало процесса списания депозита")
            self.withdrawal_of_deposit()
            logger.info("Начало проверки, что баланс равен 0 после снятия депозита.")
            self.check_for_balance_zero()
            self.wait_for_body_to_load()
            logger.info("Начинаем процесс сохранения транзакций в CSV файл")
            self.help_csv.save_transactions_to_csv()
        except Exception as e:
            logger.error(f"Произошла ошибка: {e}")
            allure.attach(
                f"Ошибка в тесте: {e}",
                name="Ошибка",
                attachment_type=allure.attachment_type.TEXT,
            )
            pytest.fail(self.make_screenshot("Ошибка в тесте"))
