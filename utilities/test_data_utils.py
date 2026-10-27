from datetime import UTC, datetime


def generate_unique_suffix() -> str:
    """Generate a timestamp-based suffix for unique test data."""
    return datetime.now(UTC).strftime("%Y%m%d_%H%M%S_%f")

import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ORDER_DATA_FILE = PROJECT_ROOT / "test_data" / "medishop_orders.json"


def load_medishop_orders() -> list[dict[str, Any]]:
    """Load synthetic MediShop order test data from JSON."""
    with ORDER_DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    orders = data["orders"]

    if len(orders) != 10:
        raise ValueError(
            f"Expected 10 test orders, found {len(orders)}"
        )

    return orders
