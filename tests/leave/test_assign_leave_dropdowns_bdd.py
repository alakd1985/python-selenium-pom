import allure
from pytest_bdd import scenario

from step_definitions.login_steps import *  # noqa: F401,F403
from step_definitions.leave_steps import *  # noqa: F401,F403


FEATURE = "../../feature/leave/assign_leave_dropdowns.feature"


@scenario(
    FEATURE,
    "Print and select Leave Type",
)
@allure.feature("Leave")
@allure.story("Assign Leave Dropdowns")
@allure.title("Print and select Leave Type")
def test_assign_leave_dropdowns():
    pass