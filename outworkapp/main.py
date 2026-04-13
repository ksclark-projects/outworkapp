import sys


def get_version_string():
    """Return a formatted string with the current Python version."""
    v = sys.version_info
    return f"Python version: {v.major}.{v.minor}.{v.micro}"


if __name__ == "__main__":
    print(get_version_string())
