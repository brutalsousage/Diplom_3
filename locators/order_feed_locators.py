from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_FEED_TEXT = (By.XPATH, '//*[@class="text text_type_main-large mt-10 mb-5" and text()="Лента заказов"]')
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList__cBvyi') and contains(@class, 'OrderFeed_orderList')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'digits-default')]")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'digits-large')]")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'digits-large')]")
    IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and normalize-space(text()) = 'В работе:']")
