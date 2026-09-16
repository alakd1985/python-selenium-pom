from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select


class Dropdown:
    """Reusable operations for standard HTML <select> dropdowns."""

    def __init__(self, page):
        self.page = page

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