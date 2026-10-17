

from pytest_bdd import parsers, then, when

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


@when("the user opens the cancel order dialog")
def user_opens_cancel_order_dialog(driver):
    order_page = MediShopOrderDetailsPage(driver)
    assert order_page.open_cancel_order_dialog(), (
        "Unable to open the cancel order dialog"
    )


@then("the cancel order dialog should be displayed")
def cancel_order_dialog_should_be_displayed(driver):
    order_page = MediShopOrderDetailsPage(driver)
    assert order_page.is_cancel_order_dialog_displayed(), (
        "Cancel order dialog was not displayed"
    )


@when("the user chooses to keep the order")
def user_chooses_to_keep_order(driver):
    order_page = MediShopOrderDetailsPage(driver)
    assert order_page.keep_order(), "Unable to select Keep order"


@then("the cancel order dialog should close")
def cancel_order_dialog_should_close(driver):
    order_page = MediShopOrderDetailsPage(driver)
    assert order_page.is_cancel_order_dialog_closed(), (
        "Cancel order dialog did not close"
    )


@when(parsers.parse('the user selects cancellation reason "{reason}"'))
def user_selects_cancellation_reason(driver, reason):
    order_page = MediShopOrderDetailsPage(driver)
    assert order_page.select_cancellation_reason(reason), (
        f"Unable to select cancellation reason: {reason}"
    )


@when("the user confirms the cancellation")
def user_confirms_cancellation(driver):
    order_page = MediShopOrderDetailsPage(driver)
    assert order_page.confirm_cancel_order(), (
        "Unable to confirm order cancellation"
    )


@then("the order should be cancelled")
def order_should_be_cancelled(driver):
    order_page = MediShopOrderDetailsPage(driver)
    assert order_page.is_order_cancelled(), (
        "Cancelled order status was not displayed"
    )

@then(parsers.parse('the cancellation message should contain "{reason}"'))
def cancellation_message_should_contain_reason(driver, reason):
    order_page = MediShopOrderDetailsPage(driver)
    message = order_page.get_cancellation_message()

    assert message, "Cancellation message was not displayed"
    assert reason in message, (
        f"Expected cancellation reason {reason!r} "
        f"to appear in message {message!r}"
    )

