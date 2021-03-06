"""
Import functions from logic.py, google_sheets_api.py and logo_and_intro.py
to run code.
"""
from logic import new_or_existing_design
from logo_and_intro import intro


def start_program():
    """
    Start the program
    """
    new_or_existing_design()


def main():
    """
    Run all functions
    """
    intro()
    start_program()


main()
