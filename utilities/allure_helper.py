from __future__ import annotations

from pathlib import Path

import allure


def attach_screenshot(path: str | None, name: str = "Failure Screenshot") -> None:
    if path and Path(path).exists():
        allure.attach.file(
            path,
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )


def attach_page_source(
    page_source: str | None,
    name: str = "Failure Page Source",
) -> None:
    if page_source:
        allure.attach(
            page_source,
            name=name,
            attachment_type=allure.attachment_type.HTML,
        )


def attach_text(
    content: str,
    name: str,
) -> None:
    allure.attach(
        content,
        name=name,
        attachment_type=allure.attachment_type.TEXT,
    )
