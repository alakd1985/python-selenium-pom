from selenium.webdriver import Keys

from base.base_page import BasePage


class PIMPage(BasePage):

    # =========================================================
    # Locators
    # =========================================================

    _pim_menu = (
        "//span[contains(@class,'oxd-main-menu-item--name') "
        "and normalize-space()='PIM']"
    )

    _add_button = "//button[normalize-space()='Add']"

    _first_name = "//input[@placeholder='First Name']"

    _last_name = "//input[@placeholder='Last Name']"

    _save_button = "//button[@type='submit']"
    _employee_id = (
        "//label[normalize-space()='Employee Id']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    # OrangeHRM form loading overlay
    _form_loader = "//div[contains(@class,'oxd-form-loader')]"

    # OrangeHRM toast notification
    _success_message = (
        "//div[contains(@class,'oxd-toast-content')]"
    )

    # =========================================================
    # Navigation
    # =========================================================

    def open_pim(self) -> bool:
        return self.click(
            locator=self._pim_menu,
            locator_type="xpath",
        )

    # =========================================================
    # Employee Actions
    # =========================================================

    def click_add_button(self) -> bool:

        if not self.click(
                locator=self._add_button,
                locator_type="xpath",
        ):
            return False

        return self.wait_for_element_invisible(
            locator=self._form_loader,
            locator_type="xpath",
            timeout=15,
        )

    def enter_employee_details(
            self,
            first_name: str,
            last_name: str,
            employee_id: str,
    ) -> bool:

        first_name_entered = self.send_keys(
            text=first_name,
            locator=self._first_name,
            locator_type="xpath",
        )

        last_name_entered = self.send_keys(
            text=last_name,
            locator=self._last_name,
            locator_type="xpath",
        )

        # Wait for OrangeHRM form loader to disappear
        if not self.wait_for_element_invisible(
                locator=self._form_loader,
                locator_type="xpath",
                timeout=15,
        ):
            self.log.error(
                "Form loader did not disappear before entering Employee ID"
            )
            return False

        employee_id_field = self.get_element(
            locator=self._employee_id,
            locator_type="xpath",
        )

        if employee_id_field is None:
            self.log.error("Employee ID field was not found")
            return False

        # OrangeHRM pre-populates Employee ID.
        # Select the existing value and delete it.
        employee_id_field.click()
        employee_id_field.send_keys(Keys.COMMAND, "a")
        employee_id_field.send_keys(Keys.BACKSPACE)

        # Enter our unique Employee ID
        employee_id_field.send_keys(employee_id)

        # Verify the actual value
        actual_employee_id = employee_id_field.get_attribute("value")

        self.log.info(
            "Expected Employee ID: %s | Actual Employee ID: %s",
            employee_id,
            actual_employee_id,
        )

        return (
                first_name_entered
                and last_name_entered
                and actual_employee_id == employee_id
        )
    def save_employee(self) -> bool:

        # Wait for OrangeHRM form loader to disappear
        if not self.wait_for_element_invisible(
            locator=self._form_loader,
            locator_type="xpath",
            timeout=15,
        ):
            self.log.error(
                "Form loader did not disappear before clicking Save"
            )
            return False

        # Click Save
        return self.click(
            locator=self._save_button,
            locator_type="xpath",
            timeout=15,
        )

    # =========================================================
    # Verification
    # =========================================================

    def verify_employee_saved(self) -> bool:

        return (
            self.wait_for_element_visible(
                locator=self._success_message,
                locator_type="xpath",
                timeout=15,
            )
            is not None
        )