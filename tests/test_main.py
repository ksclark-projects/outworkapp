import re

from main import get_version_dict, get_version_string


def test_get_version_dict_date_field():
    """Verify get_version_dict returns a 'date' key with YYYY-MM-DD format."""
    result = get_version_dict()
    assert "date" in result
    assert isinstance(result["date"], str)
    assert re.match(r"\d{4}-\d{2}-\d{2}", result["date"]), (
        f"Expected date format YYYY-MM-DD, got: {result['date']!r}"
    )


def test_get_version_dict_time_field():
    """Verify get_version_dict returns a 'time' key with HH:MM:SS format."""
    result = get_version_dict()
    assert "time" in result
    assert isinstance(result["time"], str)
    assert re.match(r"\d{2}:\d{2}:\d{2}", result["time"]), (
        f"Expected time format HH:MM:SS, got: {result['time']!r}"
    )


def test_get_version_string_format():
    """Verify get_version_string returns 'Python version: X.Y.Z'."""
    result = get_version_string()
    pattern = r"Python version: \d+\.\d+\.\d+"
    assert re.match(pattern, result), (
        f"Expected format 'Python version: X.Y.Z', got: {result!r}"
    )


def test_get_version_dict_keys():
    """Verify get_version_dict returns a dict with the expected keys."""
    result = get_version_dict()
    assert isinstance(result, dict)
    assert {"major", "minor", "micro", "date", "time"}.issubset(result.keys())


def test_get_version_dict_values_are_ints():
    """Verify get_version_dict values are all integers."""
    result = get_version_dict()
    assert isinstance(result["major"], int)
    assert isinstance(result["minor"], int)
    assert isinstance(result["micro"], int)


def test_get_version_dict_matches_version_string():
    """Verify get_version_dict values are consistent with get_version_string."""
    import sys

    v = sys.version_info
    result = get_version_dict()
    assert result["major"] == v.major
    assert result["minor"] == v.minor
    assert result["micro"] == v.micro
