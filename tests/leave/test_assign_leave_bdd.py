import allure
from pytest_bdd import scenario

from step_definitions.login_steps import *  # noqa: F401,F403
from step_definitions.leave_steps import *  # noqa: F401,F403


FEATURE = "../../feature/leave/assign_leave.feature"


@scenario(
    FEATURE,
    "Assign leave to an employee",
)
@allure.feature("Leave")
@allure.story("Assign Leave")
@allure.title("Assign leave to an employee")
def test_assign_leave():
    pass