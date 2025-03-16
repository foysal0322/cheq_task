import time
import re
import pandas as pd
import allure
import traceback
import pytest
from Pages.base_page import BasePage
from utils.locators import *
from selenium.webdriver.common.keys import Keys
from utils.locators import HomePageLocators
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators

    def login(self, email, password):
        self.driver.find_element(*self.locator.EMAIL).send_keys(email)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)
        self.driver.find_element(*self.locator.LOGIN_BTN).click()

    def select_Date_Event(self, date,event):
        '''this function will select given date and event from the calander and return nothing.'''
        self.driver.find_element(By.XPATH, f'//button[text()="{date}"]').click()
        self.scroll_down()
        self.driver.find_element(By.XPATH, f'//span[text()="{event}"]').click()
        self.driver.find_element(*self.locator.CONTINUE_BTN).click()

    def select_suite(self,suite):
        ''' this function will select given suite return nothing.'''
        self.driver.find_element(By.XPATH, f'//span[text()="{suite}"]').click()
        self.driver.find_element(*self.locator.SUITE_CONTINUE_BTN).click()
        try:
            # self.driver.find_element(*self.locator.CREATE_NEW_ORDER).click() # to handle warning Continue button
            self.driver.find_elements(*self.locator.SUITE_CONTINUE_BTN)[1].click() # to handle warning Continue button
        except:
            pass

    def select_suite_preference(self):
        '''this function will select default suite preference and return nothing.'''

        self.driver.find_element(*self.locator.SAVE_BTN).click()

    def add_item(self):
        import re
        '''this function will Add 1 item from each category to the cart and click on View Cart.
        and return nothing.'''

        # get all category id
        cat_id = []
        categories = self.driver.find_elements(*self.locator.TAB_LIST)
        for id in categories:
            cID = re.search(r'category-(\d+)', id.get_attribute('href')).group(1)
            cat_id.append(cID)

        # add i iterm from each category according to category id

        for id in cat_id:
            item = self.driver.find_element(By.XPATH, f'//*[@id="category-{id}"]//a')
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", item)
            time.sleep(2)
            item.click()
            self.driver.find_element(*self.locator.ADD_TO_ORDER_BTN).click()
            time.sleep(2)

    def submit_preorder(self):
        '''this function will make a preorder and return order total.'''
        self.driver.find_element(*self.locator.VIEW_CART).click()
        order_total = self.driver.find_element(*self.locator.ORDER_TOTAL).text # extracting order total before preorder
        order_total = re.sub(r'[^\d.]', '', order_total)
        self.driver.find_element(*self.locator.SAVE_PRE_ORDER).click()

        return order_total

    def select_credit_card(self):
        '''this function will select credit card as payment method return nothing.'''
        self.driver.find_element(*self.locator.CREDIT_CARD).click()

    def enter_credit_card_details(self,card_no,exp_date,cvv,card_holder_name):
        '''this function will select credit card as payment method return nothing.'''
        self.driver.switch_to.frame(self.driver.find_element(*self.locator.IFRAME_CARD_NUMBER))
        self.driver.find_element(*self.locator.CARD_NUMBER).send_keys(card_no)
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_element(*self.locator.IFRAME_EXP_DATE))
        self.driver.find_element(*self.locator.EXP_DATE).send_keys(exp_date)
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_element(*self.locator.IFRAME_CVV))
        self.driver.find_element(*self.locator.CVV).send_keys(cvv)
        self.driver.switch_to.default_content()

        self.driver.find_element(*self.locator.NAME_ON_CARD).send_keys(card_holder_name)
        text = self.driver.find_element(*self.locator.VERIFY_SUBTOTAL_BTN).text # extracting total amount from subtotal button
        total = text.split("$")[-1]
        self.driver.find_element(*self.locator.VERIFY_SUBTOTAL_BTN).click()
        return total

    def read_excel(self,file_name,sheet_name):
        '''this function will read a excell file and return dataframe along with the sheet data'''

        df = pd.read_excel(f"{file_name}",sheet_name=f'{sheet_name}',engine="openpyxl")
        return df

    @allure.step("Capturing screenshot")
    def take_screenshot(self, name="screenshot"):
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

    @allure.step("Adding custom logs")
    def log_info(self,logs):
        allure.attach(traceback.format_exc(), name="Selenium Error Traceback", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to exception: {logs}")