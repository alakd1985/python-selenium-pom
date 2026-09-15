from __future__ import annotations

import csv
import json
import os
from copy import deepcopy
from pathlib import Path
from typing import Any


class TestDataError(Exception):
    """Raised when test data is missing or invalid."""


class DataReader:
    """
    Centralized data-access layer for test automation.

    Supported sources:
        - JSON
        - CSV
        - pytest-bdd data tables
        - environment variables using ${VARIABLE_NAME}
    """

    def __init__(self, data_dir: str | Path = "test_data") -> None:
        self.data_dir = Path(data_dir)

    def load_json(self, file_name: str) -> Any:
        path = self._resolve_path(file_name, ".json")

        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as exc:
            raise TestDataError(
                f"Invalid JSON in {path}: {exc}"
            ) from exc

        return self._resolve_env(data)

    def load_csv(self, file_name: str) -> list[dict[str, str]]:
        path = self._resolve_path(file_name, ".csv")

        with path.open("r", encoding="utf-8", newline="") as file:
            rows = list(csv.DictReader(file))

        return [
            self._resolve_env(row)
            for row in rows
        ]

    def get_record(
        self,
        file_name: str,
        key: str,
    ) -> dict[str, Any]:
        data = self.load_json(file_name)

        if not isinstance(data, dict):
            raise TestDataError(
                f"{file_name} must contain a JSON object."
            )

        if key not in data:
            raise TestDataError(
                f"Record '{key}' was not found in {file_name}."
            )

        record = deepcopy(data[key])

        if not isinstance(record, dict):
            raise TestDataError(
                f"Record '{key}' must be a JSON object."
            )

        return record

    @staticmethod
    def table_to_dict(
        datatable: list[list[str]],
    ) -> dict[str, str]:
        if len(datatable) < 2:
            raise TestDataError(
                "BDD data table must contain a header row "
                "and at least one data row."
            )

        headers = [
            str(header).strip()
            for header in datatable[0]
        ]

        values = [
            str(value).strip()
            for value in datatable[1]
        ]

        if len(headers) != len(values):
            raise TestDataError(
                "BDD table header/value column counts do not match."
            )

        return dict(zip(headers, values))

    @staticmethod
    def validate_required_fields(
        data: dict[str, Any],
        required_fields: set[str],
    ) -> None:
        missing = {
            field
            for field in required_fields
            if field not in data
            or data[field] is None
            or str(data[field]).strip() == ""
        }

        if missing:
            raise TestDataError(
                f"Missing required test-data fields: {sorted(missing)}"
            )

    def _resolve_path(
        self,
        file_name: str,
        expected_suffix: str,
    ) -> Path:
        path = self.data_dir / file_name

        if path.suffix.lower() != expected_suffix:
            path = path.with_suffix(expected_suffix)

        if not path.exists():
            raise TestDataError(
                f"Test data file not found: {path}"
            )

        return path

    @staticmethod
    def _resolve_env(value: Any) -> Any:
        if isinstance(value, dict):
            return {
                key: DataReader._resolve_env(item)
                for key, item in value.items()
            }

        if isinstance(value, list):
            return [
                DataReader._resolve_env(item)
                for item in value
            ]

        if (
            isinstance(value, str)
            and value.startswith("${")
            and value.endswith("}")
        ):
            env_name = value[2:-1]
            return os.getenv(env_name, value)

        return value
