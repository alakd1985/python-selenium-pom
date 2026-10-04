from pytest_bdd import given, when, then, parsers

from pages.medishop.login_page import MediShopLoginPage
from pages.medishop.shop_page import MediShopShopPage


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


@when(parsers.parse('the user searches for "{product}"'))
def search_for_product(driver, product):
    shop_page = MediShopShopPage(driver)

    assert shop_page.search_medicine(product)


@when("the user adds the product to the cart")
def add_product_to_cart(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.add_to_cart()

@then(parsers.parse('the shopping cart should contain "{product}"'))
def verify_product_in_cart(driver, product):
    shop_page = MediShopShopPage(driver)

    assert shop_page.is_product_in_cart(product)


@given("the user has Aspirin in the shopping cart")
def user_has_aspirin_in_cart(driver, base_url):
    driver.get(base_url)

    login_page = MediShopLoginPage(driver)

    assert login_page.login(
        DEMO_EMAIL,
        DEMO_PASSWORD,
    )

    shop_page = MediShopShopPage(driver)

    assert shop_page.search_medicine("Aspirin")
    assert shop_page.add_to_cart()
    assert shop_page.click_cart()


@when("the user removes the product from the shopping cart")
def remove_product_from_cart(driver):
    shop_page = MediShopShopPage(driver)
    assert shop_page.remove_product_from_cart()

@then("the shopping cart should be empty")
def verify_cart_empty(driver):
    assert "Your cart is empty" in driver.find_element(
        "tag name",
        "body",
    ).text