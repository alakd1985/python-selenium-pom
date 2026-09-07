from pytest_bdd import when, then, parsers
from pages.pim.pim_page import PIMPage
from selenium.webdriver.common.by import By


@when("the user navigates to the PIM page")
def navigate_to_pim(driver):
    pim_menu = driver.find_element(By.XPATH,
                                   "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    pim_menu.click()


@when("the user clicks the Add Employee button")
def click_add_employee(driver):
    pim = PIMPage(driver)
    pim.click_add_button()


@when("the user enters employee details:")
def enter_employee_details(driver, datatable):

    pim = PIMPage(driver)

    # First row contains the column names
    headers = datatable[0]

    # Second row contains the actual values
    values = datatable[1]

    # Convert the table into a dictionary
    employee = dict(zip(headers, values))

    pim.enter_employee_details(
        first_name=employee["first_name"],
        last_name=employee["last_name"]
    )


@when("the user saves the employee record")
def save_employee(driver):
    pim = PIMPage(driver)
    pim.save_employee()


# @then("the employee should be added successfully")
# def verify_employee_added(driver):
#     pim = PIMPage(driver)
#     assert pim.verify_employee_added(), "Employee was not added"


