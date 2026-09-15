from pytest_bdd import given, when, then, parsers

from configuration.config import VALID_USERNAME, VALID_PASSWORD
from pages.home.login_page import LoginPage


@given(
    "the user is on the OrangeHRM login page",
    target_fixture="login_page",
)
def user_is_on_login_page(driver):

    login_page = LoginPage(driver)

    print("CURRENT URL:", driver.current_url)
    print("PAGE TITLE:", driver.title)

    assert login_page.wait_for_element_visible(
        locator=login_page._username_field,
        locator_type="xpath",
        timeout=15,
    ), (
        f"OrangeHRM login page was not loaded. "
        f"Current URL: {driver.current_url}"
    )

    return login_page


@when("the user logs in with valid credentials")
def user_logs_in_with_valid_credentials(login_page):

    assert login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD,
    ), "Unable to submit valid login credentials"


@then("the Dashboard should be displayed")
def dashboard_should_be_displayed(login_page):

    assert login_page.verify_login_successful(), (
        "Dashboard was not displayed after successful login"
    )


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
    assert login_page.login(
        username,
        password,
    ), "Unable to submit login credentials"


@then("the invalid credentials message should be displayed")
def invalid_credentials_message_should_be_displayed(login_page):

    assert login_page.verify_invalid_credentials(), (
        "Invalid credentials message was not displayed"
    )


@when(
    "the user clicks the Login button without entering credentials"
)
def user_clicks_login_without_credentials(login_page):

    assert login_page.click_login_button()


@then("the required field message should be displayed")
def required_field_message_should_be_displayed(login_page):

    assert login_page.verify_required_field_message(), (
        "Required field message was not displayed"
    )