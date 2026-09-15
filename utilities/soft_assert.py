from __future__ import annotations


class SoftAssert:
    """Minimal soft-assert helper retained for legacy non-BDD tests."""

    def __init__(self, driver=None):
        self.driver = driver
        self._errors: list[str] = []

    def assert_true(self, condition: bool, message: str = "") -> None:
        if not condition:
            self._errors.append(message or "Expected condition to be True")

    def assert_false(self, condition: bool, message: str = "") -> None:
        if condition:
            self._errors.append(message or "Expected condition to be False")

    def assert_equal(self, actual, expected, message: str = "") -> None:
        if actual != expected:
            self._errors.append(
                message or f"Expected {expected!r}, got {actual!r}"
            )

    def assert_all(self) -> None:
        if self._errors:
            error_message = "Soft assertion failures:\n- " + "\n- ".join(self._errors)
            self._errors.clear()
            raise AssertionError(error_message)
