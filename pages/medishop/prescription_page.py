from __future__ import annotations

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base.base_page import BasePage


class MediShopPrescriptionPage(BasePage):

    _upload_prescription_link = (
        "//a[normalize-space()='Upload a prescription']"
    )

    _upload_first_prescription_button = (
        "//button[normalize-space()='Upload your first prescription']"
    )

    _prescription_file_input = (
        "//input[@id='rx_file_input']"
    )

    _prescription_consent_checkbox = (
        "//input[@id='rx_consent_checkbox']"
    )

    _upload_prescription_button = (
        "//button[@data-testid='prescription_save_button']"
    )

    _uploaded_prescription = (
        "//strong[starts-with(normalize-space(), 'data_attachments_')]"
    )

    def click_upload_prescription(self) -> bool:
        try:
            return self.click(
                locator=self._upload_prescription_link,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to click Upload a prescription: %s",
                exc,
            )
            return False

    def click_upload_first_prescription(self) -> bool:
        try:
            return self.click(
                locator=self._upload_first_prescription_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to click Upload your first prescription: %s",
                exc,
            )
            return False

    def upload_prescription_file(self, file_path: str) -> bool:
        try:
            return self.send_keys(
                locator=self._prescription_file_input,
                text=file_path,
                locator_type="xpath",
                clear_first=False,
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to upload prescription file: %s",
                exc,
            )
            return False

    def accept_prescription_consent(self) -> bool:
        try:
            return self.click(
                locator=self._prescription_consent_checkbox,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to accept prescription consent: %s",
                exc,
            )
            return False

    def save_prescription(self) -> bool:
        try:
            return self.click(
                locator=self._upload_prescription_button,
                locator_type="xpath",
            )
        except WebDriverException as exc:
            self.log.error(
                "Unable to save prescription: %s",
                exc,
            )
            return False

    def is_prescription_uploaded(self) -> bool:
        try:
            wait = WebDriverWait(self.driver, 30)

            wait.until(
                EC.visibility_of_element_located(
                    (
                        self.get_by_type("xpath"),
                        self._uploaded_prescription,
                    )
                )
            )

            return True

        except WebDriverException as exc:
            self.log.error(
                "Unable to verify uploaded prescription: %s",
                exc,
            )
            return False