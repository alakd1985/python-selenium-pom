from __future__ import annotations

import json
import os
import platform
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENVIRONMENTS_FILE = Path(__file__).resolve().parent / "environments.json"

if load_dotenv:
    load_dotenv(PROJECT_ROOT / ".env")

# Safe defaults for the OrangeHRM public demo environment.
# Real environments should supply credentials through CI/CD secrets.
os.environ.setdefault("ORANGEHRM_USERNAME", "Admin")
os.environ.setdefault("ORANGEHRM_PASSWORD", "admin123")


def _resolve_env(value):
    if isinstance(value, dict):
        return {k: _resolve_env(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_resolve_env(v) for v in value]
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        name = value[2:-1]
        return os.getenv(name, value)
    return value


def _as_bool(value, default=False):
    if value is None:
        return default
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _as_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


@dataclass(frozen=True)
class Settings:
    environment: str
    base_url: str
    browser: str
    timeout: int
    implicit_wait: int
    headless: bool
    os_type: str
    window_width: int
    window_height: int


def load_settings(environment: str | None = None) -> Settings:
    env_name = (
        environment
        or os.getenv("TEST_ENV")
        or os.getenv("ENV")
        or "dev"
    ).strip().lower()

    if not ENVIRONMENTS_FILE.exists():
        raise FileNotFoundError(
            f"Environment configuration not found: {ENVIRONMENTS_FILE}"
        )

    with ENVIRONMENTS_FILE.open("r", encoding="utf-8") as file:
        environments = _resolve_env(json.load(file))

    if env_name not in environments:
        raise ValueError(
            f"Unknown test environment '{env_name}'. "
            f"Available environments: {', '.join(environments)}"
        )

    data = environments[env_name]

    base_url = os.getenv("BASE_URL", data.get("base_url", "")).strip()
    browser = os.getenv("BROWSER", data.get("browser", "firefox")).strip().lower()
    timeout = _as_int(os.getenv("SELENIUM_TIMEOUT", data.get("timeout")), 10)
    implicit_wait = _as_int(
        os.getenv("SELENIUM_IMPLICIT_WAIT", data.get("implicit_wait")),
        0,
    )
    headless = _as_bool(
        os.getenv("HEADLESS", data.get("headless")),
        False,
    )
    os_type = os.getenv("OS_TYPE", data.get("os_type", platform.system())).strip()
    window_width = _as_int(data.get("window_width"), 1920)
    window_height = _as_int(data.get("window_height"), 1080)

    if not base_url or base_url.startswith("${"):
        raise ValueError(
            f"No valid base URL configured for environment '{env_name}'. "
            "Set BASE_URL or the environment-specific URL variable."
        )

    if browser not in {"chrome", "firefox"}:
        raise ValueError(
            f"Unsupported browser '{browser}'. Use chrome or firefox."
        )

    return Settings(
        environment=env_name,
        base_url=base_url,
        browser=browser,
        timeout=timeout,
        implicit_wait=implicit_wait,
        headless=headless,
        os_type=os_type,
        window_width=window_width,
        window_height=window_height,
    )


# Backward-compatible constants used by existing tests/code.
DEFAULT_SETTINGS = load_settings()
BASE_URL = DEFAULT_SETTINGS.base_url
DEFAULT_BROWSER = DEFAULT_SETTINGS.browser
DEFAULT_TIMEOUT = DEFAULT_SETTINGS.timeout
HEADLESS = DEFAULT_SETTINGS.headless
VALID_USERNAME = os.getenv("ORANGEHRM_USERNAME", "Admin")
VALID_PASSWORD = os.getenv("ORANGEHRM_PASSWORD", "admin123")
