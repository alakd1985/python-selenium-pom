from pytest_bdd import when

from pages.medishop.shop_page import MediShopShopPage


@when("the user searches for Aspirin")
def user_searches_for_aspirin(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.search_medicine("aspirin"), (
        "Unable to search for Aspirin"
    )


@when("the user adds Aspirin to the cart")
def user_adds_aspirin_to_cart(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.add_to_cart(), (
        "Unable to add Aspirin to the cart"
    )


@when("the user clicks the shopping cart")
def user_clicks_shopping_cart(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.click_cart(), (
        "Unable to click the shopping cart"
    )