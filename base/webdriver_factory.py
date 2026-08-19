import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser.lower()

    def getWebDriverInstance(self, base_url):
        """
        Create WebDriver instance based on browser type.
        """

        driver = None

        if self.browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService())
            print("[INFO] Starting Chrome WebDriver")

        elif self.browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService())
            print("[INFO] Starting Firefox WebDriver")

        else:
            print(f"[WARN] Browser '{self.browser}' not recognized. Defaulting to Firefox.")
            driver = webdriver.Firefox(service=FirefoxService())

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        return driver
