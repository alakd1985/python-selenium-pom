class SoftAssert:
    def __init__(self):
        self._errors = []

    def verify(self, condition, message):
        if not condition:
            self._errors.append(message)

    def assert_all(self):
        if self._errors:
            errors = "\n".join(self._errors)
            raise AssertionError(f"Soft assertion failures:\n{errors}")
