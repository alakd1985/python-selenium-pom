from pathlib import Path

from pytest_bdd import given, when, then

from pages.medishop.login_page import MediShopLoginPage
from pages.medishop.shop_page import MediShopShopPage
from pages.medishop.prescription_page import MediShopPrescriptionPage


@given("the user is on the MediShop login page")
def user_on_login_page(driver, settings):
    driver.get(settings.base_url)


@when("the user logs in with valid demo credentials")
def user_logs_in_with_valid_demo_credentials(driver, settings):
    login_page = MediShopLoginPage(driver)

    assert login_page.login(
        email=settings.username,
        password=settings.password,
    ), "MediShop login failed"


@then("the MediShop home page should be displayed")
def verify_medishop_home_page(driver):
    assert (
        "MediShop" in driver.title
        or "MediShop" in driver.page_source
    )


@when("the user clicks Browse medicines")
def click_browse_medicines(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.click_browse_medicines(), (
        "Unable to click Browse medicines"
    )


@when("the user selects Prescription only")
def select_prescription_only(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.select_prescription_only(), (
        "Unable to select Prescription only filter"
    )


@when("the user adds Salbutamol to the cart")
def add_salbutamol_to_cart(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.add_salbutamol_to_cart(), (
        "Unable to add Salbutamol to the cart"
    )


@when("the user clicks the shopping cart")
def click_shopping_cart(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.click_cart(), (
        "Unable to click the shopping cart"
    )


@when("the user clicks Secure checkout")
def click_secure_checkout(driver):
    shop_page = MediShopShopPage(driver)

    assert shop_page.click_secure_checkout(), (
        "Unable to click Secure checkout"
    )


@when("the user clicks Upload a prescription")
def click_upload_prescription(driver):
    prescription_page = MediShopPrescriptionPage(driver)

    assert prescription_page.click_upload_prescription(), (
        "Unable to click Upload a prescription"
    )


@when("the user clicks Upload your first prescription")
def click_upload_first_prescription(driver):
    prescription_page = MediShopPrescriptionPage(driver)

    assert prescription_page.click_upload_first_prescription(), (
        "Unable to click Upload your first prescription"
    )


@when("the user uploads the test prescription")
def upload_test_prescription(
    prescription_page: MediShopPrescriptionPage,
):
    file_path = (
        Path(__file__).resolve().parents[1]
        / "test_data"
        / "prescriptions"
        / "test_prescription.txt"
    )

    assert file_path.exists(), (
        f"Prescription test file not found: {file_path}"
    )

    assert prescription_page.upload_prescription_file(
        str(file_path)
    ), "Unable to upload the test prescription"


@when("the user accepts the prescription confirmation")
def accept_prescription_confirmation(
    prescription_page: MediShopPrescriptionPage,
):
    assert prescription_page.accept_prescription_consent(), (
        "Unable to accept prescription confirmation"
    )


@when("the user saves the prescription")
def save_prescription(
    prescription_page: MediShopPrescriptionPage,
):
    assert prescription_page.save_prescription(), (
        "Unable to save the prescription"
    )


@then("the prescription should be uploaded successfully")
def verify_prescription_uploaded(
    prescription_page: MediShopPrescriptionPage,
):
    assert prescription_page.is_prescription_uploaded(), (
        "Prescription was not uploaded successfully"
    )