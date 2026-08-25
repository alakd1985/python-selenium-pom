from __future__ import annotations

import time
from pathlib import Path
from typing import Optional, Sequence, Tuple, Union

import utilities.custom_logger as cl
import logging

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]
ElementOrLocator = Union[WebElement, str]


class BasePage:
    """
    Base Page Object for Selenium Page Objects.

    Provides common, reusable browser and element operations.

    Page classes such as LoginPage, DashboardPage, AdminPage, etc.
    should inherit from this class.
    """

    log = cl.customLogger(logging.DEBUG)

    DEFAULT_TIMEOUT = 10
    DEFAULT_POLL_FREQUENCY = 0.5

    def __init__(
            self,
            driver,
            timeout: int = DEFAULT_TIMEOUT,
            poll_frequency: float = DEFAULT_POLL_FREQUENCY,
    ):
        if driver is None:
            raise ValueError("WebDriver instance cannot be None.")

        self.driver = driver
        self.timeout = timeout
        self.poll_frequency = poll_frequency

    # =========================================================
    # Locator Handling
    # =========================================================

    @staticmethod
    def get_by_type(locator_type: str) -> str:
        """
        Convert framework locator type to Selenium By strategy.

        Supported values:
            id
            name
            xpath
            css
            class / classname
            link / linktext
            partial_link / partiallinktext
            tag / tagname
        """

        if not locator_type:
            raise ValueError("locator_type cannot be empty.")

        locator_type = locator_type.strip().lower()

        locator_map = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "classname": By.CLASS_NAME,
            "link": By.LINK_TEXT,
            "linktext": By.LINK_TEXT,
            "partial_link": By.PARTIAL_LINK_TEXT,
            "partiallinktext": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME,
            "tagname": By.TAG_NAME,
        }

        if locator_type not in locator_map:
            raise ValueError(
                f"Unsupported locator type: '{locator_type}'. "
                f"Supported types: {', '.join(locator_map.keys())}"
            )

        return locator_map[locator_type]

    def build_locator(
            self,
            locator: str,
            locator_type: str = "xpath",
    ) -> Locator:
        """
        Build Selenium locator tuple.
        """

        if not locator:
            raise ValueError("locator cannot be empty.")

        return (
            self.get_by_type(locator_type),
            locator,
        )

    # =========================================================
    # WebDriver / Browser Operations
    # =========================================================

    def get_title(self) -> str:
        """Return current browser title."""

        return self.driver.title

    def get_current_url(self) -> str:
        """Return current browser URL."""

        return self.driver.current_url

    def refresh_page(self) -> None:
        """Refresh the current page."""

        self.driver.refresh()

    def navigate_back(self) -> None:
        """Navigate backward in browser history."""

        self.driver.back()

    def navigate_forward(self) -> None:
        """Navigate forward in browser history."""

        self.driver.forward()

    # =========================================================
    # Element Retrieval
    # =========================================================

    def get_element(
            self,
            locator: str,
            locator_type: str = "xpath",
            timeout: Optional[int] = None,
    ) -> Optional[WebElement]:
        """
        Wait for and return an element.

        Uses visibility by default because this is generally
        more useful for page interactions than raw DOM presence.
        """

        timeout = timeout or self.timeout
        by, value = self.build_locator(
            locator,
            locator_type,
        )

        try:
            wait = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=self.poll_frequency,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            )

            element = wait.until(
                EC.visibility_of_element_located(
                    (by, value)
                )
            )

            self.log.debug(
                f"Element found: {locator} ({locator_type})"
            )

            return element

        except TimeoutException:
            self.log.error(
                f"Timeout waiting for element: "
                f"{locator} ({locator_type})"
            )
            return None

    def get_elements(
            self,
            locator: str,
            locator_type: str = "xpath",
    ) -> list[WebElement]:
        """
        Return all matching elements.

        Returns an empty list if no elements are found.
        """

        by, value = self.build_locator(
            locator,
            locator_type,
        )

        try:
            elements = self.driver.find_elements(
                by,
                value,
            )

            self.log.debug(
                f"Found {len(elements)} element(s): "
                f"{locator} ({locator_type})"
            )

            return elements

        except WebDriverException as exc:
            self.log.error(
                f"Unable to find elements: "
                f"{locator} ({locator_type}) - {exc}"
            )
            return []

    # =========================================================
    # Wait Operations
    # =========================================================

    def wait_for_element_present(
            self,
            locator: str,
            locator_type: str = "xpath",
            timeout: Optional[int] = None,
    ) -> Optional[WebElement]:
        """
        Wait until the element exists in the DOM.
        """

        timeout = timeout or self.timeout
        by, value = self.build_locator(
            locator,
            locator_type,
        )

        try:
            wait = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=self.poll_frequency,
            )

            return wait.until(
                EC.presence_of_element_located(
                    (by, value)
                )
            )

        except TimeoutException:
            self.log.error(
                f"Element not present after {timeout}s: "
                f"{locator} ({locator_type})"
            )
            return None

    def wait_for_element_visible(
            self,
            locator: str,
            locator_type: str = "xpath",
            timeout: Optional[int] = None,
    ) -> Optional[WebElement]:
        """
        Wait until the element is visible.
        """

        timeout = timeout or self.timeout
        by, value = self.build_locator(
            locator,
            locator_type,
        )

        try:
            wait = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=self.poll_frequency,
            )

            return wait.until(
                EC.visibility_of_element_located(
                    (by, value)
                )
            )

        except TimeoutException:
            self.log.error(
                f"Element not visible after {timeout}s: "
                f"{locator} ({locator_type})"
            )
            return None

    def wait_for_element_clickable(
            self,
            locator: str,
            locator_type: str = "xpath",
            timeout: Optional[int] = None,
    ) -> Optional[WebElement]:
        """
        Wait until the element can be clicked.
        """

        timeout = timeout or self.timeout
        by, value = self.build_locator(
            locator,
            locator_type,
        )

        try:
            wait = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=self.poll_frequency,
            )

            return wait.until(
                EC.element_to_be_clickable(
                    (by, value)
                )
            )

        except TimeoutException:
            self.log.error(
                f"Element not clickable after {timeout}s: "
                f"{locator} ({locator_type})"
            )
            return None

    # =========================================================
    # Element Actions
    # =========================================================

    def click(
            self,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
            timeout: Optional[int] = None,
    ) -> bool:
        """
        Click an element.

        Can accept either:
            1. locator + locator_type
            2. an existing WebElement
        """

        try:
            target = element

            if target is None:
                if not locator:
                    raise ValueError(
                        "Either locator or element must be provided."
                    )

                target = self.wait_for_element_clickable(
                    locator,
                    locator_type,
                    timeout,
                )

            if target is None:
                return False

            target.click()

            self.log.info(
                f"Clicked element: "
                f"{locator or '<WebElement>'}"
            )

            return True

        except (
                ElementClickInterceptedException,
                ElementNotInteractableException,
                StaleElementReferenceException,
        ) as exc:

            self.log.error(
                f"Unable to click element: "
                f"{locator or '<WebElement>'} - {exc}"
            )

            return False

    def send_keys(
            self,
            text: str,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
            clear_first: bool = True,
            timeout: Optional[int] = None,
    ) -> bool:
        """
        Enter text into an input element.

        Can accept either:
            1. locator + locator_type
            2. an existing WebElement
        """

        try:
            target = element

            if target is None:
                if not locator:
                    raise ValueError(
                        "Either locator or element must be provided."
                    )

                target = self.wait_for_element_visible(
                    locator,
                    locator_type,
                    timeout,
                )

            if target is None:
                return False

            if clear_first:
                target.clear()

            target.send_keys(text)

            self.log.info(
                f"Entered text into: "
                f"{locator or '<WebElement>'}"
            )

            return True

        except (
                ElementNotInteractableException,
                StaleElementReferenceException,
        ) as exc:

            self.log.error(
                f"Unable to send keys to: "
                f"{locator or '<WebElement>'} - {exc}"
            )

            return False

    # =========================================================
    # Text Operations
    # =========================================================

    def get_text(
            self,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
            timeout: Optional[int] = None,
    ) -> Optional[str]:
        """
        Return visible element text.

        Falls back to innerText when Selenium's .text is empty.
        """

        try:
            target = element

            if target is None:
                if not locator:
                    raise ValueError(
                        "Either locator or element must be provided."
                    )

                target = self.wait_for_element_visible(
                    locator,
                    locator_type,
                    timeout,
                )

            if target is None:
                return None

            text = target.text.strip()

            if not text:
                text = (
                        target.get_attribute("innerText") or ""
                ).strip()

            self.log.debug(
                f"Element text: '{text}'"
            )

            return text

        except (
                StaleElementReferenceException,
                WebDriverException,
        ) as exc:

            self.log.error(
                f"Unable to get element text: "
                f"{locator or '<WebElement>'} - {exc}"
            )

            return None

    # =========================================================
    # Element Verification
    # =========================================================

    def is_element_present(
            self,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
    ) -> bool:
        """
        Check whether an element exists in the DOM.

        Does not require the element to be visible.
        """

        try:
            if element is not None:
                return element.is_enabled() or True

            if not locator:
                raise ValueError(
                    "Either locator or element must be provided."
                )

            by, value = self.build_locator(
                locator,
                locator_type,
            )

            return len(
                self.driver.find_elements(
                    by,
                    value,
                )
            ) > 0

        except (
                StaleElementReferenceException,
                WebDriverException,
        ):

            return False

    def is_element_visible(
            self,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
    ) -> bool:
        """
        Check whether an element exists and is visible.
        """

        try:
            if element is not None:
                return element.is_displayed()

            if not locator:
                raise ValueError(
                    "Either locator or element must be provided."
                )

            by, value = self.build_locator(
                locator,
                locator_type,
            )

            elements = self.driver.find_elements(
                by,
                value,
            )

            return any(
                current_element.is_displayed()
                for current_element in elements
            )

        except (
                StaleElementReferenceException,
                WebDriverException,
        ):

            return False

    def is_element_enabled(
            self,
            locator: str,
            locator_type: str = "xpath",
    ) -> bool:
        """
        Check whether an element is enabled.
        """

        try:
            element = self.get_element(
                locator,
                locator_type,
            )

            return (
                    element is not None
                    and element.is_enabled()
            )

        except WebDriverException:
            return False

    # =========================================================
    # Element Presence Check
    # =========================================================

    def element_presence_check(
            self,
            locator: str,
            locator_type: str = "xpath",
    ) -> bool:
        """
        Explicit presence check without waiting.

        Similar to SeleniumDriver.elementPresenceCheck().
        """

        return self.is_element_present(
            locator,
            locator_type,
        )

    # =========================================================
    # Scrolling
    # =========================================================

    def scroll_to_element(
            self,
            locator: str,
            locator_type: str = "xpath",
            timeout: Optional[int] = None,
    ) -> bool:
        """
        Scroll the page until an element is in view.
        """

        element = self.get_element(
            locator,
            locator_type,
            timeout,
        )

        if element is None:
            return False

        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView("
                "{block: 'center', inline: 'nearest'});",
                element,
            )

            return True

        except WebDriverException as exc:
            self.log.error(
                f"Unable to scroll to element: "
                f"{locator} - {exc}"
            )
            return False

    def scroll(self, direction: str = "down", pixels: int = 1000) -> None:
        """
        Scroll page up or down.

        Example:
            scroll("down", 1000)
            scroll("up", 500)
        """

        direction = direction.lower()

        if direction not in {"up", "down"}:
            raise ValueError(
                "direction must be either 'up' or 'down'."
            )

        offset = pixels if direction == "down" else -pixels

        self.driver.execute_script(
            "window.scrollBy(0, arguments[0]);",
            offset,
        )

    def scroll_to_top(self) -> None:
        """Scroll to the top of the page."""

        self.driver.execute_script(
            "window.scrollTo(0, 0);"
        )

    def scroll_to_bottom(self) -> None:
        """Scroll to the bottom of the page."""

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    # =========================================================
    # Screenshot
    # =========================================================

    def take_screenshot(
            self,
            name: str = "screenshot",
            directory: str = "screenshots",
    ) -> Optional[str]:
        """
        Capture a screenshot and return its file path.
        """

        try:
            screenshot_dir = Path(directory)
            screenshot_dir.mkdir(
                parents=True,
                exist_ok=True,
            )

            timestamp = int(time.time() * 1000)

            safe_name = (
                name.replace(" ", "_")
                .replace("/", "_")
                .replace("\\", "_")
            )

            file_path = (
                    screenshot_dir
                    / f"{safe_name}_{timestamp}.png"
            )

            self.driver.save_screenshot(
                str(file_path)
            )

            self.log.info(
                f"Screenshot saved: {file_path}"
            )

            return str(file_path)

        except WebDriverException as exc:

            self.log.error(
                f"Unable to take screenshot: {exc}"
            )

            return None
