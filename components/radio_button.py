from selenium.common.exceptions import WebDriverException


class RadioButton:
    """Reusable operations for radio buttons."""

    def __init__(self, page):
        self.page = page

    def select(
        self,
        locator: str,
        locator_type: str = "xpath",
    ) -> bool:
        try:
            element = self.page.wait_for_element_clickable(
                locator,
                locator_type,
            )

            if element is None:
                return False

            if not element.is_selected():
                element.click()

            return element.is_selected()

        except WebDriverException as exc:
            self.page.log.error(
                "Unable to select radio button %s: %s",
                locator,
                exc,
            )
            return False

    def is_selected(
        self,
        locator: str,
        locator_type: str = "xpath",
    ) -> bool:
        try:
            element = self.page.get_element(
                locator,
                locator_type,
            )

            return bool(element and element.is_selected())

        except WebDriverException as exc:
            self.page.log.error(
                "Unable to check radio button %s: %s",
                locator,
                exc,
            )
            return False