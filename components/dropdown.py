from __future__ import annotations

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select


class Dropdown:
    """Reusable operations for standard and custom dropdowns."""

    def __init__(self, page):
        self.page = page

    # =========================================================
    # Standard HTML <select> dropdown
    # =========================================================

    def select_by_visible_text(
        self,
        locator: str,
        text: str,
        locator_type: str = "xpath",
    ) -> bool:
        try:
            element = self.page.wait_for_element_visible(
                locator,
                locator_type,
            )

            if element is None:
                return False

            Select(element).select_by_visible_text(text)
            return True

        except WebDriverException as exc:
            self.page.log.error(
                "Unable to select '%s' from dropdown %s: %s",
                text,
                locator,
                exc,
            )
            return False

    def select_by_value(
        self,
        locator: str,
        value: str,
        locator_type: str = "xpath",
    ) -> bool:
        try:
            element = self.page.wait_for_element_visible(
                locator,
                locator_type,
            )

            if element is None:
                return False

            Select(element).select_by_value(value)
            return True

        except WebDriverException as exc:
            self.page.log.error(
                "Unable to select value '%s' from dropdown %s: %s",
                value,
                locator,
                exc,
            )
            return False

    def select_by_index(
        self,
        locator: str,
        index: int,
        locator_type: str = "xpath",
    ) -> bool:
        try:
            element = self.page.wait_for_element_visible(
                locator,
                locator_type,
            )

            if element is None:
                return False

            Select(element).select_by_index(index)
            return True

        except WebDriverException as exc:
            self.page.log.error(
                "Unable to select index '%s' from dropdown %s: %s",
                index,
                locator,
                exc,
            )
            return False

    # =========================================================
    # Custom OrangeHRM dropdown
    # =========================================================

    def get_options(
        self,
        dropdown_locator: str,
        option_locator: str = "//div[@role='option']",
        locator_type: str = "xpath",
    ) -> list[str]:
        """
        Open a custom dropdown and return all visible options.

        Designed for OrangeHRM custom dropdowns that use
        div elements with role='option'.
        """

        try:
            # Open the dropdown
            if not self.page.click(
                locator=dropdown_locator,
                locator_type=locator_type,
            ):
                self.page.log.error(
                    "Unable to open dropdown: %s",
                    dropdown_locator,
                )
                return []

            # Wait until at least one option becomes visible.
            first_option = self.page.wait_for_element_visible(
                locator=option_locator,
                locator_type="xpath",
                timeout=10,
            )

            if first_option is None:
                self.page.log.error(
                    "No visible options found for dropdown: %s",
                    dropdown_locator,
                )
                return []

            # Get all option elements.
            elements = self.page.get_elements(
                locator=option_locator,
                locator_type="xpath",
            )

            options = []

            for element in elements:
                if element.is_displayed():
                    text = element.text.strip()

                    if text:
                        options.append(text)

            self.page.log.info(
                "Found %d dropdown options for %s",
                len(options),
                dropdown_locator,
            )

            for option in options:
                print(f"  - {option}")

            return options

        except WebDriverException as exc:
            self.page.log.error(
                "Unable to retrieve dropdown options from %s: %s",
                dropdown_locator,
                exc,
            )
            return []