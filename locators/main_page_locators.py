from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    CONSTRUCTOR_ACTIVE = (By.XPATH, "//a[.//p[text()='Конструктор'] and contains(@class, 'active')]")
    ORDER_FEED_ACTIVE = (By.XPATH, "//a[.//p[text()='Лента Заказов'] and contains(@class, 'active')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    IDENTIFICATOR_ORDER_TEXT = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and contains(@class, 'mb-15') and text()='идентификатор заказа']")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_default')]/p[contains(@class, 'counter_counter__num')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
