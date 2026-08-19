import pytest
from base.webdriver_factory import WebDriverFactory


# ---------------------------------------------------------
# PyTest CLI Options
# ---------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser to run tests on: firefox or chrome")
    parser.addoption("--osType", help="Type of operating system")


# ---------------------------------------------------------
# Fixtures: browser + osType
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser") or "firefox"


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
# WebDriver Fixture (uses WebDriverFactory)
# ---------------------------------------------------------
@pytest.fixture(scope="function")
def driver(request, browser, base_url):
    print("[INFO] Creating WebDriver using WebDriverFactory")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance(base_url)

    # Attach driver to test class if using @pytest.mark.usefixtures
    if request.cls is not None:
        request.cls.driver = driver

    # Yield control to the test
    yield driver

    # GUARANTEED teardown — even if soft assertions throw errors
    try:
        print("[INFO] Quitting WebDriver")
        driver.quit()
    except Exception as e:
        print(f"[WARN] WebDriver quit failed: {e}")
