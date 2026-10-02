from __future__ import annotations

from selenium.common.exceptions import WebDriverException

from base.base_page import BasePage


class MediShopLoginPage(BasePage):

    _email = "//input[@id='email_id']"
    _password = "//input[@id='password_id']"
    _sign_in_button = "//button[@id='signin_button']"

    def enter_email(self, email: str) -> bool:
        try:
            return self.send_keys(
                locator=self._email,
                text=email,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error("Unable to enter email: %s", exc)
            return False

    def enter_password(self, password: str) -> bool:
        try:
            return self.send_keys(
                locator=self._password,
                text=password,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error("Unable to enter password: %s", exc)
            return False

    def click_sign_in(self) -> bool:
        try:
            return self.click(
                locator=self._sign_in_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error("Unable to click Sign in: %s", exc)
            return False

    def login(self, email: str, password: str) -> bool:
        if not self.enter_email(email):
            return False

        if not self.enter_password(password):
            return False

        return self.click_sign_in()