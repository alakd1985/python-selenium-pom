from pytest_bdd import given, when, then

from pages.medishop.login_page import MediShopLoginPage
from pages.medishop.home_page import MediShopHomePage


MEDISHOP_LOGIN_URL = (
    "https://www.way2automation.com/MediShopWebApp/login.html"
)


@given("the user is on the MediShop login page")
def user_is_on_medishop_login_page(driver):
    driver.get(MEDISHOP_LOGIN_URL)


@when("the user logs in with valid demo credentials")
def user_logs_in_with_valid_demo_credentials(driver):
    login_page = MediShopLoginPage(driver)

    assert login_page.login(
        email="trainer@way2automation.com",
        password="way2automation",
    ), "MediShop login failed"


@then("the MediShop home page should be displayed")
def medishop_home_page_should_be_displayed(driver):
    home_page = MediShopHomePage(driver)

    assert home_page.is_home_page_displayed(), (
        "MediShop home page was not displayed"
    )
