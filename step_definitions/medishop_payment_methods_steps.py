from pytest_bdd import given, scenarios, then, when

from pages.medishop.login_page import MediShopLoginPage
from pages.medishop.payment_methods_page import (
    MediShopPaymentMethodsPage,
)

scenarios("../feature/medishop/payment_methods.feature")


@given("the user is logged into MediShop")
def user_is_logged_into_medishop(driver, base_url):
    driver.get(base_url)

    login_page = MediShopLoginPage(driver)

    assert login_page.login(
        "trainer@way2automation.com",
        "way2automation",
    )


@when("the user opens Payment methods")
def user_opens_payment_methods(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.open_payment_methods(), (
        "Unable to open Payment methods"
    )


@then("the Payment methods page should be displayed")
def payment_methods_page_should_be_displayed(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.is_payment_methods_page_displayed(), (
        "Payment methods page was not displayed"
    )


@when("the user opens Add payment method")
def user_opens_add_payment_method(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.open_add_payment_method_modal(), (
        "Unable to open Add payment method modal"
    )


@then("the Add payment method modal should be displayed")
def add_payment_method_modal_should_be_displayed(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.is_add_payment_method_modal_displayed(), (
        "Add payment method modal was not displayed"
    )


@when('the user selects "Credit / debit card" as the payment type')
def user_selects_card_payment(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.select_payment_type("Credit / debit card"), (
        "Unable to select Credit / debit card"
    )


@when("the user fills the demo card details")
def user_fills_demo_card_details(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.use_demo_test_card(), (
        "Unable to populate the demo card details"
    )


@when("the user saves the payment method")
def user_saves_payment_method(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.save_payment_method(), (
        "Unable to save the payment method"
    )


@then("the saved payment method should be displayed")
def saved_payment_method_should_be_displayed(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.is_saved_card_displayed(), (
        "Saved payment method was not displayed"
    )


@then("the saved payment method should be the default")
def saved_payment_method_should_be_default(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.is_default_badge_displayed(), (
        "The saved payment method does not display the default badge"
    )

@when("the user deletes the saved payment method")
def user_deletes_saved_payment_method(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.delete_saved_card(), (
        "Unable to delete the saved payment method"
    )


@then("the payment methods empty state should be displayed")
def payment_methods_empty_state_should_be_displayed(driver):
    payment_page = MediShopPaymentMethodsPage(driver)

    assert payment_page.is_empty_state_displayed(), (
        "Payment methods empty state was not displayed"
    )
