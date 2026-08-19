from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotSelectableException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack
import utilities.custom_logger as cl
import logging


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # ---------------------------
    # Locator Type Conversion
    # ---------------------------
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        mapping = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "classname": By.CLASS_NAME,
            "linktext": By.LINK_TEXT
        }
        return mapping.get(locatorType)

    # ---------------------------
    # Wait for Element (presence)
    # ---------------------------
    def waitForElement(self, locator, locatorType="xpath", timeout=10):
        try:
            byType = self.getByType(locatorType)
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(
                EC.presence_of_element_located((byType, locator))
            )
            self.log.info(f"Element present: {locator} ({locatorType})")
            return element
        except Exception:
            self.log.info(f"Element NOT present: {locator} ({locatorType})")
            print_stack()
            return None

    # ---------------------------
    # Get Element (with wait)
    # ---------------------------
    def getElement(self, locator, locatorType="xpath"):
        try:
            element = self.waitForElement(locator, locatorType)
            return element
        except Exception:
            self.log.info(f"Element NOT found: {locator} ({locatorType})")
            return None

    # ---------------------------
    # Click Element
    # ---------------------------
    def elementClick(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f"Clicked element: {locator} ({locatorType})")
        except Exception:
            self.log.info(f"Cannot click element: {locator} ({locatorType})")
            print_stack()

    # ---------------------------
    # Send Keys
    # ---------------------------
    def sendKeys(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f"Sent keys to: {locator} ({locatorType})")
        except Exception:
            self.log.info(f"Cannot send keys to: {locator} ({locatorType})")
            print_stack()

    # ---------------------------
    # Element Present Check
    # ---------------------------
    def isElementPresent(self, locator, locatorType="xpath"):
        try:
            element = self.waitForElement(locator, locatorType, timeout=5)
            return element is not None
        except Exception:
            return False
    def verifyElementPresent(self, locator, locatorType="xpath"):
        element = self.isElementPresent(locator, locatorType)
        return element is True
