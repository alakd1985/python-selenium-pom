from datetime import datetime


def generate_unique_suffix() -> str:
    """
    Generate a timestamp-based unique suffix.

    Example:
    20260915_142035_123456
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S_%f")