from locators.homepage import Homepage, Tariffs
from locators.tariff import MyConversation
import re
from selenium.webdriver.support import expected_conditions as EC


class HomepageHelper:

    def __init__(self, app):
        self.wd = app.wd
        self.app = app

    def open_searchpage(self):
        self.wd.find_element(*Homepage.search_button).click()

    def search_tariff(self, text):
        self.wd.find_element(*Homepage.search_query).send_keys(text)
        self.app.wait.until(EC.visibility_of_element_located(Tariffs.tariffs_list))

    def select_my_conversation_tariff(self):
        self.wd.find_element(*Tariffs.my_conversation).click()
        self.app.wait.until(EC.visibility_of_element_located(MyConversation.name))

    def get_current_url(self):
        current_url = self.wd.current_url
        return re.search(f'{self.app.base_url}(.*)', current_url).group(1)