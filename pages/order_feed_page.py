import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.common.exceptions import TimeoutException

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    @allure.step("Открытие ленты заказов")
    def open(self):
        return self.open_page("feed")

    @allure.step("Ожидание прогрузки ленты заказов")
    def wait_for_page_loaded(self):
        self.wait.wait_for_page_load()
        assert self.is_visible(self.locators.ORDER_FEED_TEXT), "Лента заказов не загрузилась"
        return True

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                element = self.find_element(self.locators.TODAY_ORDERS)
                return int(element.text.replace(',', ''))
            except TimeoutException:
                if attempt == max_attempts - 1:
                    raise TimeoutException(f"Элемент {self.locators.TODAY_ORDERS} не найден после {max_attempts} попыток поиска.")
                continue

    @allure.step("Получить список заказов, которые находятся в работе")
    def get_orders_in_progress(self):

        for attempt in range(3):
            elements = self.find_elements(self.locators.ORDERS_IN_PROGRESS, timeout=5)
            texts = [el.text for el in elements]
            if any(order_text.strip() != "Все текущие заказы готовы!" for order_text in texts):
                return texts
            if attempt < 2:
                return texts

    @allure.step("Получить все количество заказов")
    def get_total_orders_count(self):
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                element = self.find_element(self.locators.TOTAL_ORDERS)
                return int(element.text.replace(',', ''))
            except TimeoutException:
                if attempt == max_attempts - 1:
                    raise TimeoutException(f"Элемент {self.locators.TOTAL_ORDERS} не найден после {max_attempts} попыток поиска.")
                continue


