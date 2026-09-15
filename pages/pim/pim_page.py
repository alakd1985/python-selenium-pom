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

    _success_message = "//div[contains(., 'Successfully Saved')]"

    # =========================================================
    # Navigation
    # =========================================================

    def open_pim(self) -> bool:
        return self.click(
            locator=self._pim_menu,
            locator_type="xpath",
        )

    # =========================================================
    # Actions
    # =========================================================

    def click_add_button(self) -> bool:
        return self.click(
            locator=self._add_button,
            locator_type="xpath",
        )

    def enter_employee_details(
        self,
        first_name: str,
        last_name: str,
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

        return first_name_entered and last_name_entered

    def save_employee(self) -> bool:
        return self.click(
            locator=self._save_button,
            locator_type="xpath",
        )

    # =========================================================
    # Verification
    # =========================================================

    def wait_for_save_confirmation(self) -> bool:
        return self.is_element_visible(
            locator=self._success_message,
            locator_type="xpath",
        )
