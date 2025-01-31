"""Tests standard target features using the built-in SDK tests library."""

from __future__ import annotations

import typing as t

from singer_sdk.helpers._compat import importlib_resources
from singer_sdk.testing import get_target_test_class
from singer_sdk.testing.suites import TestSuite
from singer_sdk.testing.templates import TargetFileTestTemplate

import tests.streams as test_streams
from target_hubspot.target import TargetHubSpot

if t.TYPE_CHECKING:
    from singer_sdk.helpers._compat import Traversable

SAMPLE_CONFIG: dict[str, t.Any] = {
    "access_token": "",
    "date_format": "YEAR_MONTH_DAY",
    "import_operations": "UPSERT",
    "column_mapping": [
        {
            "columnName": "email",
            "propertyName": "email",
            "columnObjectTypeId": "0-1",
            "columnType": "HUBSPOT_ALTERNATE_ID",
        },
        {"columnName": "name", "propertyName": "firstname", "columnObjectTypeId": "0-1"},
        {"columnName": "company_name", "propertyName": "company", "columnObjectTypeId": "0-1"},
        {"columnName": "phone_number", "propertyName": "mobilephone", "columnObjectTypeId": "0-1"},
    ],
}


class SampleData(TargetFileTestTemplate):
    """Test Target record with date attributes."""

    name = "sample_data"

    @property
    def singer_filepath(self) -> Traversable:
        return importlib_resources.files(test_streams) / "sample_data.singer"


# Run standard built-in target tests from the SDK:
StandardTargetTests = get_target_test_class(
    target_class=TargetHubSpot,
    config=SAMPLE_CONFIG,
    include_target_tests=False,
    custom_suites=[
        TestSuite(
            kind="target",
            tests=[
                SampleData,
            ],
        )
    ],
)


class TestTargetHubSpot(StandardTargetTests):  # type: ignore[misc, valid-type]  # noqa: E501
    """Standard Target Tests."""

    pass
