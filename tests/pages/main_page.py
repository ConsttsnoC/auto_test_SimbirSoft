import allure
import pytest
from loguru import logger

from tests.pages.base_page import BasePage
from tests.pages.locators import Locators
from utils.fibonacci import get_fibonacci_for_today


class MainPage(BasePage):
    deposit_amount = get_fibonacci_for_today()
    deposit_amount_str = str(deposit_amount)
    def login(self):
        try:
            logger.info("Начало процесса авторизации")
            with allure.step("Нажатие на кнопку 'Клиент'"):
                self.find_and_click_element(Locators.LOGIN_BUTTON)
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
            logger.info("Процесс входа завершён успешно.")
        except Exception as e:
            logger.error(f"Произошла ошибка: {e}")
            allure.attach(
                f"Ошибка: {e}",
                name="Ошибка входа",
                attachment_type=allure.attachment_type.TEXT,
            )
            pytest.fail(self.make_screenshot("Ошибка"))

    def logout(self):
        try:
            with allure.step("Разлогиниваемся"):
                self.find_and_click_element(Locators.LOGOUT_BUTTON)
                logger.info("Выход из профиля успешен.")
            logger.info("Процесс входа завершён успешно.")
        except Exception as e:
            logger.error(f"Произошла ошибка: {e}")
            allure.attach(
                f"Ошибка: {e}",
                name="Ошибка входа",
                attachment_type=allure.attachment_type.TEXT,
            )
            pytest.fail(self.make_screenshot("Ошибка"))

    def making_deposit(self):
        try:
            with allure.step("Нажатие на вкладку 'Deposit'"):
                self.find_and_click_element(Locators.DEPOSIT_BUTTON)
                logger.info("Вкладка 'Deposit' нажата.")

            with allure.step(f"Установка суммы депозита: {self.deposit_amount_str}"):
                self.find_and_send(Locators.DEPOSIT_AND_WITHDRAW_INPUT, self.deposit_amount_str)
                logger.info(f"Сумма депозита установлена: {self.deposit_amount_str}.")

            with allure.step("Нажатие на кнопку 'Deposit' для подтверждения депозита"):
                self.find_and_click_element(Locators.DEPOSIT_OK_BUTTON)
                logger.info("Кнопка 'Deposit' для подтверждения депозита нажата.")

            logger.info("Процесс внесения депозита завершён успешно.")
        except Exception as e:
            logger.error(f"Произошла ошибка, при процессе внесения депозита: {e}")
            allure.attach(
                f"Ошибка: {e}",
                name="Ошибка процесса внесения депозита",
                attachment_type=allure.attachment_type.TEXT,
            )
            pytest.fail(self.make_screenshot("Ошибка процесса внесения депозита"))

    def withdrawal_of_deposit(self):
        try:
            with allure.step("Нажатие на вкладку 'Withdrawl' для переключения на списания."):
                self.find_and_click_element(Locators.WRITTEN_FROM_ACCOUNT)
                logger.info("Вкладка 'Withdrawl' нажата.")

            self.wait_for_body_to_load()

            with allure.step(f"Установка суммы снятия депозита: {self.deposit_amount_str}"):
                self.find_and_send(Locators.DEPOSIT_AND_WITHDRAW_INPUT, self.deposit_amount_str)
                logger.info(f"Сумма снятия депозита установлена: {self.deposit_amount_str}.")

            with allure.step(
                    "Нажатие на кнопку 'Withdraw' для подтверждения снятия депозита"
            ):
                self.find_and_click_element(Locators.WITHDRAW_CONFIRM_BUTTON)
                logger.info(
                    "Кнопка 'Withdraw' для подтверждения снятия депозита нажата."
                )
            logger.info("Процесс списания депозита завершён успешно.")
        except Exception as e:
            logger.error(f"Произошла ошибка, при процессе списания депозита: {e}")
            allure.attach(
                f"Ошибка процесса списания депозита: {e}",
                name="Ошибка процесса списания депозита",
                attachment_type=allure.attachment_type.TEXT,
            )
            pytest.fail(self.make_screenshot("Ошибка процесса списания депозита"))

    def check_for_balance_zero(self):
        try:
            with allure.step("Проверка, что баланс равен 0 после снятия депозита."):
                balance_element = self.find_element(Locators.LOCATOR_BALANCE)
                balance_value = int(balance_element.text.strip())
                assert (
                    balance_value == 0
                ), f"Баланс не равен 0. Текущий баланс: {balance_value}"
                logger.info(f"Баланс успешно проверен и равен {balance_value}.")
        except AssertionError as e:
            logger.error(f"Ошибка проверки баланса: {e}")
            pytest.fail(f"Ошибка проверки баланса: {e}")
