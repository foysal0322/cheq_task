
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
class HomePageLocators(object):

    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BTN = (By.XPATH, '//button[text()="LOG IN"]')
    # DATE_BTN = (By.XPATH, f'//button[text()="{date}"]')
    CONTINUE_BTN = (By.XPATH, '//button[text()="CONTINUE"]')
    SUITE_CONTINUE_BTN = (By.XPATH, '//button[text()="Continue"]')
    CREATE_NEW_ORDER = (By.XPATH, '//span[text()="Create new order"]')
    SAVE_BTN = (By.XPATH, '//button[text()="Save"]')
    ADD_TO_ORDER_BTN = (By.XPATH, '//button[text()="+ Add to order"]')
    TAB_LIST = (By.XPATH, '//*[@role="tablist"]//a[@role="tab"]') # get all category list including id
    VIEW_CART = (By.XPATH, '//span[text()="View Cart"]')
    ORDER_TOTAL = (By.XPATH, "//span[text()='Order Total']/ancestor::li//div[contains(@class, 'MuiListItemSecondaryAction-root')]")
    SAVE_PRE_ORDER = (By.XPATH, '//button[text()="Save  Pre-Order"]')
    CREDIT_CARD = (By.XPATH, '//span[text()="Credit Card"]')

#     locators credit card
    IFRAME_CARD_NUMBER = (By.XPATH, "//iframe[@title='Iframe for secured card number']")
    CARD_NUMBER = (By.XPATH, '//input[@aria-label="Card number"]')
    IFRAME_EXP_DATE = (By.XPATH, "//iframe[@title='Iframe for secured card expiry date']")
    EXP_DATE = (By.XPATH, '//input[@aria-label="Expiry date"]')
    IFRAME_CVV = (By.XPATH, "//iframe[@title='Iframe for secured card security code']")
    CVV = (By.XPATH,'//input[@aria-label="Security code"]')
    NAME_ON_CARD = (By.NAME,'holderName')
    VERIFY_SUBTOTAL_BTN = (By.XPATH,"//span[contains(text(),'Verify subtotal')]")

#     Profile
    ACCOUNT_BTN = (By.XPATH, '//button[text()="Account"]')
    LOGOUT_BTN = (By.XPATH, '//button[text()="Log Out"]')










