from __future__ import annotations

import platform
from pathlib import Path

import allure
import pytest

from base.webdriver_factory import WebDriverFactory
from configuration.config import load_settings
from utilities.allure_helper import (
    attach_screenshot,
)
from utilities.custom_logger import customLogger

pytest_plugins = [
    "step_definitions.medishop_login_steps",
    "step_definitions.medishop_shop_steps",
    "step_definitions.medishop_checkout_steps",
    "step_definitions.medishop_negative_login_steps",
    "step_definitions.medishop_search_steps",
    "step_definitions.medishop_cart_steps",
    "step_definitions.medishop_checkout_validation_steps",
    "step_definitions.medishop_logout_steps",
    "step_definitions.medishop_prescription_steps",
]

PROJECT_ROOT = Path(__file__).resolve().parent
REPORT_DIR = PROJECT_ROOT / "reports"
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
log = customLogger()


# =============================================================
# CLI OPTIONS
# =============================================================


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser: chrome or firefox",
    )

    parser.addoption(
        "--env",
        action="store",
        default=None,
        help="Test environment: dev, qa, or prod",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )

    # Backward compatibility with the original framework.
    parser.addoption(
        "--osType",
        action="store",
        default=None,
        help="Execution OS label used by the original framework",
    )


# =============================================================
# SESSION FIXTURES
# =============================================================


@pytest.fixture(scope="session")
def settings(request):
    settings = load_settings(
        request.config.getoption("--env")
    )

    cli_browser = request.config.getoption("--browser")
    cli_headless = request.config.getoption("--headless")
    cli_os = request.config.getoption("--osType")

    if cli_browser:
        settings = settings.__class__(
            **{
                **settings.__dict__,
                "browser": cli_browser.lower(),
            }
        )

    if cli_headless:
        settings = settings.__class__(
            **{
                **settings.__dict__,
                "headless": True,
            }
        )

    if cli_os:
        settings = settings.__class__(
            **{
                **settings.__dict__,
                "os_type": cli_os,
            }
        )

    return settings


@pytest.fixture(scope="session")
def browser(settings):
    return settings.browser


@pytest.fixture(scope="session")
def osType(settings):
    return settings.os_type


@pytest.fixture(scope="session")
def base_url(settings):
    return settings.base_url





# =============================================================
# DRIVER FIXTURE
# =============================================================


@pytest.fixture
def driver(settings, base_url):
    factory = WebDriverFactory(
        browser=settings.browser,
        headless=settings.headless,
        implicit_wait=settings.implicit_wait,
        window_width=settings.window_width,
        window_height=settings.window_height,
    )

    web_driver = factory.create_driver()

    yield web_driver

    try:
        web_driver.quit()
        log.info("WebDriver closed successfully")
    except Exception as exc:  # noqa: BLE001
        log.error("Failed to close WebDriver: %s", exc)

# =============================================================
# PYTEST CONFIGURATION
# =============================================================


def pytest_configure(config):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    settings = load_settings(config.getoption("--env"))

    if config.getoption("--browser"):
        browser = config.getoption("--browser")
    else:
        browser = settings.browser

    lines = [
        f"Environment={settings.environment}",
        f"Browser={browser}",
        f"Headless={settings.headless}",
        f"OS={platform.system()}",
        f"Python={platform.python_version()}",
        f"BaseURL={settings.base_url}",
    ]

    environment_file = REPORT_DIR / "environment.properties"
    environment_file.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    # Allure reads environment.properties from its results directory.
    allure_results_dir = getattr(
        config.option, "allure_report_dir", None
    )

    if allure_results_dir:
        allure_dir = Path(allure_results_dir)
        allure_dir.mkdir(parents=True, exist_ok=True)
        (allure_dir / "environment.properties").write_text(
            "\n".join(lines),
            encoding="utf-8",
        )


# =============================================================
# FAILURE ARTIFACTS
# =============================================================


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    log.error("Test failed: %s", item.name)

    try:
        driver = item._request.getfixturevalue("driver")
    except Exception as exc:  # noqa: BLE001
        log.error("Unable to get driver fixture: %s", exc)
        return

    if driver is None:
        log.error("Driver fixture returned None")
        return

    test_name = (
        item.name
        .replace("/", "_")
        .replace(" ", "_")
    )

    screenshot_path = SCREENSHOT_DIR / f"{test_name}.png"

    # Screenshot
    try:
        if driver.save_screenshot(str(screenshot_path)):
            attach_screenshot(
                str(screenshot_path),
                name="Failure Screenshot",
            )
            log.info(
                "Failure screenshot attached: %s",
                screenshot_path,
            )
    except Exception as exc:  # noqa: BLE001
        log.error("Unable to capture failure screenshot: %s", exc)

    # Page source
    try:
        allure.attach(
            driver.page_source,
            name="Failure Page Source",
            attachment_type=allure.attachment_type.HTML,
        )
        log.info("Failure page source attached")
    except Exception as exc:  # noqa: BLE001
        log.error(
            "Unable to attach failure page source: %s",
            exc,
        )

    # Current URL
    try:
        allure.attach(
            driver.current_url,
            name="Failure URL",
            attachment_type=allure.attachment_type.TEXT,
        )
        log.info("Failure URL attached")
    except Exception as exc:  # noqa: BLE001
        log.error(
            "Unable to attach failure URL: %s",
            exc,
        )