
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

from base.base_page import BasePage


class MediShopPaymentMethodsPage(BasePage):
    # Page navigation
    _payment_methods_link = "//a[normalize-space()='Payment methods']"
    _page_heading = "//h1[normalize-space()='Payment methods']"
    _add_payment_method_button = (
        "//button[normalize-space()='Add payment method']"
    )
    _add_modal_heading = (
        "//h2[normalize-space()='Add payment method']"
    )

    # Add payment method form
    _payment_type = "//select[@id='pm_type_select']"
    _card_number = "//input[@data-testid='pm_card_number_input']"
    _card_expiry = "//input[@data-testid='pm_card_expiry_input']"
    _card_cvv = "//input[@data-testid='pm_card_cvv_input']"
    _card_name = "//input[@data-testid='pm_card_name_input']"
    _use_test_card = "//button[@data-testid='pm_use_test_card_button']"
    _upi_id = "//input[@data-testid='pm_upi_id_input']"
    _nickname = "//input[@data-testid='pm_nickname_input']"
    _default_checkbox = "//input[@id='pm_default_checkbox']"
    _save_button = "//button[@data-testid='payment_save_button']"
    _cancel_button = "//button[@data-testid='payment_cancel_button']"

    # Saved payment methods
    _payments_list = "//*[@id='payments_list']"
    _payments_empty = "//*[@id='payments_empty']"
    _empty_add_button = (
        "//button[@data-testid='empty_add_payment_button']"
    )
    _payment_card = "//*[@data-testid='payment_card_0']"
    _default_badge = "//*[@data-testid='payment_default_0']"
    _saved_card_label = "//*[@data-testid='payment_label_0']"
    _saved_card_holder = "//*[@data-testid='payment_holder_0']"
    _saved_card_nickname = "//*[@data-testid='payment_nickname_0']"
    _delete_card_button = (
        "//button[@data-testid='delete_payment_0']"
    )

    # Navigation methods
    def open_payment_methods(self) -> bool:
        try:
            return self.click(
                locator=self._payment_methods_link,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to open Payment methods: %s",
                exc,
            )
            return False

    def is_payment_methods_page_displayed(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._page_heading,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error(
                "Payment methods page not displayed: %s",
                exc,
            )
            return False

    def open_add_payment_method_modal(self) -> bool:
        try:
            return self.click(
                locator=self._add_payment_method_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to open Add payment method modal: %s",
                exc,
            )
            return False

    def is_add_payment_method_modal_displayed(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._add_modal_heading,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error(
                "Add payment method modal not displayed: %s",
                exc,
            )
            return False

    # Payment form methods
    def select_payment_type(self, payment_type: str) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._payment_type,
                locator_type="xpath",
                timeout=10,
            )
            if element is None:
                return False

            Select(element).select_by_visible_text(payment_type)
            return True
        except (WebDriverException, ValueError) as exc:
            self.log.error(
                "Unable to select payment type: %s",
                exc,
            )
            return False

    def use_demo_test_card(self) -> bool:
        try:
            return self.click(
                locator=self._use_test_card,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to fill demo card: %s",
                exc,
            )
            return False

    def enter_upi_id(self, upi_id: str) -> bool:
        try:
            return self.send_keys(
                locator=self._upi_id,
                text=upi_id,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to enter UPI ID: %s",
                exc,
            )
            return False

    def enter_nickname(self, nickname: str) -> bool:
        try:
            return self.send_keys(
                locator=self._nickname,
                text=nickname,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to enter nickname: %s",
                exc,
            )
            return False

    def set_default_payment_method(self, make_default: bool) -> bool:
        try:
            checkbox = self.wait_for_element_visible(
                locator=self._default_checkbox,
                locator_type="xpath",
                timeout=10,
            )
            if checkbox is None:
                return False

            if checkbox.is_selected() != make_default:
                checkbox.click()

            return checkbox.is_selected() == make_default
        except WebDriverException as exc:
            self.log.error(
                "Unable to set default payment method: %s",
                exc,
            )
            return False

    def save_payment_method(self) -> bool:
        try:
            return self.click(
                locator=self._save_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to save payment method: %s",
                exc,
            )
            return False

    # Saved payment method verification
    def is_saved_card_displayed(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._payment_card,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error(
                "Saved card not displayed: %s",
                exc,
            )
            return False

    def is_default_badge_displayed(self) -> bool:
        try:
            elements = self.driver.find_elements(
                "xpath",
                self._default_badge,
            )
            return any(
                element.is_displayed()
                for element in elements
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to verify default badge: %s",
                exc,
            )
            return False

    def delete_saved_card(self) -> bool:
        try:
            return self.click(
                locator=self._delete_card_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to delete saved card: %s",
                exc,
            )
            return False

    def is_empty_state_displayed(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._payments_empty,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error(
                "Empty payment methods state not displayed: %s",
                exc,
            )
            return False
