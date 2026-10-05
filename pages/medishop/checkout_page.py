
from __future__ import annotations

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

from base.base_page import BasePage


class MediShopCheckoutPage(BasePage):

    _name = "//input[@id='checkout_name_input']"
    _mobile = "//input[@id='checkout_mobile_input']"
    _house = "//input[@id='checkout_house_input']"
    _city = "//input[@id='checkout_city_input']"
    _state = "//input[@id='checkout_state_input']"
    _pincode = "//input[@id='checkout_pincode_input']"
    _country = "//select[@id='checkout_country_select']"
    _delivery_notes = "//textarea[@id='checkout_notes_input']"

    _cash_on_delivery = (
        "//strong[normalize-space()='Cash on delivery']"
    )

    _place_order = (
        "//button[@type='submit'][normalize-space()='Place order'][1]"
    )
    _terms_checkbox = (
        "//span[contains(text(),"
        "'I confirm the prescription details are accurate an')]"
    )
    _order_confirmation = (
        "//h1[@data-testid='confirmation_heading']"
    )
    _order_id = "//strong[@class='mono']"

    _payment_method = "//dd[@data-testid='confirmation_payment']"
    _card_number = "//input[@id='card_number_input']"
    _card_expiry = "//input[@id='card_expiry_input']"
    _card_cvv = "//input[@id='card_cvv_input']"
    _card_name = "//input[@id='card_name_input']"
    _card_payment_method = (
        "//span[normalize-space()='Secure gateway · Visa, Mastercard, Amex']"
    )

    def enter_name(self, name: str) -> bool:
        try:
            return self.send_keys(
                locator=self._name,
                text=name,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error("Unable to enter name: %s", exc)
            return False

    def enter_mobile(self, mobile: str) -> bool:
        try:
            return self.send_keys(
                locator=self._mobile,
                text=mobile,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error("Unable to enter mobile number: %s", exc)
            return False

    def enter_house(self, house: str) -> bool:
        try:
            return self.send_keys(
                locator=self._house,
                text=house,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error("Unable to enter address: %s", exc)
            return False

    def enter_city(self, city: str) -> bool:
        try:
            return self.send_keys(
                locator=self._city,
                text=city,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error("Unable to enter city: %s", exc)
            return False

    def enter_state(self, state: str) -> bool:
        try:
            return self.send_keys(
                locator=self._state,
                text=state,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error("Unable to enter state: %s", exc)
            return False

    def enter_pincode(self, pincode: str) -> bool:
        try:
            return self.send_keys(
                locator=self._pincode,
                text=pincode,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error("Unable to enter pincode: %s", exc)
            return False

    def select_country(self, country: str) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._country,
                locator_type="xpath",
                timeout=10,
            )

            if element is None:
                return False

            Select(element).select_by_visible_text(country)

            self.log.info(
                "Country selected successfully: %s",
                country,
            )
            return True

        except WebDriverException as exc:
            self.log.error(
                "Unable to select country '%s': %s",
                country,
                exc,
            )
            return False

    def enter_delivery_notes(self, notes: str) -> bool:
        try:
            return self.send_keys(
                locator=self._delivery_notes,
                text=notes,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to enter delivery notes: %s",
                exc,
            )
            return False

    def select_cash_on_delivery(self) -> bool:
        try:
            return self.click(
                locator=self._cash_on_delivery,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to select Cash on delivery: %s",
                exc,
            )
            return False

    def click_place_order(self) -> bool:
        try:
            return self.click(
                locator=self._place_order,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to click Place order: %s",
                exc,
            )
            return False

    def submit_checkout_form(self) -> bool:
        return self.click_place_order()

    def is_checkout_form_invalid(self) -> bool:
        try:
            page_text = self.driver.find_element(
                "tag name",
                "body",
            ).text.lower()

            return (
                    "is required" in page_text
                    or "please accept the terms" in page_text
            )

        except WebDriverException as exc:
            self.log.error(
                "Unable to verify checkout validation message: %s",
                exc,
            )
            return False

    def accept_terms_and_conditions(self) -> bool:
        try:
            return self.click(
                locator=self._terms_checkbox,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to accept terms and conditions: %s",
                exc,
            )
            return False

    def is_order_confirmed(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._order_confirmation,
                locator_type="xpath",
                timeout=10,
            )

            if element is None:
                return False

            return element.text.strip() == "Order confirmed"

        except WebDriverException as exc:
            self.log.error(
                "Unable to verify order confirmation: %s",
                exc,
            )
            return False

    def get_order_id(self) -> str | None:
        try:
            element = self.wait_for_element_visible(
                locator=self._order_id,
                locator_type="xpath",
                timeout=10,
            )
            if element is None:
                return None

            return element.text.strip()

        except WebDriverException as exc:
            self.log.error(
                "Unable to retrieve order ID: %s",
                exc,
            )
            return None

    def get_payment_method(self) -> str | None:
        try:
            element = self.wait_for_element_visible(
                locator=self._payment_method,
                locator_type="xpath",
                timeout=10,
            )
            if element is None:
                return None

            return element.text.strip()

        except WebDriverException as exc:
            self.log.error(
                "Unable to retrieve payment method: %s",
                exc,
            )
            return None

    def enter_card_number(self, card_number: str) -> bool:
        try:
            return self.send_keys(
                locator=self._card_number,
                text=card_number,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to enter card number: %s",
                exc,
            )
            return False

    def enter_card_expiry(self, expiry: str) -> bool:
        try:
            return self.send_keys(
                locator=self._card_expiry,
                text=expiry,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to enter card expiry: %s",
                exc,
            )
            return False

    def enter_card_cvv(self, cvv: str) -> bool:
        try:
            return self.send_keys(
                locator=self._card_cvv,
                text=cvv,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to enter card CVV: %s",
                exc,
            )
            return False

    def enter_card_name(self, name: str) -> bool:
        try:
            return self.send_keys(
                locator=self._card_name,
                text=name,
                locator_type="xpath",
                clear_first=True,
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to enter card name: %s",
                exc,
            )
            return False

    def select_credit_card(self) -> bool:
        try:
            return self.click(
                locator=self._card_payment_method,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to select credit/debit card payment method: %s",
                exc,
            )
            return False