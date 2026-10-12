
from pytest_bdd import then, when

from pages.medishop.order_details_page import MediShopOrderDetailsPage


@when("the user clicks Track order status")
def user_clicks_track_order_status(driver):
    order_page = MediShopOrderDetailsPage(driver)

    assert order_page.open_order_tracking(), (
        "Unable to click Track order status"
    )


@then("the order tracking section should be displayed")
def order_tracking_section_should_be_displayed(driver):
    order_page = MediShopOrderDetailsPage(driver)

    assert order_page.is_order_tracking_displayed(), (
        "Order tracking section was not displayed"
    )


@when("the user clicks Print invoice")
def user_clicks_print_invoice(driver):
    order_page = MediShopOrderDetailsPage(driver)

    assert order_page.prepare_print_intercept(), (
        "Unable to prepare invoice print interception"
    )
    assert order_page.open_invoice_print_dialog(), (
        "Unable to click Print invoice"
    )


@then("the invoice print action should be triggered")
def invoice_print_action_should_be_triggered(driver):
    order_page = MediShopOrderDetailsPage(driver)

    assert order_page.was_print_triggered(), (
        "The invoice did not trigger window.print()"
    )
