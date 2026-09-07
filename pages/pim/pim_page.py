from base.base_page import BasePage


class PIMPage(BasePage):
    # =========================================================
    # Locators
    # =========================================================

    _pim_menu = (
        "//span[@class='oxd-text "
        "oxd-text--span "
        "oxd-main-menu-item--name']"
        "[normalize-space()='PIM']"
    )

    _add_button = "//button[normalize-space()='Add']"

    _first_name = (
        "//input[@placeholder='First Name']"
    )

    _last_name = (
        "//input[@placeholder='Last Name']"
    )

    _employee_id = (
        "//input[@class='oxd-input oxd-input--focus']"
    )

    _save_button = "//button[@type='submit']"

    _success_message = (
        "//div[contains(text(), 'Successfully Saved')]"
    )

    # =========================================================
    # Navigation
    # =========================================================

    def click_pim_menu(self):
        return self.click(
            locator=self._pim_menu,
            locator_type="xpath",
        )

    # =========================================================
    # Actions
    # =========================================================

    def click_add_button(self):
        return self.click(
            locator=self._add_button,
            locator_type="xpath",
        )

    def enter_employee_details(
            self,
            first_name,
            last_name

    ):
        self.send_keys(
            text=first_name,
            locator=self._first_name,
            locator_type="xpath",
        )

        self.send_keys(
            text=last_name,
            locator=self._last_name,
            locator_type="xpath",
        )

    def save_employee(self):
        return self.click(
            locator=self._save_button,
            locator_type="xpath",
        )

    # =========================================================
    # Verification
    # =========================================================

    def verify_employee_added(self):
        return self.is_element_visible(
            locator=self._success_message,
            locator_type="xpath",
        )
