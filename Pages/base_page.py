from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver, base_url='https://suites.uat.cheqplease.com/'):
        self.base_url = base_url
        self.driver = driver
        # self.driver.implicitly_wait(5)
        self.timeout = 10

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0,0)")

    # def read_excel(file_name, sheet_name):
    #     df = pd.read_excel(f"{file_name}", sheet_name=f'{sheet_name}', engine="openpyxl")
    #     return df
