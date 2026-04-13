import re

from main import get_version_string


def test_get_version_string_format():
    """Verify get_version_string returns 'Python version: X.Y.Z'."""
    result = get_version_string()
    pattern = r"Python version: \d+\.\d+\.\d+"
    assert re.match(pattern, result), (
        f"Expected format 'Python version: X.Y.Z', got: {result!r}"
    )
