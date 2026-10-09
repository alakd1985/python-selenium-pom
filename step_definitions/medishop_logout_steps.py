from pytest_bdd import given, then, when

from pages.medishop.login_page import MediShopLoginPage

DEMO_EMAIL = "trainer@way2automation.com"
DEMO_PASSWORD = "way2automation"


@given("the user is logged into MediShop")
def user_is_logged_into_medishop(driver, base_url):
    driver.get(base_url)

    login_page = MediShopLoginPage(driver)

    assert login_page.login(
        DEMO_EMAIL,
        DEMO_PASSWORD,
    )


@when("the user logs out")
def logout(driver):
    login_page = MediShopLoginPage(driver)
    assert login_page.logout()


@then("the user should be returned to the login page")
def verify_login_page(driver):
    assert "login.html" in driver.current_url.lower()