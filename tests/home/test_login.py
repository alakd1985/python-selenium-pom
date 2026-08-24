import pytest

from pages.home.login_page import LoginPage
from utilities.soft_assert import SoftAssert


class TestLogin:

    # ---------------------------------------------------------
    # Test Setup / Teardown
    # ---------------------------------------------------------

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Initialize WebDriver and SoftAssert for every test.
        """

        self.driver = driver
        self.soft = SoftAssert(self.driver)

        yield

        # Execute all soft assertions after the test
        self.soft.assert_all()

    # ---------------------------------------------------------
    # Valid Login
    # ---------------------------------------------------------

    def test_valid_login(self):
        """
        Verify that a user can successfully log in
        with valid username and password.
        """

        lp = LoginPage(self.driver)

        lp.login(
            "Admin",
            "admin123"
        )

        self.soft.verify(
            lp.verify_login_successful(),
            "Dashboard not visible after successful login"
        )

    # ---------------------------------------------------------
    # Invalid Username
    # ---------------------------------------------------------

    def test_invalid_login_wrong_username(self):
        """
        Verify login fails when username is incorrect.
        """

        lp = LoginPage(self.driver)

        lp.login(
            "Admin1",
            "admin123"
        )

        self.soft.verify(
            lp.verify_invalid_credentials(),
            "Invalid credentials message not shown for wrong username"
        )

    # ---------------------------------------------------------
    # Invalid Password
    # ---------------------------------------------------------

    def test_invalid_login_wrong_password(self):
        """
        Verify login fails when password is incorrect.
        """

        lp = LoginPage(self.driver)

        lp.login(
            "Admin",
            "admin1234"
        )

        self.soft.verify(
            lp.verify_invalid_credentials(),
            "Invalid credentials message not shown for wrong password"
        )

    # ---------------------------------------------------------
    # Invalid Username + Password
    # ---------------------------------------------------------

    def test_invalid_login_both_wrong(self):
        """
        Verify login fails when both username and password
        are incorrect.
        """

        lp = LoginPage(self.driver)

        lp.login(
            "Admin1",
            "admin1234"
        )

        self.soft.verify(
            lp.verify_invalid_credentials(),
            "Invalid credentials message not shown when both credentials are wrong"
        )

    # ---------------------------------------------------------
    # Empty Username + Password
    # ---------------------------------------------------------

    def test_invalid_login_empty_fields(self):
        """
        Verify required field validation when both fields
        are left empty.
        """

        lp = LoginPage(self.driver)

        lp.click_login_button()

        self.soft.verify(
            lp.verify_required_field_message(),
            "Required field message not shown"
        )