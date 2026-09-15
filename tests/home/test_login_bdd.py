import allure
from pytest_bdd import scenario
from step_definitions.login_steps import *  # noqa: F401,F403

FEATURE = "../../feature/login/login.feature"

@scenario(
    FEATURE,
    "Successful login with valid credentials",
)
@allure.feature("Login")
@allure.story("Valid Login")
@allure.title("Valid login should navigate to Dashboard")
def test_valid_login_bdd():
    pass


@scenario(
    FEATURE,
    "Login with invalid credentials",
)
@allure.feature("Login")
@allure.story("Invalid Credentials")
@allure.title("Login should fail with invalid credentials")
def test_invalid_login_bdd():
    pass


@scenario(
    FEATURE,
    "Login with empty username and password",
)
@allure.feature("Login")
@allure.story("Empty Fields")
@allure.title("Login should show required field validation")
def test_empty_credentials_login_bdd():
    pass
