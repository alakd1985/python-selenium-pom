from __future__ import annotations

from datetime import datetime
from pathlib import Path


def save_screenshot(driver, test_name: str, directory: str = "screenshots") -> str | None:
    try:
        folder = Path(directory)
        folder.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        safe_name = test_name.replace("/", "_").replace(" ", "_")
        path = folder / f"{safe_name}_{timestamp}.png"
        driver.save_screenshot(str(path))
        return str(path)
    except Exception:
        return None
