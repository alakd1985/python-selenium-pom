
from selenium.common.exceptions import WebDriverException

from base.base_page import BasePage


class MediShopOrderDetailsPage(BasePage):
    # Order details actions
    _track_order_button = "//a[@data-testid='track_order_button']"
    _print_invoice_button = "//button[@data-testid='print_invoice_button']"

    # Tracking section
    _tracking_heading = "//*[normalize-space()='Tracking']"

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
        """Intercept window.print so the native dialog does not block Selenium."""
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
