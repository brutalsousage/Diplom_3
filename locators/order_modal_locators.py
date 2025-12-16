from selenium.webdriver.common.by import By

class OrderModalLocators:
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_TICK_ANIMATION = (By.XPATH, "//div[@class='undefined mb-15']//img[@alt='tick animation']")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_NAME = (By.XPATH, "//h2[text()='Детали ингредиента']/following-sibling::p[contains(@class, 'text')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]")
