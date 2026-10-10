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
