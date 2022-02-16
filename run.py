"""
Import of time module to set times for pause.
Import of gspread library and Credentials class from Google auth library
and wireup APIS, based on instructions from CI's Love Sandwiches project.
Import of colorama and termcolor modules to be able to color text
and thus improve readability and accessibility for the user.
Import functions from validations to run code.
"""
from validations import new_or_existing_design
from validations import input_and_validate_first_name
from validations import input_and_validate_last_name
from validations import input_and_validate_outer_fabric
from validations import input_and_validate_outer_color
from validations import input_and_validate_inner_fabric
from validations import input_and_validate_inner_color
from validations import input_and_validate_handle_fabric
from validations import input_and_validate_handle_color
from validations import find_and_validate_bag_design
from google_sheets_api import update_name_worksheet
from google_sheets_api import update_design_worksheet
from google_sheets_api import get_design_no_from_worksheet
from google_sheets_api import return_new_no_to_worksheet
from google_sheets_api import create_unique_id
from google_sheets_api import get_data_from_worksheets
from logo_and_intro import intro


def main():
    """
    Run all functions
    """
    intro()
    new_or_existing_design()
    first_name = input_and_validate_first_name()
    full_name = input_and_validate_last_name(first_name)
    update_name_worksheet(full_name)
    outer_fabric = input_and_validate_outer_fabric()
    outer_color = input_and_validate_outer_color()
    inner_fabric = input_and_validate_inner_fabric()
    inner_color = input_and_validate_inner_color()
    handle_fabric = input_and_validate_handle_fabric()
    handle_color = input_and_validate_handle_color()
    update_design_worksheet(outer_color, outer_fabric, inner_color,
                            inner_fabric, handle_color, handle_fabric)
    present_no = get_design_no_from_worksheet()
    return_new_no_to_worksheet(present_no)
    create_unique_id()
    get_data_from_worksheets()
    find_and_validate_bag_design()


main()
