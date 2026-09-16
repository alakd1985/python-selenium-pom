from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Optional, Tuple

import utilities.custom_logger as cl
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


class BasePage:
    """Reusable Selenium operations shared by all page objects."""

    log = cl.customLogger(logging.DEBUG)
    DEFAULT_TIMEOUT = 10
    DEFAULT_POLL_FREQUENCY = 0.5

    def __init__(
            self,
            driver,
            timeout: int = DEFAULT_TIMEOUT,
            poll_frequency: float = DEFAULT_POLL_FREQUENCY,
    ) -> None:
        if driver is None:
            raise ValueError("WebDriver instance cannot be None.")
        self.driver = driver
        self.timeout = timeout
        self.poll_frequency = poll_frequency

    @staticmethod
    def get_by_type(locator_type: str) -> str:
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
        key = (locator_type or "").strip().lower()
        if key not in locator_map:
            raise ValueError(
                f"Unsupported locator type '{locator_type}'. "
                f"Supported: {', '.join(locator_map)}"
            )
        return locator_map[key]

    def build_locator(self, locator: str, locator_type: str = "xpath") -> Locator:
        if not locator:
            raise ValueError("locator cannot be empty.")
        return self.get_by_type(locator_type), locator

    def _wait(self, condition, timeout: Optional[int] = None):
        return WebDriverWait(
            self.driver,
            timeout if timeout is not None else self.timeout,
            poll_frequency=self.poll_frequency,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        ).until(condition)

    def wait_for_element_present(
            self, locator: str, locator_type: str = "xpath", timeout: Optional[int] = None
    ) -> Optional[WebElement]:
        try:
            return self._wait(
                EC.presence_of_element_located(self.build_locator(locator, locator_type)),
                timeout,
            )
        except TimeoutException:
            self.log.error("Element not present: %s (%s)", locator, locator_type)
            return None

    def wait_for_element_visible(
            self, locator: str, locator_type: str = "xpath", timeout: Optional[int] = None
    ) -> Optional[WebElement]:
        try:
            return self._wait(
                EC.visibility_of_element_located(self.build_locator(locator, locator_type)),
                timeout,
            )
        except TimeoutException:
            self.log.error("Element not visible: %s (%s)", locator, locator_type)
            return None

    def wait_for_element_clickable(
            self, locator: str, locator_type: str = "xpath", timeout: Optional[int] = None
    ) -> Optional[WebElement]:
        try:
            return self._wait(
                EC.element_to_be_clickable(self.build_locator(locator, locator_type)),
                timeout,
            )
        except TimeoutException:
            self.log.error("Element not clickable: %s (%s)", locator, locator_type)
            return None

    def get_element(
            self, locator: str, locator_type: str = "xpath", timeout: Optional[int] = None
    ) -> Optional[WebElement]:
        return self.wait_for_element_visible(locator, locator_type, timeout)

    def get_elements(self, locator: str, locator_type: str = "xpath") -> list[WebElement]:
        by, value = self.build_locator(locator, locator_type)
        try:
            return self.driver.find_elements(by, value)
        except WebDriverException as exc:
            self.log.error("Unable to find elements %s: %s", locator, exc)
            return []

    def click(
            self,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
            timeout: Optional[int] = None,
    ) -> bool:
        try:
            target = element or self.wait_for_element_clickable(locator, locator_type, timeout)
            if target is None:
                return False
            target.click()
            return True
        except (
                ElementClickInterceptedException,
                ElementNotInteractableException,
                StaleElementReferenceException,
                WebDriverException,
        ) as exc:
            self.log.error("Unable to click %s: %s", locator, exc)
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
        try:
            target = element or self.wait_for_element_visible(locator, locator_type, timeout)
            if target is None:
                return False
            if clear_first:
                target.clear()
            target.send_keys(str(text))
            return True
        except (
                ElementNotInteractableException,
                StaleElementReferenceException,
                WebDriverException,
        ) as exc:
            self.log.error("Unable to enter text into %s: %s", locator, exc)
            return False

    def clear(self, locator: str, locator_type: str = "xpath") -> bool:
        element = self.get_element(locator, locator_type)
        if element is None:
            return False
        element.clear()
        return True

    def get_text(
            self,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
            timeout: Optional[int] = None,
    ) -> Optional[str]:
        try:
            target = element or self.get_element(locator, locator_type, timeout)
            if target is None:
                return None
            value = (target.text or "").strip()
            return value or (target.get_attribute("innerText") or "").strip()
        except WebDriverException as exc:
            self.log.error("Unable to get text from %s: %s", locator, exc)
            return None

    def get_attribute(
            self, locator: str, attribute: str, locator_type: str = "xpath"
    ) -> Optional[str]:
        element = self.get_element(locator, locator_type)
        return element.get_attribute(attribute) if element else None

    def is_element_present(
            self,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
    ) -> bool:
        try:
            if element is not None:
                return True
            if not locator:
                raise ValueError("Either locator or element must be provided.")
            by, value = self.build_locator(locator, locator_type)
            return bool(self.driver.find_elements(by, value))
        except WebDriverException:
            return False

    def is_element_visible(
            self,
            locator: Optional[str] = None,
            locator_type: str = "xpath",
            element: Optional[WebElement] = None,
    ) -> bool:
        try:
            if element is not None:
                return element.is_displayed()
            if not locator:
                raise ValueError("Either locator or element must be provided.")
            return any(e.is_displayed() for e in self.get_elements(locator, locator_type))
        except WebDriverException:
            return False

    def is_element_enabled(self, locator: str, locator_type: str = "xpath") -> bool:
        element = self.get_element(locator, locator_type)
        return bool(element and element.is_enabled())

    def scroll_to_element(
            self, locator: str, locator_type: str = "xpath", timeout: Optional[int] = None
    ) -> bool:
        element = self.get_element(locator, locator_type, timeout)
        if element is None:
            return False
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                element,
            )
            return True
        except WebDriverException as exc:
            self.log.error("Unable to scroll to %s: %s", locator, exc)
            return False

    def scroll(self, direction: str = "down", pixels: int = 1000) -> None:
        direction = direction.lower()
        if direction not in {"up", "down"}:
            raise ValueError("direction must be 'up' or 'down'.")
        self.driver.execute_script(
            "window.scrollBy(0, arguments[0]);", pixels if direction == "down" else -pixels
        )

    def refresh_page(self) -> None:
        self.driver.refresh()

    def navigate_back(self) -> None:
        self.driver.back()

    def navigate_forward(self) -> None:
        self.driver.forward()

    def get_title(self) -> str:
        return self.driver.title

    def get_current_url(self) -> str:
        return self.driver.current_url

    def take_screenshot(self, name: str = "screenshot", directory: str = "screenshots") -> Optional[str]:
        try:
            folder = Path(directory)
            folder.mkdir(parents=True, exist_ok=True)
            safe_name = name.replace(" ", "_").replace("/", "_").replace("\\", "_")
            path = folder / f"{safe_name}_{int(time.time() * 1000)}.png"
            self.driver.save_screenshot(str(path))
            return str(path)
        except WebDriverException as exc:
            self.log.error("Unable to take screenshot: %s", exc)
            return None

    def wait_for_element_invisible(
            self,
            locator: str,
            locator_type: str = "xpath",
            timeout: Optional[int] = None,
    ) -> bool:
        try:
            result = WebDriverWait(
                self.driver,
                timeout if timeout is not None else self.timeout,
                poll_frequency=self.poll_frequency,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            ).until(
                EC.invisibility_of_element_located(
                    self.build_locator(locator, locator_type)
                )
            )

            return bool(result)

        except TimeoutException:
            self.log.error(
                "Element did not become invisible: %s (%s)",
                locator,
                locator_type,
            )
            return False