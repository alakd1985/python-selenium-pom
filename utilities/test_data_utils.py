from datetime import UTC, datetime


def generate_unique_suffix() -> str:
    """Generate a timestamp-based suffix for unique test data."""
    return datetime.now(UTC).strftime("%Y%m%d_%H%M%S_%f")