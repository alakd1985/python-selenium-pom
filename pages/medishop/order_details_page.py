from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

from base.base_page import BasePage


class MediShopOrderDetailsPage(BasePage):
    # Order details actions
    _track_order_button = "//a[@data-testid='track_order_button']"
    _print_invoice_button = "//button[@data-testid='print_invoice_button']"
    _cancel_order_button = "//button[@data-testid='cancel_order_button']"

    # Tracking section
    _tracking_heading = "//*[normalize-space()='Tracking']"

    # Cancellation dialog
    _cancel_dialog = "//dialog[@data-testid='cancel_order_dialog']"

    _cancel_reason_select = (
        "//dialog[@data-testid='cancel_order_dialog']"
        "//select[@data-testid='cancel_reason_select']"
    )

    _confirm_cancel_button = (
        "//dialog[@data-testid='cancel_order_dialog']"
        "//button[@data-testid='cancel_dialog_confirm_button']"
    )

    _keep_order_button = (
        "//dialog[@data-testid='cancel_order_dialog']"
        "//button[@data-testid='cancel_dialog_keep_button']"
    )

    _cancelled_status = (
        "//*[contains(translate(normalize-space(.), "
        "'abcdefghijklmnopqrstuvwxyz', "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'CANCELLED')]"
    )

    _cancellation_message = (
        "//*[contains(normalize-space(.), "
        "'This order was cancelled')]"
    )

    def open_order_tracking(self) -> bool:
        try:
            return self.click(
                locator=self._track_order_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error("Unable to open order tracking: %s", exc)
            return False

    def is_order_tracking_displayed(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._tracking_heading,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error("Order tracking section not displayed: %s", exc)
            return False

    def prepare_print_intercept(self) -> bool:
        """Intercept window.print so Selenium is not blocked by the native dialog."""
        try:
            self.driver.execute_script(
                """
                window.__seleniumPrintCalled = false;
                window.print = function () {
                    window.__seleniumPrintCalled = true;
                };
                """
            )
            return True
        except WebDriverException as exc:
            self.log.error("Unable to prepare print interception: %s", exc)
            return False

    def open_invoice_print_dialog(self) -> bool:
        try:
            return self.click(
                locator=self._print_invoice_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error("Unable to trigger invoice printing: %s", exc)
            return False

    def was_print_triggered(self) -> bool:
        try:
            return bool(
                self.driver.execute_script(
                    "return window.__seleniumPrintCalled === true;"
                )
            )
        except WebDriverException as exc:
            self.log.error("Unable to verify invoice print action: %s", exc)
            return False

    def open_cancel_order_dialog(self) -> bool:
        try:
            return self.click(
                locator=self._cancel_order_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error("Unable to open cancellation dialog: %s", exc)
            return False

    def is_cancel_order_dialog_displayed(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._cancel_dialog,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error("Cancellation dialog not displayed: %s", exc)
            return False

    def select_cancellation_reason(self, reason: str) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._cancel_reason_select,
                locator_type="xpath",
                timeout=10,
            )
            if element is None:
                return False

            Select(element).select_by_visible_text(reason)
            return True
        except (WebDriverException, ValueError) as exc:
            self.log.error("Unable to select cancellation reason: %s", exc)
            return False

    def keep_order(self) -> bool:
        try:
            return self.click(
                locator=self._keep_order_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error("Unable to keep order: %s", exc)
            return False

    def confirm_cancel_order(self) -> bool:
        try:
            return self.click(
                locator=self._confirm_cancel_button,
                locator_type="xpath",
                timeout=10,
            )
        except WebDriverException as exc:
            self.log.error("Unable to confirm cancellation: %s", exc)
            return False

    def is_order_cancelled(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._cancelled_status,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error("Cancelled status not displayed: %s", exc)
            return False

    def get_cancellation_message(self) -> str:
        try:
            element = self.wait_for_element_visible(
                locator=self._cancellation_message,
                locator_type="xpath",
                timeout=10,
            )
            return element.text.strip() if element else ""
        except WebDriverException as exc:
            self.log.error(
                "Unable to read cancellation message: %s", exc
            )
            return ""

    def is_cancel_order_dialog_closed(self) -> bool:
        try:
            element = self.wait_for_element_invisible(
                locator=self._cancel_dialog,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error("Cancellation dialog did not close: %s", exc)
            return False
