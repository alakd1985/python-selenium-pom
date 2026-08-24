from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as cl
import logging


class BasePage:
    """
    Base Page class.

    Contains common Selenium operations that can be reused
    by all Page Object classes.
    """

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # ---------------------------------------------------------
    # Locator Type Conversion
    # ---------------------------------------------------------

    def getByType(self, locatorType="xpath"):
        locatorType = locatorType.lower()

        mapping = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "classname": By.CLASS_NAME,
            "linktext": By.LINK_TEXT,
            "partiallinktext": By.PARTIAL_LINK_TEXT,
            "tagname": By.TAG_NAME,
        }

        if locatorType not in mapping:
            raise ValueError(
                f"Unsupported locator type: {locatorType}"
            )

        return mapping[locatorType]

    # ---------------------------------------------------------
    # Wait for Element
    # ---------------------------------------------------------

    def waitForElement(
        self,
        locator,
        locatorType="xpath",
        timeout=10
    ):
        try:
            byType = self.getByType(locatorType)

            wait = WebDriverWait(
                self.driver,
                timeout
            )

            element = wait.until(
                EC.presence_of_element_located(
                    (byType, locator)
                )
            )

            self.log.info(
                f"Element present: {locator} ({locatorType})"
            )

            return element

        except Exception as e:
            self.log.error(
                f"Element NOT present: "
                f"{locator} ({locatorType}) - {e}"
            )

            return None

    # ---------------------------------------------------------
    # Get Element
    # ---------------------------------------------------------

    def getElement(
        self,
        locator,
        locatorType="xpath",
        timeout=10
    ):
        return self.waitForElement(
            locator,
            locatorType,
            timeout
        )

    # ---------------------------------------------------------
    # Click Element
    # ---------------------------------------------------------

    def elementClick(
        self,
        locator,
        locatorType="xpath"
    ):
        try:
            element = self.getElement(
                locator,
                locatorType
            )

            if element is None:
                return False

            element.click()

            self.log.info(
                f"Clicked element: "
                f"{locator} ({locatorType})"
            )

            return True

        except Exception as e:
            self.log.error(
                f"Cannot click element: "
                f"{locator} ({locatorType}) - {e}"
            )

            return False

    # ---------------------------------------------------------
    # Send Keys
    # ---------------------------------------------------------

    def sendKeys(
        self,
        data,
        locator,
        locatorType="xpath"
    ):
        try:
            element = self.getElement(
                locator,
                locatorType
            )

            if element is None:
                return False

            element.clear()
            element.send_keys(data)

            self.log.info(
                f"Sent keys to: "
                f"{locator} ({locatorType})"
            )

            return True

        except Exception as e:
            self.log.error(
                f"Cannot send keys to: "
                f"{locator} ({locatorType}) - {e}"
            )

            return False

    # ---------------------------------------------------------
    # Element Present Check
    # ---------------------------------------------------------

    def isElementPresent(
        self,
        locator,
        locatorType="xpath",
        timeout=5
    ):
        try:
            element = self.waitForElement(
                locator,
                locatorType,
                timeout
            )

            return element is not None

        except Exception:
            return False

    # ---------------------------------------------------------
    # Verify Element Present
    # ---------------------------------------------------------

    def verifyElementPresent(
        self,
        locator,
        locatorType="xpath",
        timeout=5
    ):
        return self.isElementPresent(
            locator,
            locatorType,
            timeout
        )