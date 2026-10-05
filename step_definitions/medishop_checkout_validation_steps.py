from pytest_bdd import given, when, then

from pages.medishop.login_page import MediShopLoginPage
from pages.medishop.shop_page import MediShopShopPage
from pages.medishop.checkout_page import MediShopCheckoutPage


DEMO_EMAIL = "trainer@way2automation.com"
DEMO_PASSWORD = "way2automation"


@given("the user is logged into MediShop")
def user_is_logged_into_medishop(driver, base_url):
    driver.get(base_url)
    login_page = MediShopLoginPage(driver)
    assert login_page.login(
        DEMO_EMAIL,
        DEMO_PASSWORD,
    ), "MediShop login failed"


@when('the user searches for "Aspirin"')
def search_for_aspirin(shop_page):
    assert shop_page.search_medicine("Aspirin"), (
        "Unable to search for Aspirin"
    )


@when("the user adds the product to the cart")
def add_product_to_cart(shop_page):
    assert shop_page.add_to_cart(), (
        "Unable to add product to cart"
    )


@when("the user opens the shopping cart")
def open_shopping_cart(shop_page):
    assert shop_page.click_cart(), (
        "Unable to open shopping cart"
    )


@when("the user proceeds to checkout")
def proceed_to_checkout(shop_page):
    assert shop_page.click_checkout(), (
        "Unable to proceed to checkout"
    )


@when("the user leaves the customer name empty")
def leave_customer_name_empty(checkout_page):
    assert checkout_page.enter_name(""), (
        "Unable to clear customer name"
    )


@when("the user leaves the mobile number empty")
def leave_mobile_number_empty(checkout_page):
    assert checkout_page.enter_mobile(""), (
        "Unable to clear mobile number"
    )


@when("the user leaves the house address empty")
def leave_house_address_empty(checkout_page):
    assert checkout_page.enter_house(""), (
        "Unable to clear house address"
    )


@when("the user leaves the city empty")
def leave_city_empty(checkout_page):
    assert checkout_page.enter_city(""), (
        "Unable to clear city"
    )


@when("the user leaves the pincode empty")
def leave_pincode_empty(checkout_page):
    assert checkout_page.enter_pincode(""), (
        "Unable to clear pincode"
    )

@when("the user submits the checkout form")
def submit_checkout_form(checkout_page):
    assert checkout_page.submit_checkout_form(), (
        "Unable to submit checkout form"
    )

@then("the checkout form should show a validation error")
def verify_checkout_validation_error(checkout_page):
    assert checkout_page.is_checkout_form_invalid(), (
        "Expected checkout form validation error, "
        "but the form was considered valid."
    )