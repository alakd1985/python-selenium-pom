from pytest_bdd import given, when, then

from pages.medishop.login_page import MediShopLoginPage
from pages.medishop.shop_page import MediShopShopPage
from pages.medishop.checkout_page import MediShopCheckoutPage


DEMO_EMAIL = "trainer@way2automation.com"
DEMO_PASSWORD = "way2automation"


@given("the user has Aspirin in the shopping cart")
def user_has_aspirin_in_cart(driver, base_url):
    driver.get(base_url)

    login_page = MediShopLoginPage(driver)

    assert login_page.login(
        DEMO_EMAIL,
        DEMO_PASSWORD,
    )

    shop_page = MediShopShopPage(driver)

    assert shop_page.search_medicine("Aspirin")
    assert shop_page.add_to_cart()
    assert shop_page.click_cart()


@when("the user opens the checkout page")
def open_checkout(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.click_secure_checkout()


@when("the user attempts to place the order without delivery information")
def attempt_order_without_delivery_information(driver):
    checkout_page = MediShopCheckoutPage(driver)

    assert checkout_page.click_place_order()


@then("the checkout should not be completed")
def verify_checkout_not_completed(driver):
    assert "login.html" not in driver.current_url.lower()