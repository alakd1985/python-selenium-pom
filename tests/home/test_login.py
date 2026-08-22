import pytest
from pages.home.login_page import LoginPage
from utilities.soft_assert import SoftAssert

@pytest.mark.usefixtures("driver")
class TestLogin:

    def setup_method(self):
        self.soft = SoftAssert(self.driver)

    def teardown_method(self):
        # Ensure soft assertions run but do NOT block fixture teardown
        try:
            self.soft.assert_all()
        finally:
            pass

    def test_valid_login(self):
        lp = LoginPage(self.driver)
        lp.login("Admin", "admin123")
        self.soft.verify(lp.verifyLoginSuccessful(), "Dashboard not visible")

    def test_invalid_login_wrong_username(self):
        lp = LoginPage(self.driver)
        lp.login("Admin1", "admin123")
        self.soft.verify(lp.verifyInvalidCredentials(), "Invalid credentials not shown")

    def test_invalid_login_wrong_password(self):
        lp = LoginPage(self.driver)
        lp.login("Admin", "admin1234")
        self.soft.verify(lp.verifyInvalidCredentials(), "Invalid credentials not shown")

    def test_invalid_login_both_wrong(self):
        lp = LoginPage(self.driver)
        lp.login("Admin1", "admin1234")
        self.soft.verify(lp.verifyInvalidCredentials(), "Invalid credentials not shown")

    def test_invalid_login_empty_fields(self):
        lp = LoginPage(self.driver)
        lp.clickLoginButton()
        self.soft.verify(lp.verifyRequiredFieldMessage(), "Required field message not shown")
