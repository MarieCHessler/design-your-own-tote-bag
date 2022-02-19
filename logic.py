"""
Import of colorama and termcolor modules to be able to color text
and thus improve readability and accessibility for the user.
Import functions from constants.py, google_sheets_api.py and
validations.py to run code.
"""
from colorama import init
from termcolor import colored

from constants import NEW_DESIGN, EXISTING_DESIGN
from google_sheets_api import update_name_worksheet, update_design_worksheet, \
    get_design_no_from_worksheet, return_new_no_to_worksheet, \
    create_unique_id, presentation_of_created_tote_bag
from validations import find_and_validate_bag_design, \
    input_and_validate_first_name, input_and_validate_last_name, \
    input_and_validate_outer_fabric, input_and_validate_outer_color, \
    input_and_validate_inner_fabric, input_and_validate_inner_color, \
    input_and_validate_handle_fabric, input_and_validate_handle_color

# Needed by colorama to run on Windows
init()


def new_or_existing_design():
    """
    Let user choose between picking up his/her existing design
    or creating a new one.
    """
    while True:
        # Have user choose if he/she wants to pick up his/her existing design
        # or create a new one.
        choice_e_or_n = input(colored("\nWould you like to create a new "
                                      "design, or pick up one created "
                                      "before?\n"
                                      "Enter N for new and E for existing: "
                                      "\n", "cyan")).upper()
        # Validate choice
        try:
            if choice_e_or_n == NEW_DESIGN:
                new_bag_design()
            elif choice_e_or_n == EXISTING_DESIGN:
                find_and_validate_bag_design()
            else:
                raise ValueError("\nPlease enter E for existing or N for "
                                 "new.\n")
        # Error handling inspired by Code Institute's Love Sandwiches
        except ValueError as e:
            print(f"{e}\n")


# Tips given on how to structure functions for best flow - Reuben Ferrante


def update_names():
    """
    Define first, last and full names, and update the name worksheet
    """
    first_name = input_and_validate_first_name()
    full_name = input_and_validate_last_name(first_name)
    update_name_worksheet(full_name)


def validate_fabrics():
    """
    Define design fabrics and colors, and update the design worksheet
    """
    outer_fabric = input_and_validate_outer_fabric()
    outer_color = input_and_validate_outer_color()
    inner_fabric = input_and_validate_inner_fabric()
    inner_color = input_and_validate_inner_color()
    handle_fabric = input_and_validate_handle_fabric()
    handle_color = input_and_validate_handle_color()
    update_design_worksheet(outer_color, outer_fabric, inner_color,
                            inner_fabric, handle_color, handle_fabric)


def save_bag_design():
    """
    Define present number, update the design number worksheet and
    create a design ID
    """
    present_no = get_design_no_from_worksheet()
    return_new_no_to_worksheet(present_no)
    create_unique_id()


def present_new_bag():
    """
    Present the new tote bag design to the user
    """
    presentation_of_created_tote_bag()


def new_bag_design():
    """
    Update the names, validate the facbrics, and save the bag design
    """
    update_names()
    validate_fabrics()
    save_bag_design()
    presentation_of_created_tote_bag()
