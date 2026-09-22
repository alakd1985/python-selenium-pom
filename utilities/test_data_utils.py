from datetime import datetime


def generate_unique_suffix() -> str:
    """Generate a timestamp-based suffix for unique test data."""
    return datetime.now().strftime("%Y%m%d_%H%M%S_%f")


def build_unique_employee_data(employee: dict) -> dict:
    """Build unique employee data for OrangeHRM."""
    unique_suffix = generate_unique_suffix()

    return {
        "first_name": f"{employee['first_name']}_{unique_suffix}",
        "last_name": f"{employee['last_name']}_{unique_suffix}",
        "employee_id": f"E{unique_suffix[-8:].replace('_', '')}",
    }