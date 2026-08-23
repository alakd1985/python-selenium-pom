import pytest
from base.webdriver_factory import WebDriverFactory
from utilities.screenshot import take_screenshot


# ---------------------------------------------------------
# PyTest CLI Options
# ---------------------------------------------------------

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser to run tests on: firefox or chrome"
    )

    parser.addoption(
        "--osType",
        action="store",
        default=None,
        help="Type of operating system"
    )


# ---------------------------------------------------------
# Browser Fixture
# ---------------------------------------------------------

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# ---------------------------------------------------------
# OS Fixture
# ---------------------------------------------------------

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


# ---------------------------------------------------------
# Base URL Fixture
# ---------------------------------------------------------

@pytest.fixture(scope="session")
def base_url():
    return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


# ---------------------------------------------------------
# WebDriver Fixture
# ---------------------------------------------------------

@pytest.fixture(scope="function")
def driver(request, browser, base_url):

    print("[INFO] Creating WebDriver using WebDriverFactory")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance(base_url)

    # Attach driver to TestLogin
    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    # WebDriver teardown
    try:
        print("[INFO] Quitting WebDriver")
        driver.quit()
    except Exception as e:
        print(f"[WARN] WebDriver quit failed: {e}")


# =========================================================
# Screenshot on Test Failure
# =========================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            path = take_screenshot(driver, item.name)

            print(
                f"[TEST FAILURE] Screenshot saved: {path}"
            )