import allure
import logging
from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OrderModalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Закрытие модального окна")
    def _close_by_close_button(self):
        try:
            if self.is_visible(OrderModalLocators.MODAL_CLOSE):
                self.wait.wait_for_element_clickable(OrderModalLocators.MODAL_CLOSE)
                button_close = self.find_element(OrderModalLocators.MODAL_CLOSE)
                self.execute_script("arguments[0].click();", button_close)
            self.wait_for_element_invisible(OrderModalLocators.MODAL, timeout=None)
            return True
        except Exception as e:
            logger.error(f"Ошибка при закрытии модалки: {e}")
            return False
        return False
    
    @allure.step("Проверка видимости модального окна")
    def is_modal_visible(self):
        return self.is_visible(OrderModalLocators.MODAL)
    
    @allure.step("Вывести номер заказа")
    def get_order_number(self):
        try:
            order_number_element = self.find_element(OrderModalLocators.ORDER_NUMBER, timeout=10)
            order_number = '0' + order_number_element.text
            return order_number if order_number and order_number != '0' else None 
        except:
            return None
        
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        return self._close_by_close_button()
       
    @allure.step("Вывести название ингредиента")
    def get_ingredient_name(self):
        try:
            ingredient_name_element = self.find_element(OrderModalLocators.INGREDIENT_NAME, timeout=10)
            return ingredient_name_element.text
        except:
            return None
        
    @allure.step("Ожидание пока крестик в модале будет кликабелен")
    def button_close_modal_activity(self):
        self.is_visible(OrderModalLocators.MODAL_TICK_ANIMATION)
        self.wait.wait_for_element_clickable(OrderModalLocators.MODAL_TICK_ANIMATION)

    @allure.step("Ожидание исчезновения модал оверлея")
    def wait_close_modal_overlay(self):
        self.wait_for_element_invisible(OrderModalLocators.MODAL_OVERLAY, timeout=5)

