import pytest

from pages.medishop.checkout_page import MediShopCheckoutPage
from pages.medishop.prescription_page import MediShopPrescriptionPage
from pages.medishop.shop_page import MediShopShopPage


@pytest.fixture
def checkout_page(driver):
    return MediShopCheckoutPage(driver)

@pytest.fixture
def shop_page(driver):
    return MediShopShopPage(driver)

@pytest.fixture
def prescription_page(driver):
    return MediShopPrescriptionPage(driver)