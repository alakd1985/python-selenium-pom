import pytest
import allure
from pages.home.login_page import LoginPage
from utilities.soft_assert import SoftAssert


@pytest.mark.usefixtures("driver")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.soft = SoftAssert(self.driver)

    # ---------------------------------------------------------
    # Valid Login
    # ---------------------------------------------------------

    @allure.feature("Login")
    @allure.story("Valid Login")
    @allure.title("Valid login should navigate to Dashboard")
    def test_valid_login(self):
        lp = LoginPage(self.driver)

        with allure.step("Logging in with valid credentials"):
            lp.login("Admin", "admin123")

        self.soft.verify(
            lp.verify_login_successful(),
            "Dashboard not visible after successful login"
        )

        # IMPORTANT: run assert_all inside test, not teardown
        self.soft.assert_all()

    # ---------------------------------------------------------
    # Invalid Username
    # ---------------------------------------------------------

    @allure.feature("Login")
    @allure.story("Invalid Username")
    @allure.title("Login should fail with wrong username")
    def test_invalid_login_wrong_username(self):
        lp = LoginPage(self.driver)

        with allure.step("Attempt login with wrong username"):
            lp.login("Admin1", "admin123")

        self.soft.verify(
            lp.verify_invalid_credentials(),
            "Invalid credentials message not shown for wrong username"
        )

        self.soft.assert_all()

    # ---------------------------------------------------------
    # Invalid Password
    # ---------------------------------------------------------

    @allure.feature("Login")
    @allure.story("Invalid Password")
    @allure.title("Login should fail with wrong password")
    def test_invalid_login_wrong_password(self):
        lp = LoginPage(self.driver)

        with allure.step("Attempt login with wrong password"):
            lp.login("Admin", "admin1234")

        self.soft.verify(
            lp.verify_invalid_credentials(),
            "Invalid credentials message not shown for wrong password"
        )

        self.soft.assert_all()

    # ---------------------------------------------------------
    # Invalid Username + Password
    # ---------------------------------------------------------

    @allure.feature("Login")
    @allure.story("Invalid Credentials")
    @allure.title("Login should fail with both username and password wrong")
    def test_invalid_login_both_wrong(self):
        lp = LoginPage(self.driver)

        with allure.step("Attempt login with both wrong username and password"):
            lp.login("Admin1", "admin1234")

        self.soft.verify(
            lp.verify_invalid_credentials(),
            "Invalid credentials message not shown when both credentials are wrong"
        )

        self.soft.assert_all()

    # ---------------------------------------------------------
    # Empty Username + Password
    # ---------------------------------------------------------

    @allure.feature("Login")
    @allure.story("Empty Fields")
    @allure.title("Login should show required field validation when fields are empty")
    def test_invalid_login_empty_fields(self):
        lp = LoginPage(self.driver)

        with allure.step("Click login button without entering credentials"):
            lp.click_login_button()

        self.soft.verify(
            lp.verify_required_field_message(),
            "Required field message not shown"
        )

        self.soft.assert_all()
