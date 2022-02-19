"""
Import of time module to set times for pause.
Import of gspread library and Credentials class from Google auth library
and wireup APIS, based on instructions from CI's Love Sandwiches project.
Import of colorama and termcolor modules to be able to color text
and thus improve readability and accessibility for the user.
Import functions from validations to run code.
"""
from logic import new_or_existing_design
from google_sheets_api import presentation_of_created_tote_bag
from logo_and_intro import intro


def start_program():
    """
    Start the program
    """
    new_or_existing_design()
    presentation_of_created_tote_bag()


def main():
    """
    Run all functions
    """
    intro()
    start_program()


main()