from pytest_bdd import given, parsers, then, when

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
@when("the user increases the product quantity")
def increase_product_quantity(driver):
    shop_page = MediShopShopPage(driver)
    assert shop_page.increase_product_quantity()


@given("the user has two Aspirin in the shopping cart")
def user_has_two_aspirin_in_cart(driver, base_url):
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
    assert shop_page.increase_product_quantity()


@when("the user decreases the product quantity")
def decrease_product_quantity(driver):
    shop_page = MediShopShopPage(driver)
    assert shop_page.decrease_product_quantity()


@then(parsers.parse('the product quantity should be "{quantity}"'))
def verify_product_quantity(driver, quantity):
    shop_page = MediShopShopPage(driver)

    actual_quantity = shop_page.get_product_quantity()

    assert actual_quantity == quantity, (
        f"Expected quantity {quantity}, "
        f"but found {actual_quantity}"
    )


@when("the user clears the shopping cart")
def clear_shopping_cart(driver):
    shop_page = MediShopShopPage(driver)
    assert shop_page.clear_cart()


@when("the user continues shopping")
def continue_shopping(driver):
    shop_page = MediShopShopPage(driver)
    assert shop_page.continue_shopping()


@then("the MediShop product page should be displayed")
def verify_product_page_displayed(driver):
    assert "products.html" in driver.current_url.lower()