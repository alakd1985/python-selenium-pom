from __future__ import annotations

from selenium.common.exceptions import WebDriverException

from base.base_page import BasePage


class MediShopShopPage(BasePage):

    _search_input = "//input[@id='header_search_input']"

    _add_to_cart_button = (
        "//button[normalize-space()='Add to cart']"
    )
    _cart_product = (
        "//*[contains(normalize-space(), 'Aspirin')]"
    )
    _shopping_cart = (
        "//a[contains(@aria-label,'Shopping cart')]"
        "//*[name()='svg']"
    )

    _cart_checkout_button = (
        "//button[@data-testid='cart_checkout_button']"
    )
    _remove_product_button = (
        "//button[starts-with(@data-testid, 'remove_')]"
    )
    def search_medicine(self, medicine: str) -> bool:
        try:
            if not self.send_keys(
                locator=self._search_input,
                text=medicine,
                locator_type="xpath",
                clear_first=True,
            ):
                return False

            element = self.wait_for_element_visible(
                locator=self._search_input,
                locator_type="xpath",
                timeout=10,
            )

            if element is None:
                return False

            element.send_keys("\n")
            return True

        except WebDriverException as exc:
            self.log.error(
                "Unable to search for medicine '%s': %s",
                medicine,
                exc,
            )
            return False

    def add_to_cart(self) -> bool:
        try:
            return self.click(
                locator=self._add_to_cart_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to add medicine to cart: %s",
                exc,
            )
            return False

    def click_cart(self) -> bool:
        try:
            return self.click(
                locator=self._shopping_cart,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to click shopping cart: %s",
                exc,
            )
            return False

    def is_product_in_cart(self, product: str) -> bool:
        try:
            locator = (
                f"//*[contains("
                f"translate(normalize-space(), "
                f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
                f"'abcdefghijklmnopqrstuvwxyz'), "
                f"'{product.lower()}')]"
            )

            element = self.wait_for_element_visible(
                locator=locator,
                locator_type="xpath",
                timeout=10,
            )

            return element is not None

        except WebDriverException as exc:
            self.log.error(
                "Unable to verify product '%s' in cart: %s",
                product,
                exc,
            )
            return False

    def click_secure_checkout(self) -> bool:
        try:
            return self.click(
                locator=self._cart_checkout_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to click Secure checkout: %s",
                exc,
            )
            return False

    def remove_product_from_cart(self) -> bool:
        return self.click(
            locator=self._remove_product_button,
            locator_type="xpath",
        )
