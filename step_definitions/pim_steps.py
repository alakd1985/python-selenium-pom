from pytest_bdd import then, when, parsers

from pages.pim.pim_page import PIMPage


@when("the user navigates to the PIM page")
def navigate_to_pim(driver):
    pim = PIMPage(driver)

    assert pim.open_pim(), (
        "Unable to navigate to the PIM page"
    )


@when("the user clicks the Add Employee button")
def click_add_employee(driver):
    pim = PIMPage(driver)

    assert pim.click_add_button(), (
        "Unable to click the Add Employee button"
    )


@when(
    parsers.parse(
        'the user enters employee data for "{employee_key}"'
    )
)
def enter_employee_data(driver, employee_key, data_reader):
    employee = data_reader.get_record(
        "employees.json",
        employee_key,
    )

    data_reader.validate_required_fields(
        employee,
        {"first_name", "last_name"},
    )

    pim = PIMPage(driver)

    assert pim.enter_employee_details(
        first_name=employee["first_name"],
        last_name=employee["last_name"],
    ), "Unable to enter employee details"


@when("the user enters employee details:")
def enter_employee_details_from_table(
    driver,
    datatable,
    data_reader,
):
    employee = data_reader.table_to_dict(datatable)

    data_reader.validate_required_fields(
        employee,
        {"first_name", "last_name"},
    )

    pim = PIMPage(driver)

    assert pim.enter_employee_details(
        first_name=employee["first_name"],
        last_name=employee["last_name"],
    ), "Unable to enter employee details"


@when("the user saves the employee record")
def save_employee(driver):
    pim = PIMPage(driver)

    assert pim.save_employee(), (
        "Unable to save employee record"
    )


@then("the employee should be added successfully")
def verify_employee_added(driver):
    pim = PIMPage(driver)

    assert pim.wait_for_save_confirmation(), (
        "Employee was not added successfully"
    )
