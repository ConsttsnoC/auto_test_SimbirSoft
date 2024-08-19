import allure
from tests.pages.banking_page import BankingPage


class TestBanking:

    @allure.title(
        "Тест login/logout, проведения транзакций, сохранение отчета в CSV файле"
    )
    def test_banking_operations(self, login_logout):
        page = BankingPage(login_logout)
        page.authorize_and_manage_deposit()
