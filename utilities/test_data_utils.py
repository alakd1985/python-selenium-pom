from datetime import datetime, timezone


def generate_unique_suffix() -> str:
    """Generate a timestamp-based suffix for unique test data."""
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")