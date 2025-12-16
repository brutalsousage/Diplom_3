# conftest.py
import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from help.data import Data
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_modal_page import OrderModalPage
from pages.order_feed_page import OrderFeedPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Choose browser: chrome or firefox"
    )
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        #options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        options = webdriver.ChromeOptions()
        #ptions.add_argument("--headless")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    
    yield driver
    driver.quit()

@pytest.fixture
def main_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.wait_for_main_page_loaded()
    return main_page

@pytest.fixture
def authenticated_user(browser):

    main_page = MainPage(browser)
    login_page = LoginPage(browser)
    test_email = Data.get_test_user_email()
    test_password = Data.get_test_user_password()
    main_page.open()
    main_page.wait_for_main_page_loaded()
    main_page.click_personal_account()
    login_page.enter_email(test_email)
    login_page.enter_password(test_password)
    login_page.click_login_button()
    main_page.changing_the_authorization_page()
    return main_page

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture
def order_feed_page(browser):
    return OrderFeedPage(browser)

@pytest.fixture
def order_modal(browser):
    return OrderModalPage(browser)





