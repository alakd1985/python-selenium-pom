from pytest_bdd import when, then
from pytest_bdd import when, then, parsers
from pages.leave.assign_leave_page import AssignLeavePage


@when("the user navigates to the Leave page")
def user_navigates_to_leave(driver):
    leave_page = AssignLeavePage(driver)

    assert leave_page.open_leave(), (
        "Unable to navigate to the Leave page"
    )


@when("the user navigates to Assign Leave")
def user_navigates_to_assign_leave(driver):
    assign_leave_page = AssignLeavePage(driver)

    assert assign_leave_page.open_assign_leave(), (
        "Unable to navigate to Assign Leave"
    )


@when("the user assigns leave with the following details")
def user_assigns_leave(driver, datatable, data_reader):
    assign_leave_page = AssignLeavePage(driver)

    leave_data = data_reader.table_to_dict(datatable)

    data_reader.validate_required_fields(
        leave_data,
        {
            "employee",
            "leave_type",
            "from_date",
            "to_date",
        },
    )

    assert assign_leave_page.enter_employee(
        leave_data["employee"]
    ), (
        f"Unable to select employee: "
        f"{leave_data['employee']}"
    )

    assert assign_leave_page.select_leave_type(
        leave_data["leave_type"]
    ), (
        f"Unable to select leave type: "
        f"{leave_data['leave_type']}"
    )

    assert assign_leave_page.enter_from_date(
        leave_data["from_date"]
    ), (
        f"Unable to enter From Date: "
        f"{leave_data['from_date']}"
    )

    assert assign_leave_page.enter_to_date(
        leave_data["to_date"]
    ), (
        f"Unable to enter To Date: "
        f"{leave_data['to_date']}"
    )

    comment = leave_data.get("comment", "").strip()

    if comment:
        assert assign_leave_page.enter_comment(comment), (
            "Unable to enter leave comment"
        )


@when("the user clicks the Assign button")
def user_clicks_assign_button(driver):
    assign_leave_page = AssignLeavePage(driver)

    assert assign_leave_page.click_assign(), (
        "Unable to click Assign button"
    )


@when("the user confirms the leave assignment")
def user_confirms_leave_assignment(driver):
    assign_leave_page = AssignLeavePage(driver)

    assert assign_leave_page.confirm_leave_assignment(), (
        "Unable to confirm leave assignment"
    )


@then("the leave should be assigned successfully")
def leave_should_be_assigned_successfully(driver):
    assign_leave_page = AssignLeavePage(driver)

    assert assign_leave_page.verify_leave_assigned(), (
        "Leave was not assigned successfully"
    )


@when("the user prints the Assign Leave dropdown options")
def user_prints_assign_leave_dropdown_options(driver):
    assign_leave_page = AssignLeavePage(driver)

    options = assign_leave_page.print_leave_type_options()

    assert options, "No Leave Type options were found"

@when(parsers.parse('the user selects employee "{employee_name}"'))
def user_selects_employee(driver, employee_name):
    assign_leave_page = AssignLeavePage(driver)

    assert assign_leave_page.enter_employee(
        employee_name
    ), (
        f"Unable to select employee: {employee_name}"
    )
@when(parsers.parse('the user selects leave type "{leave_type}"'))
def user_selects_leave_type(driver, leave_type):
    assign_leave_page = AssignLeavePage(driver)

    assert assign_leave_page.select_leave_type(
        leave_type
    ), (
        f"Unable to select leave type: {leave_type}"
    )

@when("the user enters the leave dates")
def user_enters_leave_dates(driver, datatable, data_reader):
    assign_leave_page = AssignLeavePage(driver)

    leave_data = data_reader.table_to_dict(datatable)

    data_reader.validate_required_fields(
        leave_data,
        {"from_date", "to_date"},
    )

    assert assign_leave_page.enter_from_date(
        leave_data["from_date"]
    ), (
        f"Unable to enter From Date: "
        f"{leave_data['from_date']}"
    )

    assert assign_leave_page.enter_to_date(
        leave_data["to_date"]
    ), (
        f"Unable to enter To Date: "
        f"{leave_data['to_date']}"
    )
@when("the user prints the Partial Days dropdown options")
def user_prints_partial_days_options(driver):
    assign_leave_page = AssignLeavePage(driver)

    options = assign_leave_page.print_partial_day_options()

    assert options, (
        "Partial Days dropdown returned no options"
    )