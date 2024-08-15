import random
import time

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class BasePage:
    """
    Базовый класс для всех страниц.

    Этот класс предоставляет общие методы для взаимодействия с веб-элементами.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует объект BasePage с драйвером.

        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver

    def find_element(self, locator: tuple, timeout=10):
        """
        Находит один элемент на странице по указанным параметрам.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Найденный веб-элемент.
        """
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    def wait_for_body_to_load(self, timeout=10):
        """
        Ожидает, пока элемент <body> не станет полностью загруженным, проверяя также состояние загрузки страницы.

        :param timeout: Максимальное время ожидания в секундах.
        """
        time.sleep(2)
        wait = WebDriverWait(self.driver, timeout)

        # Ожидаем появления элемента <body>
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Ожидаем, пока страница не загрузится полностью
        wait.until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

    def find_and_click_element(self, locator: tuple, timeout=10):
        """
        Находит элемент по локатору, ждет его доступности и кликает по нему.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param timeout: Максимальное время ожидания в секундах.
        """
        self.wait_for_body_to_load(timeout)
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def scroll_to_element(self, locator: tuple, timeout=10):
        """
        Прокручивает страницу до элемента, чтобы он оказался в видимой области.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param timeout: Максимальное время ожидания в секундах.
        """
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located((by, value)))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element,
        )
        time.sleep(0.5)

    def get_current_url(self):
        """
        Возвращает текущий URL страницы.

        :return: Текущий URL.
        """
        return self.driver.current_url

    def switch_to_last_tab(self):
        """
        Переключение на последнюю открытую вкладку браузера.
        """
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    def assert_url_is_equal(self, expected_url: str):
        """
        Проверяет, что текущий URL соответствует ожидаемому.

        :param expected_url: Ожидаемый URL.
        :raises AssertionError: Если текущий URL не соответствует ожидаемому.
        """
        current_url = self.get_current_url()
        assert (
            expected_url == current_url
        ), f"Ожидали url {expected_url}, получили {current_url}"

    def find_and_send(self, locator: tuple, key: str, timeout=10):
        """
        Находит элемент по локатору и отправляет в него текст.

        :param locator: Кортеж, содержащий способ поиска элемента и значение для поиска.
        :param key: Текст для отправки в элемент.
        :param timeout: Максимальное время ожидания в секундах.
        """
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located((by, value)))
        element.send_keys(key)

    def wait_for_element(self, locator, timeout=10):
        """
        Ожидание загрузки элемента на странице.

        :param driver: Экземпляр WebDriver.
        :param locator: Кортеж, содержащий стратегию поиска (например, By.ID) и значение поиска (например, 'element_id').
        :param timeout: Максимальное время ожидания в секундах. По умолчанию 10 секунд.
        :return: Найденный элемент.
        :raises TimeoutException: Если элемент не найден в течение времени ожидания.
        """
        time.sleep(1)
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def generate_first_name(self):
        fake = Faker("ru_RU")
        first_name = fake.first_name_male()
        return first_name

    def generate_email(self):
        fake = Faker()
        return fake.email()

    def generate_password(self):
        fake = Faker()
        # Генерация 8 случайных цифр
        digits = "".join([str(random.randint(0, 9)) for _ in range(8)])
        # Генерация одной строчной и одной заглавной буквы
        lowercase_letter = fake.random_lowercase_letter()
        uppercase_letter = fake.random_uppercase_letter()
        # Специальный символ
        special_char = "!"
        # Формирование пароля
        password = digits + lowercase_letter + uppercase_letter + special_char
        # Перемешиваем символы в пароле для большей случайности
        password = "".join(random.sample(password, len(password)))
        return password

    def make_screenshot(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )