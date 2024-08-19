import allure
import pytest
from loguru import logger
from tests.pages.base_page import BasePage
from tests.pages.locators import Locators


class MainPage(BasePage):

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
