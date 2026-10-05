
from pytest_bdd import when, then


@when("the user clicks Secure checkout")
def user_clicks_secure_checkout(shop_page):
    assert shop_page.click_secure_checkout(), (
        "Unable to click Secure checkout"
    )

@when("the user enters the checkout delivery information")
def user_enters_checkout_delivery_information(checkout_page):

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
def user_selects_cash_on_delivery(checkout_page):
    assert checkout_page.select_cash_on_delivery(), (
        "Unable to select Cash on delivery"
    )


@when("the user clicks Place order")
def user_clicks_place_order(checkout_page):
    assert checkout_page.click_place_order(), (
        "Unable to click Place order"
    )
@when("the user accepts the terms and conditions")
def user_accepts_terms_and_conditions(checkout_page):

    assert checkout_page.accept_terms_and_conditions(), (
        "Unable to accept terms and conditions"
    )
@then("the order confirmation should be displayed")
def order_confirmation_should_be_displayed(checkout_page):
    assert checkout_page.is_order_confirmed(), (
        "Order confirmation was not displayed"
    )
@then("the order ID should be displayed")
def order_id_should_be_displayed(checkout_page):
    order_id = checkout_page.get_order_id()
    assert order_id, "Order ID was not displayed"

@then("the payment method should be Cash on Delivery")
def payment_method_should_be_cash_on_delivery(checkout_page):
    payment_method = checkout_page.get_payment_method()
    assert payment_method == "Cash on Delivery", (
        f"Expected 'Cash on Delivery', "
        f"but found '{payment_method}'"
    )
@when("the user selects Credit / debit card")
def user_selects_credit_card(checkout_page):
    assert checkout_page.select_credit_card(), (
        "Unable to select Credit / debit card"
    )

@when("the user enters the card number")
def user_enters_card_number(checkout_page):
    assert checkout_page.enter_card_number(
        "4242 4242 4242 4242"
    ), "Unable to enter card number"


@when("the user enters the card expiry date")
def user_enters_card_expiry_date(checkout_page):
    assert checkout_page.enter_card_expiry(
        "12/30"
    ), "Unable to enter card expiry date"


@when("the user enters the card CVV")
def user_enters_card_cvv(checkout_page):
    assert checkout_page.enter_card_cvv(
        "123"
    ), "Unable to enter card CVV"


@when("the user enters the name on card")
def user_enters_name_on_card(checkout_page):
    assert checkout_page.enter_card_name(
        "RAHUL ARORA"
    ), "Unable to enter name on card"
@then("the payment method should be Credit / Debit Card")
def payment_method_should_be_credit_card(checkout_page):
    payment_method = checkout_page.get_payment_method()

    assert payment_method == "Credit / Debit Card", (
        f"Expected 'Credit / Debit Card', "
        f"but found '{payment_method}'"
    )