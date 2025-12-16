import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_modal_locators import OrderModalLocators
from selenium.webdriver import ActionChains


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Нажатие на Конструктор")
    def click_constructor(self):
        self.click(self.locators.CONSTRUCTOR_BUTTON)
        return self

    @allure.step("Нажатие на Лента Заказов")
    def click_order_feed(self):
        self.click(self.locators.ORDER_FEED_BUTTON)
        return self.wait_for_page_loaded()

    @allure.step("Нажатие на Личный Кабинет")
    def click_personal_account(self):
        self.click(self.locators.PERSONAL_ACCOUNT_BUTTON)
        return self.wait_for_page_loaded()

    @allure.step("Открытие главной страницу")
    def open(self):
        return self.open_page("main")

    def wait_for_element_not_visible(self, locator, timeout=None, message=""):
        return self.wait_for_element_invisible(locator, timeout, message)   

    @allure.step("Ожидание прогрузки главной страницы")
    def wait_for_main_page_loaded(self):
        self.wait.wait_for_page_load()
        assert self.wait.wait_for_element_present(self.locators.CONSTRUCTOR_BUTTON, timeout=10)

    @allure.step("Ожидание прогрузки страницы")
    def wait_for_page_loaded(self):
        self.wait.wait_for_page_load()
        return self

    @allure.step("Получить номер созданного заказа из модального окна")
    def get_created_order_number(self):
        try:
            order_number_element = self.find_element(OrderModalLocators.ORDER_NUMBER, timeout=10)
            return order_number_element.text
        except:
            return None

    @allure.step("Проверить прогрузку главной страницы")
    def is_main_page_loaded(self):
        return self.is_visible(self.locators.PAGE_TITLE)

    @allure.step("Проверить авторизацию в системе")
    def changing_the_authorization_page(self):
        self.click(self.locators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_and_assert_url_contains("/account/profile")

    @allure.step("Активность ленты заказов")
    def is_order_feed_active(self):
        return self.is_present(self.locators.ORDER_FEED_ACTIVE)

    @allure.step("Нажать Оформить заказ")
    def click_make_order(self):
        self.wait.wait_for_element_visible(self.locators.ORDER_BUTTON)
        self.wait.wait_for_element_clickable(self.locators.ORDER_BUTTON)
        self.click(self.locators.ORDER_BUTTON)
        return self

    @allure.step("Активность конструктора")
    def is_constructor_active(self):
        return self.is_present(self.locators.CONSTRUCTOR_ACTIVE)

    @allure.step("Создаем тест заказ")
    def create_test_order(self):
        self.add_ingredient_to_constructor(0)
        self.add_ingredient_to_constructor(5)
        self.add_ingredient_to_constructor(10)
        result = self.click_make_order()
        return result

    @allure.step("Нажать на ингредиент с индексом {index}")
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.execute_script("arguments[0].scrollIntoView(true);", ingredients[index])
            ingredients[index].click()
            self.wait.wait_for_element_visible(OrderModalLocators.INGREDIENT_DETAILS)
        return self

    @allure.step("Получить счетчик ингредиента по индексу {index}")
    def get_ingredient_counter(self, index):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            try:
                counter_element = ingredients[index].find_element(*self.locators.INGREDIENT_COUNTER)
                return int(counter_element.text)
            except:
                return 0
        return 0

    @allure.step("Перетащить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, index):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            ingredient = ingredients[index]
            constructor_area = self.find_element(self.locators.CONSTRUCTOR_AREA)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(ingredient, constructor_area).perform()
        return self
    
    def is_ingredient_modal_visible(self, timeout=5):
        try:
            self.wait.wait_for_element_visible(self.locators.ORDER_MODAL)
            return True
        except Exception:
            return False   