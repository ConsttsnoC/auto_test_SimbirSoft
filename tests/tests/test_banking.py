import allure
from tests.pages.banking_page import BankingPage


class TestBanking:

    @allure.title("Тест login/logout, выбор пользователя, проведения транзакций, сохранение отчета в CSV файле")
    def test_banking_operations(self, open_website_and_clear):
        page = BankingPage(open_website_and_clear)
        page.authorize_and_manage_deposit()
