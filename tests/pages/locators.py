from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    SELECT_USER_NAME = (By.ID, "userSelect")
    ELEMENT_HARRY_POTTER = (By.XPATH, '//*[@id="userSelect"]/option[3]')
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "[ng-class='btnClass2']")
    DEPOSIT_AND_WITHDRAW_INPUT = (By.CSS_SELECTOR, "input[ng-model='amount']")
    DEPOSIT_OK_BUTTON = (By.XPATH, "//button[text()='Deposit']")
    WRITTEN_FROM_ACCOUNT = (By.CSS_SELECTOR, "[ng-class='btnClass3']")
    WITHDRAW_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Withdraw']")
    LOCATOR_BALANCE = (By.XPATH, "//strong[@class='ng-binding'][2]")
    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, "[ng-class='btnClass1']")
    TABLE_ELEMENTS = LOCATOR_TABLE = (By.TAG_NAME, "table")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button[ng-show='logout']")

