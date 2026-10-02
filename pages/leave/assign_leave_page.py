from __future__ import annotations

import time

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from components.dropdown import Dropdown
from pages.leave.leave_base_page import LeaveBasePage


class AssignLeavePage(LeaveBasePage):
    """Page Object for OrangeHRM Leave -> Assign Leave."""

    def __init__(self, driver):
        super().__init__(driver)
        self.dropdown = Dropdown(self)
    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    _assign_leave_tab = (
        "//a[normalize-space()='Assign Leave']"
    )

    # ------------------------------------------------------------------
    # Form locators
    # ------------------------------------------------------------------

    _employee = (
        "//label[normalize-space()='Employee Name']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input[@placeholder='Type for hints...']"
    )

    _employee_option = (
        "//div[@role='option']"
    )

    _leave_type = (
        "//label[normalize-space()='Leave Type']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text-input')]"
    )
    # _leave_type = (".oxd-select-text-input")

    _leave_type_option = (
        "//div[@role='option']"
    )

    _from_date = (
        "//label[normalize-space()='From Date']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    _to_date = (
        "//label[normalize-space()='To Date']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    _partial_days = (
        "//label[normalize-space()='Partial Days']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text-input')]"
    )

    _partial_days_option = (
        "//div[@role='option']"
    )

    _comments = (
        "//textarea[contains(@class,'oxd-textarea')]"
    )

    _assign_button = (
        "//button[normalize-space()='Assign']"
    )
    # ------------------------------------------------------------------
    # Confirmation modal
    # ------------------------------------------------------------------

    _confirmation_modal = (
        "//div[contains(@class,'oxd-dialog-container')]"
    )

    _confirm_ok_button = (
        "//button[normalize-space()='Ok']"
    )

    # ------------------------------------------------------------------
    # Feedback / loading
    # ------------------------------------------------------------------

    _form_loader = (
        "//div[contains(@class,'oxd-form-loader')]"
    )

    _success_toast = (
        "//div[contains(@class,'oxd-toast-content')]"
    )

    # ------------------------------------------------------------------
    # Navigation methods
    # ------------------------------------------------------------------

    def open_assign_leave(self) -> bool:
        """
        Navigate from the Leave module to the Assign Leave screen.
        """


        try:
            if not self.click(
                locator=self._assign_leave_tab,
                locator_type="xpath",
            ):
                return False

            return self.wait_for_element_invisible(
                locator=self._form_loader,
                locator_type="xpath",
                timeout=15,
            )

        except WebDriverException as exc:
            self.log.error(
                "Unable to open Assign Leave page: %s",
                exc,
            )
            return False

    # ------------------------------------------------------------------
    # Employee
    # ------------------------------------------------------------------

    def enter_employee(self, employee_name: str) -> bool:
        """
        Enter employee name and select the matching employee
        from the autocomplete list.
        """

        try:
            if not self.send_keys(
                locator=self._employee,
                text=employee_name,
                locator_type="xpath",
                clear_first=True,
            ):
                return False

            option = (
                f"//div[@role='option']"
                f"[normalize-space()='{employee_name}']"
            )

            return self.click(
                locator=option,
                locator_type="xpath",
            )

        except WebDriverException as exc:
            self.log.error(
                "Unable to select employee '%s': %s",
                employee_name,
                exc,
            )
            return False

    # ------------------------------------------------------------------
    # Leave Type
    # ------------------------------------------------------------------

    def select_leave_type(self, leave_type: str) -> bool:
        """
        Open Leave Type dropdown and select the requested leave type.
        """

        try:
            if not self.click(
                locator=self._leave_type,
                locator_type="css",
            ):
                return False

            option = (
                f"//div[@role='option']"
                f"[normalize-space()='{leave_type}']"
            )

            return self.click(
                locator=option,
                locator_type="xpath",
            )

        except WebDriverException as exc:
            self.log.error(
                "Unable to select leave type '%s': %s",
                leave_type,
                exc,
            )
            return False

    # ------------------------------------------------------------------
    # Dates
    # ------------------------------------------------------------------

    def enter_from_date(self, from_date: str) -> bool:
        """
        Enter the From Date.
        Expected format depends on the OrangeHRM instance.
        """

        try:
            element = self.wait_for_element_visible(
                locator=self._from_date,
                locator_type="xpath",
            )

            if element is None:
                return False

            element.click()
            element.send_keys(Keys.COMMAND, "a")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(from_date)

            return True

        except WebDriverException as exc:
            self.log.error(
                "Unable to enter From Date '%s': %s",
                from_date,
                exc,
            )
            return False

    def enter_to_date(self, to_date: str) -> bool:
        """
        Enter the To Date.
        Expected format depends on the OrangeHRM instance.
        """

        try:
            element = self.wait_for_element_visible(
                locator=self._to_date,
                locator_type="xpath",
            )

            if element is None:
                return False

            element.click()
            element.send_keys(Keys.COMMAND, "a")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(to_date)

            return True

        except WebDriverException as exc:
            self.log.error(
                "Unable to enter To Date '%s': %s",
                to_date,
                exc,
            )
            return False

    # ------------------------------------------------------------------
    # Partial Days
    # ------------------------------------------------------------------

    def select_partial_day(self, option: str) -> bool:
        """
        Select a Partial Days option.

        Examples:
            'Full Day'
            'Half Day - Morning'
            'Half Day - Evening'
        """

        try:
            if not self.click(
                locator=self._partial_days,
                locator_type="xpath",
            ):
                return False

            partial_day_option = (
                f"//div[@role='option']"
                f"[normalize-space()='{option}']"
            )

            return self.click(
                locator=partial_day_option,
                locator_type="xpath",
            )

        except WebDriverException as exc:
            self.log.error(
                "Unable to select partial day '%s': %s",
                option,
                exc,
            )
            return False

    # ------------------------------------------------------------------
    # Comments
    # ------------------------------------------------------------------

    def enter_comment(self, comment: str) -> bool:
        """
        Enter an optional comment.
        """

        try:
            return self.send_keys(
                locator=self._comments,
                text=comment,
                locator_type="xpath",
                clear_first=True,
            )

        except WebDriverException as exc:
            self.log.error(
                "Unable to enter leave comment: %s",
                exc,
            )
            return False

    # ------------------------------------------------------------------
    # Assign
    # ------------------------------------------------------------------

    def click_assign(self) -> bool:
        """
        Click the Assign button after the form is ready.
        """

        try:
            if not self.wait_for_element_invisible(
                locator=self._form_loader,
                locator_type="xpath",
                timeout=15,
            ):
                return False

            return self.click(
                locator=self._assign_button,
                locator_type="xpath",
            )

        except WebDriverException as exc:
            self.log.error(
                "Unable to click Assign button: %s",
                exc,
            )
            return False

    # ------------------------------------------------------------------
    # Verification
    # ------------------------------------------------------------------

    def verify_leave_assigned(self) -> bool:
        """
        Verify that OrangeHRM displayed a confirmation toast
        after assigning leave.
        """

        try:
            toast = self.wait_for_element_visible(
                locator=self._success_toast,
                locator_type="xpath",
                timeout=15,
            )

            if toast is None:
                return False

            message = toast.text.strip().lower()

            self.log.info(
                "Assign Leave confirmation message: %s",
                message,
            )

            return bool(message)

        except WebDriverException as exc:
            self.log.error(
                "Unable to verify Assign Leave confirmation: %s",
                exc,
            )
            return False

    def confirm_leave_assignment(self) -> bool:
        """
        Confirm the leave assignment from the confirmation modal.
        """

        try:
            modal = self.wait_for_element_visible(
                locator=self._confirmation_modal,
                locator_type="xpath",
                timeout=10,
            )

            if modal is None:
                return False

            return self.click(
                locator=self._confirm_ok_button,
                locator_type="xpath",
            )

        except WebDriverException as exc:
            self.log.error(
                "Unable to confirm leave assignment: %s",
                exc,
            )
            return False

    def print_leave_type_options(self) -> list[str]:
        print("\nLeave Type options:")
        return self.dropdown.get_options(
            dropdown_locator=self._leave_type,
        )

    def print_partial_day_options(self) -> list[str]:
        print("\nPartial Days options:")
        return self.dropdown.get_options(
            dropdown_locator=self._partial_days,
        )

    def print_leave_type_options(self) -> list[str]:
        print("\nLeave Type options:")

        options = self.dropdown.get_options(
            dropdown_locator=self._leave_type,
        )

        return options

    def select_leave_type(self, leave_type: str) -> bool:
        try:
            if not self.click(
                    locator=self._leave_type,
                    locator_type="xpath",
            ):
                return False

            print("Leave Type clicked - waiting 3 seconds...")
            time.sleep(3)

            option_locator = "//div[@role='option']"

            options = self.get_elements(
                locator=option_locator,
                locator_type="xpath",
            )

            print(f"Options currently in DOM: {len(options)}")

            for option in options:
                if option.is_displayed():
                    print(f"Visible option: {option.text.strip()}")

            for option in options:
                if (
                        option.is_displayed()
                        and option.text.strip() == leave_type
                ):
                    option.click()

                    self.log.info(
                        "Leave Type selected successfully: %s",
                        leave_type,
                    )
                    return True

            self.log.error(
                "Leave Type option not visible: %s",
                leave_type,
            )
            return False

        except WebDriverException as exc:
            self.log.error(
                "Unable to select leave type '%s': %s",
                leave_type,
                exc,
            )
            return False