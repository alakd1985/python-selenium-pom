from utilities.screenshot import take_screenshot

class SoftAssert:
    def __init__(self, driver=None):
        self._errors = []
        self.driver = driver

    def verify(self, condition, message):
        if not condition:
            self._errors.append(message)

            if self.driver:
                path = take_screenshot(self.driver, "soft_assert_failure")
                print(f"[SOFT ASSERT] Screenshot saved: {path}")

    def assert_all(self):
        if self._errors:
            errors = "\n".join(self._errors)
            raise AssertionError(f"Soft assertion failures:\n{errors}")
