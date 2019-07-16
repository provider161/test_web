from locators.tariff import MyConversation


class TariffHelper:

    def __init__(self, app):
        self.wd = app.wd
        self.app = app

    def get_tariff_price(self):
        price = self.wd.find_element(*MyConversation.price).text
        return int(price)