from selenium.webdriver.common.by import By


class MyConversation:

    price = (By.XPATH, "//span[@class='price']/span")
    name = (By.XPATH, "//div[@class='tariff-card-new__heading']//span[contains(text(), 'Мой разговор')]")