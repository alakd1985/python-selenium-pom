
from __future__ import annotations

from selenium.common.exceptions import (
    NoSuchElementException,
    WebDriverException,
)
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class MediShopShopPage(BasePage):
    # =========================================================
    # LOCATORS: SEARCH
    # =========================================================
    _search_input = "//input[@id='header_search_input']"

    # =========================================================
    # LOCATORS: PRODUCTS
    # =========================================================
    _product_link_template = (
        "//a[normalize-space()='{product}']"
    )
    _product_card_template = (
        _product_link_template
        + "/ancestor::article[1]"
    )
    _salbutamol_add_to_cart = "//article[1]//div[3]//button[1]"

    _add_to_cart_button = (
        "//button[normalize-space()='Add to cart']"
    )
    _product_add_button_template = (
        _product_card_template
        + "//button[normalize-space()='Add to cart']"
    )

    # =========================================================
    # LOCATORS: CART
    # =========================================================
    _shopping_cart = (
        "//a[contains(@aria-label, 'Shopping cart')]"
    )
    _cart_checkout_button = (
        "//button[@data-testid='cart_checkout_button']"
    )
    _remove_product_button = (
        "//button[starts-with(@data-testid, 'remove_')]"
    )
    _clear_cart_button = (
        "//button[@data-testid='clear_cart_button']"
    )

    # =========================================================
    # LOCATORS: QUANTITY
    # =========================================================
    _increase_quantity_button = (
        "//button[starts-with(@data-testid, 'increase_')]"
    )
    _decrease_quantity_button = (
        "//button[starts-with(@data-testid, 'decrease_')]"
    )
    _quantity_display = (
        "//button[starts-with(@data-testid, 'increase_')]"
        "/preceding-sibling::*[self::span or self::input]"
    )

    # =========================================================
    # LOCATORS: NAVIGATION
    # =========================================================
    _continue_shopping_button = (
        "//a[normalize-space()='Continue shopping']"
    )
    _browse_medicines_button = (
        "//a[contains(@class, 'btn-primary') "
        "and contains(@class, 'btn-lg')]"
    )

    # =========================================================
    # LOCATORS: FILTERS
    # =========================================================
    _prescription_only = (
        "//span[normalize-space()='Prescription only']"
    )

    # =========================================================
    # SEARCH METHODS
    # =========================================================
    def search_medicine(self, medicine: str) -> bool:
        try:
            if not self.send_keys(
                locator=self._search_input,
                text=medicine,
                locator_type="xpath",
                clear_first=True,
            ):
                return False

            search_element = self.wait_for_element_visible(
                locator=self._search_input,
                locator_type="xpath",
                timeout=10,
            )

            if search_element is None:
                return False

            search_element.send_keys("\n")
            return True

        except WebDriverException as exc:
            self.log.error(
                "Unable to search for medicine '%s': %s",
                medicine,
                exc,
            )
            return False

    # =========================================================
    # PRODUCT METHODS
    # =========================================================
    def add_to_cart(self) -> bool:
        """Add the first available matching Add to cart button."""
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

    def add_product_to_cart(self, product: str) -> bool:
        """Add a specific product using its product card."""
        try:
            product_locator = (
                self._product_link_template.format(
                    product=product
                )
            )

            product_element = self.wait_for_element_visible(
                locator=product_locator,
                locator_type="xpath",
                timeout=10,
            )

            if product_element is None:
                self.log.error(
                    "Product not found: %s",
                    product,
                )
                return False

            product_card = product_element.find_element(
                By.XPATH,
                "./ancestor::article[1]",
            )

            add_button = product_card.find_element(
                By.XPATH,
                ".//button[normalize-space()='Add to cart']",
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                add_button,
            )

            add_button.click()

            self.log.info(
                "Added product to cart: %s",
                product,
            )
            return True

        except NoSuchElementException as exc:
            self.log.error(
                "Product card or Add to cart button not found "
                "for '%s': %s",
                product,
                exc,
            )
            return False

        except WebDriverException as exc:
            self.log.error(
                "Unable to add product '%s' to cart: %s",
                product,
                exc,
            )
            return False

    def is_product_in_cart(self, product: str) -> bool:
        """Verify a product is present in the shopping cart."""
        try:
            body = self.wait_for_element_visible(
                locator="//body",
                locator_type="xpath",
                timeout=10,
            )

            if body is None:
                self.log.error("Page body was not available.")
                return False

            page_text = body.text.casefold()

            if "your cart is empty" in page_text:
                return False

            is_present = product.casefold() in page_text

            if not is_present:
                self.log.error(
                    "Product '%s' was not found in the cart.",
                    product,
                )

            return is_present

        except WebDriverException as exc:
            self.log.error(
                "Unable to verify product '%s' in cart: %s",
                product,
                exc,
            )
            return False

    @staticmethod
    def _xpath_literal(value: str) -> str:
        """Safely represent a string as an XPath 1.0 literal."""
        if "'" not in value:
            return f"'{value}'"

        if '"' not in value:
            return f'"{value}"'

        parts = value.split("'")
        expressions = []

        for index, part in enumerate(parts):
            if part:
                expressions.append(f"'{part}'")

            if index < len(parts) - 1:
                expressions.append('"\'"')

        return f"concat({', '.join(expressions)})"

    # =========================================================
    # CART METHODS
    # =========================================================
    def click_cart(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._shopping_cart,
                locator_type="xpath",
            )

            if element is None:
                return False

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element,
            )

            self.driver.execute_script(
                "arguments[0].click();",
                element,
            )

            return True

        except WebDriverException as exc:
            self.log.error(
                "Unable to click shopping cart: %s",
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

    def click_checkout(self) -> bool:
        return self.click_secure_checkout()

    def remove_product_from_cart(self) -> bool:
        return self.click(
            locator=self._remove_product_button,
            locator_type="xpath",
        )

    def clear_cart(self) -> bool:
        return self.click(
            locator=self._clear_cart_button,
            locator_type="xpath",
        )

    # =========================================================
    # QUANTITY METHODS
    # =========================================================
    def increase_product_quantity(self) -> bool:
        return self.click(
            locator=self._increase_quantity_button,
            locator_type="xpath",
        )

    def decrease_product_quantity(self) -> bool:
        return self.click(
            locator=self._decrease_quantity_button,
            locator_type="xpath",
        )

    def get_product_quantity(self) -> str | None:
        try:
            quantity_element = self.wait_for_element_visible(
                locator=self._quantity_display,
                locator_type="xpath",
                timeout=10,
            )

            if quantity_element is None:
                return None

            return (
                quantity_element.get_attribute("value")
                or quantity_element.text
            ).strip()

        except WebDriverException as exc:
            self.log.error(
                "Unable to read product quantity: %s",
                exc,
            )
            return None

    # =========================================================
    # NAVIGATION METHODS
    # =========================================================
    def continue_shopping(self) -> bool:
        return self.click(
            locator=self._continue_shopping_button,
            locator_type="xpath",
        )

    def click_browse_medicines(self) -> bool:
        return self.click(
            locator=self._browse_medicines_button,
            locator_type="xpath",
        )

    def add_salbutamol_to_cart(self) -> bool:
        """Add Salbutamol to the shopping cart."""
        try:
            return self.click(
                locator=self._salbutamol_add_to_cart,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to add Salbutamol to cart: %s",
                exc,
            )
            return False

    # =========================================================
    # FILTER METHODS
    # =========================================================
    def select_prescription_only(self) -> bool:
        try:
            return self.click(
                locator=self._prescription_only,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to select Prescription only filter: %s",
                exc,
            )
            return False

    def are_prescription_medicines_displayed(self) -> bool:
        """Verify prescription-required medicines appear after filtering."""
        try:
            grid = self._wait(
                lambda driver: (
                    element
                    if (
                            (element := driver.find_element(By.ID, "product_grid"))
                            .get_attribute("aria-busy") == "false"
                    )
                    else False
                ),
                timeout=30,
            )

            product_cards = grid.find_elements(
                By.CSS_SELECTOR,
                "[data-testid^='product_card_']",
            )

            prescription_cards = [
                card
                for card in product_cards
                if card.find_elements(
                    By.CSS_SELECTOR,
                    ".badge.badge-rx",
                )
            ]

            self.log.info(
                "Loaded product cards: %s; prescription-required cards: %s",
                len(product_cards),
                len(prescription_cards),
            )

            return bool(product_cards) and len(prescription_cards) == len(product_cards)

        except WebDriverException as exc:
            self.log.error(
                "Unable to verify prescription-required medicines: %s",
                exc,
            )
            return False
