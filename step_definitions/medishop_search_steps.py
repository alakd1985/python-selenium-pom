from pytest_bdd import given, parsers, then, when

from pages.medishop.login_page import MediShopLoginPage
from pages.medishop.shop_page import MediShopShopPage

DEMO_EMAIL = "trainer@way2automation.com"
DEMO_PASSWORD = "way2automation"


@given("the user is logged into MediShop")
def user_is_logged_into_medishop(driver, settings):
    driver.get(settings.base_url)
    login_page = MediShopLoginPage(driver)
    assert login_page.login(
        settings.username,
        settings.password,
    ), "MediShop login failed"

@when(parsers.parse('the user searches for "{product}"'))
def search_for_product(driver, product):
    shop_page = MediShopShopPage(driver)

    assert shop_page.search_medicine(product)


@then(parsers.parse('the search results should contain "{product}"'))
def verify_search_result(driver, product):
    assert product.lower() in driver.page_source.lower()


@then("no matching product should be displayed")
def verify_no_matching_product(driver):
    assert "ProductThatDoesNotExist123".lower() not in (
        driver.page_source.lower()
    )