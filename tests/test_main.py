import re

from main import get_version_dict, get_version_string


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
    assert {"major", "minor", "micro", "os_version"}.issubset(result.keys())


def test_get_version_dict_os_version():
    """Verify get_version_dict includes a non-empty os_version string."""
    result = get_version_dict()
    assert isinstance(result["os_version"], str)
    assert len(result["os_version"]) > 0


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
