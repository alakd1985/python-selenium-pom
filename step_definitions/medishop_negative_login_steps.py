from pytest_bdd import given, then, when

from pages.medishop.login_page import MediShopLoginPage


@given("the user is on the MediShop login page")
def user_is_on_login_page(driver, base_url):
    driver.get(base_url)


@when("the user enters invalid login credentials")
def enter_invalid_credentials(driver):
    login_page = MediShopLoginPage(driver)

    assert login_page.enter_email("invalid@example.com")
    assert login_page.enter_password("WrongPassword123")


@when("the user clicks the Sign In button")
def click_sign_in(driver):
    login_page = MediShopLoginPage(driver)

    assert login_page.click_sign_in()


@then("the login should not be successful")
def verify_login_failed(driver):
    assert "login.html" in driver.current_url.lower()