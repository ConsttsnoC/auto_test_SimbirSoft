import allure
import pytest
from loguru import logger
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.csv_helper import HelpCsv
from utils.fibonacci import get_fibonacci_for_today
from .base_page import BasePage
from .locators import Locators


class BankingPage(BasePage):

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
            logger.info("Начало процесса авторизации, внесения и списания депозита.")
            with allure.step("Нажатие на кнопку 'Клиент'"):
                self.find_and_click_element(Locators.CUSTOMER_LOGIN_BUTTON)
                logger.info("Кнопка 'Клиент' нажата.")

            with allure.step("Выбор имени пользователя"):
                self.find_and_click_element(Locators.SELECT_USER_NAME)
                logger.info("Выбор имени пользователя.")

            with allure.step("Выбор имени пользователя: Гарри Поттер"):
                self.find_and_click_element(Locators.ELEMENT_HARRY_POTTER)
                logger.info("Выбрано имя пользователя: Гарри Поттер.")

            with allure.step("Нажатие на кнопку 'Войти'"):
                self.find_and_click_element(Locators.LOGIN_BUTTON)
                logger.info("Кнопка 'Войти' нажата.")

            with allure.step("Нажатие на кнопку 'Депозит'"):
                self.find_and_click_element(Locators.DEPOSIT_BUTTON)
                logger.info("Кнопка 'Депозит' нажата.")

            deposit_amount = get_fibonacci_for_today()
            deposit_amount_str = str(deposit_amount)

            with allure.step(f"Установка суммы депозита: {deposit_amount_str}"):
                self.find_and_send(Locators.DEPOSIT_INPUT_FIELD, deposit_amount_str)
                logger.info(f"Сумма депозита установлена: {deposit_amount_str}.")

            with allure.step("Нажатие на кнопку 'Deposit' для подтверждения депозита"):
                self.find_and_click_element(Locators.DEPOSIT_OK_BUTTON)
                logger.info("Кнопка 'Deposit' для подтверждения депозита нажата.")

            logger.info("Процесс входа и внесения депозита завершён успешно.")

            with allure.step(
                "Нажатие на кнопку 'Withdrawl' для переключения на списания."
            ):
                self.find_and_click_element(Locators.WRITTEN_FROM_ACCOUNT)
                logger.info("Кнопка 'Withdrawl' для переключения на списания.")

            self.wait_for_body_to_load()

            with allure.step(f"Установка суммы снятия депозита: {deposit_amount_str}"):
                self.find_and_send(Locators.INPUT_WITHDRAW_AMOUNT, deposit_amount_str)
                logger.info(f"Сумма снятия депозита установлена: {deposit_amount_str}.")

            with allure.step(
                "Нажатие на кнопку 'Withdraw' для подтверждения снятия депозита"
            ):
                self.find_and_click_element(Locators.WITHDRAW_CONFIRM_BUTTON)
                logger.info(
                    "Кнопка 'Withdraw' для подтверждения снятия депозита нажата."
                )

            with allure.step("Проверка, что баланс равен 0 после снятия депозита."):
                balance_element = self.find_element(Locators.LOCATOR_BALANCE)
                balance_value = int(balance_element.text.strip())

                assert (
                    balance_value == 0
                ), f"Баланс не равен 0. Текущий баланс: {balance_value}"
                logger.info(f"Баланс успешно проверен и равен {balance_value}.")
                # Переход к разделу транзакций
            with allure.step("Переход к разделу транзакций."):
                self.find_and_click_element(Locators.TRANSACTIONS_BUTTON)
                logger.info("Перейдено к разделу транзакций.")
            self.wait_for_body_to_load()
            self.help_csv.save_transactions_to_csv()
            with allure.step("Разлогиниваемся"):
                self.find_and_click_element(Locators.LOGOUT_BUTTON)
                logger.info("Выход из профиля успешен.")

        except Exception as e:
            logger.error(f"Произошла ошибка: {e}")
            allure.attach(
                f"Ошибка: {e}",
                name="Ошибка входа",
                attachment_type=allure.attachment_type.TEXT,
            )
            pytest.fail(self.make_screenshot("Ошибка"))
