"""Provides Unit Tests for the `abis_mapping.plugins.empty` module"""


# Third-Party
import frictionless

# Local
from abis_mapping import plugins


def test_checks_not_empty() -> None:
    """Tests the NotEmpty Checker"""
    # Construct Fake Resource
    resource = frictionless.Resource(
        source=__file__,
    )

    # Validate
    report: frictionless.Report = resource.validate(
        checks=[
            plugins.empty.NotEmpty(),
        ]
    )

    # Check
    assert not report.valid
    assert len(report.flatten()) == 1
