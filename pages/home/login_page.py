from base.base_page import BasePage


class LoginPage(BasePage):
    _username_field = "//input[@name='username']"
    _password_field = "//input[@name='password']"
    _login_button = "//button[@type='submit']"
    _dashboard_header = "//h6[normalize-space()='Dashboard']"
    _invalid_credentials = "//p[contains(@class,'oxd-alert-content-text')]"
    _required_field = "//span[normalize-space()='Required']"

    def enter_username(self, username: str) -> bool:
        return self.send_keys(text=username, locator=self._username_field)

    def enter_password(self, password: str) -> bool:
        return self.send_keys(text=password, locator=self._password_field)

    def click_login_button(self) -> bool:
        return self.click(locator=self._login_button)

    def login(self, username: str, password: str) -> bool:
        return (
            self.enter_username(username)
            and self.enter_password(password)
            and self.click_login_button()
        )

    def verify_login_successful(self) -> bool:
        return self.is_element_visible(locator=self._dashboard_header)

    def verify_invalid_credentials(self) -> bool:
        return self.is_element_visible(locator=self._invalid_credentials)

    def verify_required_field_message(self) -> bool:
        return self.is_element_visible(locator=self._required_field)
