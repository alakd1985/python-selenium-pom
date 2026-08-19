from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ---------------------------
    # Locators
    # ---------------------------
    _userName_field = "//input[@placeholder='Username']"
    _password_field = "//input[@placeholder='Password']"
    _login_button = "//button[@type='submit']"
    _dashboard_text = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Dashboard']"
    _invalid_credentials = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
    _required_field = "//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]"




    # ---------------------------
    # Actions
    # ---------------------------
    def enterEmail(self, email):
        self.log.info(f"Entering email: {email}")
        self.sendKeys(email, self._userName_field, "xpath")

    def enterPassword(self, password):
        self.log.info("Entering password.")
        self.sendKeys(password, self._password_field, "xpath")

    def clickLoginButton(self):
        self.log.info("Clicking login button.")
        self.elementClick(self._login_button, "xpath")

    def login(self, email, password):
        self.waitForElement(self._userName_field, "xpath")
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    # ---------------------------
    # Verifications
    # ---------------------------
    def verifyLoginSuccessful(self):
        self.log.info("Verifying login success.")
        return self.isElementPresent(self._dashboard_text, "xpath")

    def verifyInvalidCredentials(self):
        self.waitForElement(self._invalid_credentials, "xpath", timeout=3)
        return self.isElementPresent(self._invalid_credentials, "xpath")

    def verifyRequiredFieldMessage(self):
        self.waitForElement(self._required_field, "xpath", timeout=3)
        return self.isElementPresent(self._required_field, "xpath")

    def verifyLoginSuccessful(self):
        return self.verifyElementPresent(self._dashboard_text, "xpath")

    def verifyInvalidCredentials(self):
        return self.verifyElementPresent(self._invalid_credentials, "xpath")

    def verifyRequiredFieldMessage(self):
        return self.verifyElementPresent(self._required_field, "xpath")


