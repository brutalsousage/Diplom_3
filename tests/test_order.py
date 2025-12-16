import pytest
import allure


@allure.feature("Заказы")
class TestOrderFeed:
    
    @allure.title("Счетчик 'Выполнено за всё время' увеличивается при новом заказе")
    def test_total_orders_counter_plus(self, order_feed_page, authenticated_user, main_page):
        authenticated_user
        
        with allure.step("Информация об общем счетчике заказов"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            initial_total = order_feed_page.get_total_orders_count()
            
        with allure.step("Генерация нового заказа"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.create_test_order()
            main_page.wait.wait_for_element_visible(main_page.locators.ORDER_MODAL)
            
        with allure.step("Переход на ленту заказов и сравнение счетчика"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            order_feed_page.wait.wait_for_page_load()
            new_total = order_feed_page.get_total_orders_count()       
            
            assert new_total > initial_total

    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается при новом заказе")
    def test_today_orders_counter_plus(self, order_feed_page, authenticated_user, main_page):
        with allure.step("Информация о сегодняшнем счетчике заказов"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            initial_today = order_feed_page.get_today_orders_count()

        with allure.step("Генерация нового заказа"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.create_test_order()
            main_page.wait.wait_for_element_visible(main_page.locators.ORDER_MODAL)
            main_page.wait.wait_for_element_visible(main_page.locators.IDENTIFICATOR_ORDER_TEXT)
        
        with allure.step("Переход на ленту заказов и сравнение счетчика"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            order_feed_page.wait.wait_for_page_load()
            new_today = order_feed_page.get_today_orders_count()
            assert new_today > initial_today

    @allure.title("Номера заказа отображается в разделе 'В работе'")
    def test_appears_order_progress_table(self, order_feed_page, authenticated_user, main_page, order_modal):
        with allure.step("Генерация нового заказа и получение номера"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.create_test_order()
            main_page.wait.wait_for_element_visible(main_page.locators.ORDER_MODAL)
            order_modal.button_close_modal_activity()
            order_modal.wait_close_modal_overlay()
            order_number = order_modal.get_order_number()
            assert order_number is not None
            order_modal.close_modal()

        with allure.step("Переход на ленту заказов"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            order_feed_page.wait.wait_for_page_load()

        with allure.step("Наш заказ отображается в разделе 'В работе'"):
            orders_in_progress = order_feed_page.get_orders_in_progress()
            assert any(order_number in order_text for order_text in orders_in_progress)