
import allure
import inspect
import pytest
from Pages.home_page import HomePage
from TestConf.config import *
from TestConf.send_report import *

from selenium.webdriver.common.by import By


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sanity
@pytest.mark.parallel
class Test_001(BaseTest):
    @pytest.mark.regression
    def test_login(self, setUp):
        '''this test case will login with given credentials'''
        try:

            home_page = HomePage(driver=self.driver)
            home_page.open('')
            # read data from excel
            credentials = home_page.read_excel("C:/Users/Foysal/Desktop/cheq_task/utils/info.xlsx","Login credentials")
            home_page.login(credentials['Email'][0],credentials['Password'][0])
            self.driver.find_element(By.XPATH,'//button[text()="Account"]').click()
            assert  self.driver.find_element(By.XPATH,'//button[text()="Log Out"]').is_displayed(),"Element is not visible"

            send_discord_notification(f'{inspect.currentframe().f_code.co_name} executed')
        except Exception as e:
            home_page.take_screenshot()
            home_page.log_info(e)
            send_discord_notification(f'{inspect.currentframe().f_code.co_name} failed, Here is the logs: {e}')

    @pytest.mark.negative
    def test_negative(self, setUp):
        '''this test case will login with wromg credentials'''
        try:
            home_page = HomePage(driver=self.driver)
            home_page.open('')
            # read data from excel
            credentials = home_page.read_excel("C:/Users/Foysal/Desktop/cheq_task/utils/info.xlsx","Login credentials")
            home_page.login(credentials['Email'][1],credentials['Password'][1])
            self.driver.find_element(By.XPATH,"//*[contains(text(),'Invalid Username or Password')]").is_displayed(),"Element is not visible"

            send_discord_notification(f'{inspect.currentframe().f_code.co_name} executed')
        except Exception as e:
            home_page.take_screenshot()
            home_page.log_info(e)
            send_discord_notification(f'{inspect.currentframe().f_code.co_name} failed, Here is the logs: {e}')


    @pytest.mark.e2e
    def test_end_to_end(self, setUp):
        ''' this test case will book a suite and make a pre order ith given data'''
        try:
            # cancel all available new orders before creating new preorder
            cancelOrder = CancelOrders()
            cancelOrder.cancel_new_orders()

            home_page = HomePage(driver=self.driver)
            home_page.open('')
            # read data from excel
            credentials = home_page.read_excel("C:/Users/Foysal/Desktop/cheq_task/utils/info.xlsx","Login credentials")
            event_details = home_page.read_excel("C:/Users/Foysal/Desktop/cheq_task/utils/info.xlsx","Event details")
            card_details = home_page.read_excel("C:/Users/Foysal/Desktop/cheq_task/utils/info.xlsx","Card details")

            home_page.login(credentials['Email'][0],credentials['Password'][0])
            home_page.select_Date_Event(event_details['Date'][0],event_details['Event name'][0])
            home_page.select_suite(event_details['Suite name'][0])
            home_page.select_suite_preference()
            home_page.add_item()
            total_before_preorder = home_page.submit_preorder()
            home_page.select_credit_card()
            total_after_preorder = home_page.enter_credit_card_details(card_details['Card no'][0],str(card_details['Exp_Date'][0]),card_details['CVC/CVV'][0],card_details['Name On Card'][0])
            assert str(total_before_preorder) == str(total_after_preorder)

            send_discord_notification(f'{inspect.currentframe().f_code.co_name} executed')

        except Exception as e:
            home_page.take_screenshot()
            home_page.log_info(e)
            send_discord_notification(f'{inspect.currentframe().f_code.co_name} failed, Here is the logs: {e}')

