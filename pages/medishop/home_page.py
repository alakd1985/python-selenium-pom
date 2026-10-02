from __future__ import annotations

from selenium.common.exceptions import WebDriverException

from base.base_page import BasePage


class MediShopHomePage(BasePage):

    _home_menu = "//a[normalize-space()='Home']"

    def is_home_page_displayed(self) -> bool:
        try:
            element = self.wait_for_element_visible(
                locator=self._home_menu,
                locator_type="xpath",
                timeout=10,
            )
            return element is not None
        except WebDriverException as exc:
            self.log.error(
                "Unable to verify MediShop home page: %s",
                exc,
            )
            return False
