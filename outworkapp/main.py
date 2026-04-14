import argparse
import json
import platform
import sys

import psutil


def get_version_string():
    """Return a formatted string with the current Python version and CPU usage."""
    v = sys.version_info
    cpu_usage = psutil.cpu_percent(interval=0.1)
    return f"Python version: {v.major}.{v.minor}.{v.micro} | CPU usage: {cpu_usage}%"


def get_version_dict():
    """Return the current Python version and CPU usage as a dictionary."""
    v = sys.version_info
    return {
        "major": v.major,
        "minor": v.minor,
        "micro": v.micro,
        "os_version": platform.platform(),
        "cpu_usage": psutil.cpu_percent(interval=0.1),
    }


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
