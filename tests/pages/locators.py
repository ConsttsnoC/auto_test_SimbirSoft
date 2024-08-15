from selenium.webdriver.common.by import By

class Locators:
    # Локаторы для страницы входа
    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
    SELECT_USER_NAME = (By.ID, 'userSelect')
    ELEMENT_HARRY_POTTER = (By.XPATH, '//*[@id="userSelect"]/option[3]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > form > button')

    # Локаторы для депозита
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
    DEPOSIT_INPUT_FIELD = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    DEPOSIT_OK_BUTTON = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
    WRITTEN_FROM_ACCOUNT = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)')
    INPUT_WITHDRAW_AMOUNT = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    WITHDRAW_CONFIRM_BUTTON = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
    LOCATOR_BALANCE = (By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)')
