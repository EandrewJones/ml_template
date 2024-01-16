import sys
import subprocess


def is_conda_installed() -> bool:
    """Check if conda is installed."""
    try:
        subprocess.run(["conda", "--version"], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    if not is_conda_installed():
        print(
            "conda is not installed. Please install conda before using this template."
        )
        sys.exit(1)
