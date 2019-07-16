from selenium.webdriver.common.by import By


class Homepage:

    search_button = (By.XPATH, '//span[contains(text(), "Поиск")]')
    search_query = (By.XPATH, '//div[@id="globalSearch"]//input[@placeholder]')


class Tariffs:

    tariffs_list = (By.XPATH, "//div[@class='recently-tariffs']")
    my_conversation = (By.XPATH, '//a[@href="/tariff/my-conversation"]')