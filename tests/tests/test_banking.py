from tests.pages.login_page import LoginPage


class TestBanking:

    def test_banking_operations(self, open_website_and_clear):
        page = LoginPage(open_website_and_clear)
        page.login()