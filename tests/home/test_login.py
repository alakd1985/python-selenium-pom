import pytest

from pages.home.login_page import LoginPage
from utilities.soft_assert import SoftAssert


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        # driver fixture is guaranteed to exist here
        self.driver = driver
        self.soft = SoftAssert(self.driver)

        yield

        # Run all soft assertions after the test
        self.soft.assert_all()

    def test_valid_login(self):
        lp = LoginPage(self.driver)

        lp.login("Admin", "admin123")

        self.soft.verify(
            lp.verifyLoginSuccessful(),
            "Dashboard not visible"
        )

    def test_invalid_login_wrong_username(self):
        lp = LoginPage(self.driver)

        lp.login("Admin1", "admin123")

        self.soft.verify(
            lp.verifyInvalidCredentials(),
            "Invalid credentials not shown"
        )

    def test_invalid_login_wrong_password(self):
        lp = LoginPage(self.driver)

        lp.login("Admin", "admin1234")

        self.soft.verify(
            lp.verifyInvalidCredentials(),
            "Invalid credentials not shown"
        )

    def test_invalid_login_both_wrong(self):
        lp = LoginPage(self.driver)

        lp.login("Admin1", "admin1234")

        self.soft.verify(
            lp.verifyInvalidCredentials(),
            "Invalid credentials not shown"
        )

    def test_invalid_login_empty_fields(self):
        lp = LoginPage(self.driver)

        lp.clickLoginButton()

        self.soft.verify(
            lp.verifyRequiredFieldMessage(),
            "Required field message not shown"
        )