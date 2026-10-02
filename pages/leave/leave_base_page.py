from __future__ import annotations

from base.base_page import BasePage


class LeaveBasePage(BasePage):
    """Common functionality shared by Leave module pages."""

    _leave_menu = (
        "//span[contains(@class,'oxd-main-menu-item--name') "
        "and normalize-space()='Leave']"
    )

    def open_leave(self) -> bool:
        """Open the Leave module from the main menu."""
        return self.click(
            locator=self._leave_menu,
            locator_type="xpath",
        )