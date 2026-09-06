import os

import allure
import pytest
from base.webdriver_factory import WebDriverFactory
from utilities.screenshot import take_screenshot


# =========================================================
# CLI OPTIONS
# =========================================================

def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser: firefox or chrome",
    )

    parser.addoption(
        "--osType",
        action="store",
        default=None,
        help="Operating system",
    )


# =========================================================
# BROWSER
# =========================================================

@pytest.fixture(scope="session")
def browser(request):

    return request.config.getoption("--browser")


# =========================================================
# OS
# =========================================================

@pytest.fixture(scope="session")
def osType(request):

    return request.config.getoption("--osType")


# =========================================================
# BASE URL
# =========================================================

@pytest.fixture(scope="session")
def base_url():

    return (
        "https://opensource-demo.orangehrmlive.com/"
        "web/index.php/auth/login"
    )


# =========================================================
# WEBDRIVER
# =========================================================

@pytest.fixture(scope="function")
def driver(browser, base_url):

    print(
        f"[INFO] Creating WebDriver: {browser}"
    )

    wdf = WebDriverFactory(browser)

    driver = wdf.getWebDriverInstance(
        base_url
    )

    yield driver

    try:

        print("[INFO] Quitting WebDriver")

        driver.quit()

    except Exception as exc:

        print(
            f"[WARN] WebDriver quit failed: {exc}"
        )


# =========================================================
# CREATE DIRECTORIES
# =========================================================

def pytest_configure(config):

    os.makedirs(
        os.path.join(
            config.rootpath,
            "reports",
        ),
        exist_ok=True,
    )

    os.makedirs(
        os.path.join(
            config.rootpath,
            "screenshots",
        ),
        exist_ok=True,
    )


# =========================================================
# FAILURE SCREENSHOT + ALLURE ATTACHMENT
# =========================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when != "call":
        return

    if not report.failed:
        return

    driver_instance = item.funcargs.get("driver")

    if not driver_instance:
        return

    try:

        screenshot_path = take_screenshot(
            driver_instance,
            item.name,
        )

        print(
            f"[TEST FAILURE] "
            f"Screenshot saved: {screenshot_path}"
        )

        if (
            screenshot_path
            and os.path.exists(screenshot_path)
        ):

            allure.attach.file(
                screenshot_path,
                name=(
                    f"Failure Screenshot - "
                    f"{item.name}"
                ),
                attachment_type=(
                    allure.attachment_type.PNG
                ),
            )

    except Exception as exc:

        print(
            f"[WARN] Screenshot/Allure "
            f"attachment failed: {exc}"
        )