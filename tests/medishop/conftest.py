import pytest

from pages.medishop.checkout_page import MediShopCheckoutPage
from pages.medishop.shop_page import MediShopShopPage

pytest_plugins = [
    "step_definitions.medishop_login_steps",
    "step_definitions.medishop_shop_steps",
    "step_definitions.medishop_checkout_steps",
    "step_definitions.medishop_negative_login_steps",
    "step_definitions.medishop_search_steps",
    "step_definitions.medishop_cart_steps",
    "step_definitions.medishop_checkout_validation_steps",
    "step_definitions.medishop_logout_steps",
]

@pytest.fixture
def checkout_page(driver):
    return MediShopCheckoutPage(driver)

@pytest.fixture
def shop_page(driver):
    return MediShopShopPage(driver)