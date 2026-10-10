from selenium.common.exceptions import WebDriverException

from base.base_page import BasePage


class MediShopPaymentMethodsPage(BasePage):
    _payment_methods_link = (
        "//a[normalize-space()='Payment methods']"
    )
    _page_heading = (
        "//h1[normalize-space()='Payment methods']"
    )
    _add_payment_method_button = (
        "//button[normalize-space()='Add payment method']"
    )
    _add_modal_heading = (
        "//h2[normalize-space()='Add payment method']"
    )

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
