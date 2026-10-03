
from pytest_bdd import when, then
from pages.medishop.shop_page import MediShopShopPage
from pages.medishop.checkout_page import MediShopCheckoutPage


@when("the user clicks Secure checkout")
def user_clicks_secure_checkout(driver):


    shop_page = MediShopShopPage(driver)

    assert shop_page.click_secure_checkout(), (
        "Unable to click Secure checkout"
    )


@when("the user enters the checkout delivery information")
def user_enters_checkout_delivery_information(driver):
    checkout_page = MediShopCheckoutPage(driver)

    assert checkout_page.enter_name("Rahul Arora"), (
        "Unable to enter name"
    )

    assert checkout_page.enter_mobile("+1 (555) 019-2834"), (
        "Unable to enter mobile number"
    )

    assert checkout_page.enter_house("123 Main Street"), (
        "Unable to enter house/address"
    )

    assert checkout_page.enter_city("Gaithersburg"), (
        "Unable to enter city"
    )

    assert checkout_page.enter_state("Maryland"), (
        "Unable to enter state"
    )

    assert checkout_page.enter_pincode("20877"), (
        "Unable to enter pincode"
    )

    assert checkout_page.select_country("United States"), (
        "Unable to select country"
    )

    assert checkout_page.enter_delivery_notes(
        "Please leave the package at the front door."
    ), "Unable to enter delivery notes"


@when("the user selects Cash on delivery")
def user_selects_cash_on_delivery(driver):
    checkout_page = MediShopCheckoutPage(driver)

    assert checkout_page.select_cash_on_delivery(), (
        "Unable to select Cash on delivery"
    )


@then("the user clicks Place order")
def user_clicks_place_order(driver):
    checkout_page = MediShopCheckoutPage(driver)

    assert checkout_page.click_place_order(), (
        "Unable to click Place order"
    )
