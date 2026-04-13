import argparse
import json
import sys


def get_version_string():
    """Return a formatted string with the current Python version."""
    v = sys.version_info
    return f"Python version: {v.major}.{v.minor}.{v.micro}"


def get_version_dict():
    """Return the current Python version as a dictionary."""
    v = sys.version_info
    return {"major": v.major, "minor": v.minor, "micro": v.micro}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print the current Python version.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output version as JSON",
    )
    args = parser.parse_args()

    if args.json:
        print(json.dumps(get_version_dict()))
    else:
        print(get_version_string())
