import csv
import os
import allure
import pytest
from loguru import logger
from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
from tests.pages.locators import Locators


class HelpCsv(BasePage):
    TRANSACTION_FILE_PATH = os.path.join("test_data", "transactions.csv")

    @allure.step("Получение всех записей из таблицы транзакций.")
    def get_table_records(self):
        """
        Получение всех записей из таблицы транзакций.
        """
        try:
            logger.info("Начало поиска таблицы с записями транзакций.")
            table_element = self.find_element(Locators.TABLE_ELEMENTS)
            logger.info("Таблица с записями транзакций найдена успешно.")

            logger.info("Начало поиска строк в таблице.")
            rows = table_element.find_elements(By.CSS_SELECTOR, "tr")
            logger.info(f"Количество найденных строк: {len(rows)}.")

            logger.info("Извлечение текста из каждой строки таблицы.")
            records = []
            for index, row in enumerate(rows):
                record = row.text.strip()
                if record:
                    records.append(record)
                    logger.info(f"Запись номер {index + 1} получена: {record}")
                else:
                    logger.warning(f"Строка номер {index + 1} пуста.")

            logger.info("Извлечение всех записей завершено успешно.")
            return records

        except Exception as e:
            logger.error(f"Ошибка при извлечении записей из таблицы: {e}")
            pytest.fail(self.make_screenshot("Ошибка"))

    @allure.step("Сохранение данных о проведенных транзакциях в файл CSV.")
    def save_transactions_to_csv(self):
        """
        Сохранение данных о проведенных транзакциях в файл CSV.
        """
        try:
            logger.info("Начинаем процесс сохранения транзакций в CSV файл...")
            records = self.get_table_records()
            if len(records) < 2:
                logger.warning(
                    "Записей для сохранения недостаточно. Возможно, таблица пуста."
                )
                return

            formatted_records = []
            logger.info(
                "Обрабатываем каждую запись таблицы, начиная со второй строки (пропуская заголовок)."
            )
            for index, record in enumerate(records[1:], start=2):
                parts = record.split()

                if len(parts) < 6:
                    logger.warning(
                        f"Запись номер {index} имеет недостаточное количество элементов: {record}"
                    )
                    continue
                logger.info(
                    "Извлекаем данные: день, месяц, год, время, сумму и тип транзакции."
                )
                day = parts[1]
                month = parts[0]
                year = parts[2]
                time = parts[3]
                amount = int(parts[5])
                transaction_type = parts[6]
                logger.info("Формируем строку с датой, временем и типом транзакции")
                original_datetime_str = f"{day}.{month}.{year} {time}"
                logger.info(
                    "Добавляем запись в форматированном виде, убирая лишние символы"
                )
                formatted_records.append(
                    [
                        original_datetime_str.replace('"', "").replace(",", ""),
                        amount,
                        transaction_type,
                    ]
                )
                logger.info(
                    f"Запись номер {index} добавлена в список для сохранения: {original_datetime_str}, {amount}, "
                    f"{transaction_type}"
                )

            logger.info("Записываем данные в CSV файл")
            with open(
                self.TRANSACTION_FILE_PATH, mode="w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.writer(file)
                writer.writerow(["Дата и Время Транзакции", "Сумма", "Тип Транзакции"])
                writer.writerows(formatted_records)
                logger.info(
                    f"Транзакции успешно сохранены в файл {self.TRANSACTION_FILE_PATH}"
                )

            allure.attach.file(
                self.TRANSACTION_FILE_PATH,
                name="Транзакции",
                attachment_type=allure.attachment_type.CSV,
            )
        except Exception as e:
            logger.error(f"Ошибка при сохранении транзакций в файл CSV: {e}")
            pytest.fail(self.make_screenshot("Ошибка"))
