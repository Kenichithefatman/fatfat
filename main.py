"""Start the Student Grader System."""

from grader.menu import run_menu
from grader.storage import load_students


def main() -> None:
    """Load saved records and start the command-line menu."""
    try:
        manager = load_students()
    except (OSError, ValueError) as error:
        print(f"Cannot start: {error}")
        return
    run_menu(manager)


if __name__ == "__main__":
    main()
