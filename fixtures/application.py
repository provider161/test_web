from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from helpers.homepage import HomepageHelper
from helpers.tariff import TariffHelper


class Application:

    def __init__(self, base_url):
        options = webdriver.ChromeOptions()
        options.add_argument('no-sandbox')
        options.add_argument('window-size=1920,1080')
        self.wd = webdriver.Chrome(options=options)
        self.wd.maximize_window()
        self.wd.delete_all_cookies()
        self.wd.implicitly_wait(60)
        self.wait = WebDriverWait(self.wd, 60)
        self.homepage = HomepageHelper(self)
        self.tariff = TariffHelper(self)
        self.base_url = base_url

    def open_homepage(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
