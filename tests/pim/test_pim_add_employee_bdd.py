import allure

from pytest_bdd import scenario

from step_definitions.login_steps import *  # noqa: F401,F403
from step_definitions.pim_steps import *    # noqa: F401,F403


FEATURE = "../../feature/pim/pim_add_employee.feature"


@scenario(
    FEATURE,
    "Add a new employee",
)
@allure.feature("PIM")
@allure.story("Add Employee")
@allure.title("Add Employee via PIM module")
def test_pim_add_employee():
    pass