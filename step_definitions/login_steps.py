from pytest_bdd import given, when, then, parsers

from configuration.config import (
    VALID_USERNAME,
    VALID_PASSWORD,
)

from pages.home.login_page import LoginPage


# =========================================================
# Background
# =========================================================

@given(
    "the user is on the OrangeHRM login page",
    target_fixture="login_page",
)
def user_is_on_login_page(driver):

    login_page = LoginPage(driver)

    assert login_page.is_element_visible(
        locator=login_page._username_field,
        locator_type="xpath",
    ), "OrangeHRM login page was not loaded"

    return login_page


# =========================================================
# Valid Login
# =========================================================

@when("the user logs in with valid credentials")
def user_logs_in_with_valid_credentials(login_page):

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD,
    )


@then("the Dashboard should be displayed")
def dashboard_should_be_displayed(login_page):

    assert login_page.verify_login_successful(), (
        "Dashboard was not displayed after successful login"
    )


# =========================================================
# Scenario Outline - Invalid Credentials
# =========================================================

@when(
    parsers.parse(
        'the user logs in with username "{username}" '
        'and password "{password}"'
    )
)
def user_logs_in_with_credentials(
    login_page,
    username,
    password,
):

    login_page.login(
        username,
        password,
    )


@then(
    "the invalid credentials message should be displayed"
)
def invalid_credentials_message_should_be_displayed(
    login_page,
):

    assert login_page.verify_invalid_credentials(), (
        "Invalid credentials message was not displayed"
    )


# =========================================================
# Empty Credentials
# =========================================================

@when(
    "the user clicks the Login button "
    "without entering credentials"
)
def user_clicks_login_without_credentials(login_page):

    login_page.click_login_button()


@then(
    "the required field message should be displayed"
)
def required_field_message_should_be_displayed(login_page):

    assert login_page.verify_required_field_message(), (
        "Required field message was not displayed"
    )