from __future__ import annotations

import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

import utilities.custom_logger as cl


class WebDriverFactory:
    """Create and configure Selenium WebDriver instances."""

    log = cl.customLogger(logging.DEBUG)

    def __init__(
        self,
        browser: str = "firefox",
        headless: bool = False,
        implicit_wait: int = 0,
        window_width: int = 1920,
        window_height: int = 1080,
    ) -> None:
        self.browser = browser.strip().lower()
        self.headless = headless
        self.implicit_wait = implicit_wait
        self.window_width = window_width
        self.window_height = window_height

    def create_driver(self, base_url: str | None = None):
        if self.browser == "chrome":
            driver = self._create_chrome()
        elif self.browser == "firefox":
            driver = self._create_firefox()
        else:
            raise ValueError(
                f"Unsupported browser: {self.browser}. "
                "Supported browsers: chrome, firefox."
            )

        self._configure_driver(driver)

        if base_url:
            driver.get(base_url)

        self.log.info(
            "WebDriver created: browser=%s headless=%s",
            self.browser,
            self.headless,
        )

        return driver

    # Backward-compatible method used by older framework code.
    def getWebDriverInstance(self, base_url: str):
        return self.create_driver(base_url)

    def _create_chrome(self):
        options = ChromeOptions()
        if self.headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        return webdriver.Chrome(
            service=ChromeService(),
            options=options,
        )

    def _create_firefox(self):
        options = FirefoxOptions()
        if self.headless:
            options.add_argument("-headless")
        options.set_preference(
            "dom.webnotifications.enabled",
            False,
        )

        return webdriver.Firefox(
            service=FirefoxService(),
            options=options,
        )

    def _configure_driver(self, driver) -> None:
        try:
            driver.set_window_size(
                self.window_width,
                self.window_height,
            )
        except Exception:
            driver.maximize_window()

        driver.implicitly_wait(self.implicit_wait)
