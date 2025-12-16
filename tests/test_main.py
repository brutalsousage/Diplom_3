import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_modal_page import OrderModalPage

@allure.feature("Главная страница")
class TestMain:

    @allure.title('Переход на "Конструктор"')
    def test_constructor_menu(self, browser):
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.open()
            main_page.wait_for_main_page_loaded()

        with allure.step("Сделать переход на ленту заказов"):
            main_page.click_order_feed()
            assert "feed" in order_feed_page.get_current_url()
            assert main_page.is_order_feed_active()

        with allure.step("Сделать переход на конструктор"):
            main_page.click_constructor()
            assert main_page.is_constructor_active()
            assert main_page.is_main_page_loaded()

    @allure.title("'Переход на ленту заказов")
    def test_order_feed_navigation(self, browser):
        main_page = MainPage(browser)
        order_feed_page = OrderFeedPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.open()
            main_page.wait_for_main_page_loaded()

        with allure.step("Сделать переход на ленту заказов"):
            main_page.click_order_feed()

        with allure.step("Проверить полученный URL"):
            assert "feed" in order_feed_page.get_current_url()

    @allure.title("Проверка модального окна с деталями для ингредиента")
    def test_ingredient_modal_opening(self, browser):
        main_page = MainPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.open()
            main_page.wait_for_main_page_loaded()

        with allure.step("Нажать на ингредиент"):
            main_page.click_ingredient(0)

        with allure.step("Модальное окно появилось?"):
            assert main_page.is_ingredient_modal_visible()

    @allure.title("Проверка закрытия модального окна с деталями для ингредиента")
    def test_ingredient_modal_closing(self, browser):
        main_page = MainPage(browser)
        order_modal = OrderModalPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.open()
            main_page.wait_for_main_page_loaded()

        with allure.step("Открыть модальное окно с ингредиентом"):
            main_page.click_ingredient(0)
            assert main_page.is_ingredient_modal_visible()

        with allure.step("Закрыть модальное окно"):
            assert order_modal.close_modal()

        with allure.step("Проверить закрылось ли модальное окно"):
            assert not main_page.is_ingredient_modal_visible()

    @allure.title("Счетчик ингредиента повышается при добавлении")
    def test_ingredient_counter_plus(self, main_page):
        with allure.step("Ждем полной загрузки главной страницы"):
            main_page.wait_for_main_page_loaded()
        
        with allure.step("Начальное значение счетчика ингредиента"):
            initial_counter = main_page.get_ingredient_counter(0)
        
        with allure.step("Добавить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor(0)
        
        with allure.step("Проверить повышение счетчика"):
            new_counter = main_page.get_ingredient_counter(0)
            assert new_counter > initial_counter