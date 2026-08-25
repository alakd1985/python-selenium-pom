from base.base_page import BasePage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    # =========================================================
    # Locators
    # =========================================================

    _username_field = "//input[@placeholder='Username']"
    _password_field = "//input[@placeholder='Password']"
    _login_button = "//button[@type='submit']"

    _dashboard_text = (
        "//span[@class='oxd-text "
        "oxd-text--span "
        "oxd-main-menu-item--name']"
        "[normalize-space()='Dashboard']"
    )

    _invalid_credentials = (
        "//p[@class='oxd-text "
        "oxd-text--p "
        "oxd-alert-content-text']"
    )

    _required_field = (
        "//div[@class='orangehrm-login-slot-wrapper']"
        "//div[1]//div[1]//span[1]"
    )

    # =========================================================
    # Actions
    # =========================================================

    def enter_username(self, username):
        self.log.info(
            f"Entering username: {username}"
        )

        return self.send_keys(
            text=username,
            locator=self._username_field,
            locator_type="xpath"
        )

    def enter_password(self, password):
        self.log.info(
            "Entering password."
        )

        return self.send_keys(
            text=password,
            locator=self._password_field,
            locator_type="xpath"
        )

    def click_login_button(self):
        self.log.info(
            "Clicking login button."
        )

        return self.click(
            locator=self._login_button,
            locator_type="xpath"
        )

    def login(self, username, password):

        self.wait_for_element_visible(
            locator=self._username_field,
            locator_type="xpath"
        )

        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    # =========================================================
    # Verifications
    # =========================================================

    def verify_login_successful(self):

        self.log.info(
            "Verifying login success."
        )

        return self.is_element_visible(
            locator=self._dashboard_text,
            locator_type="xpath"
        )

    def verify_invalid_credentials(self):

        return self.is_element_visible(
            locator=self._invalid_credentials,
            locator_type="xpath",
            # timeout=5
        )

    def verify_required_field_message(self):

        return self.is_element_visible(
            locator=self._required_field,
            locator_type="xpath",
            # timeout=5
        )