"""
Import of time module to set times for pause.
Import of gspread library and Credentials class from Google auth library
and wireup APIS, based on instructions from CI's Love Sandwiches project.
Import of colorama module to be able to color text and thus improve
readability and accessibility for the user.
Import functions from validations to run code
"""
import time
import gspread
from google.oauth2.service_account import Credentials
from colorama import init
from termcolor import colored
from validations import new_or_existing_design, input_and_validate_first_name
from validations import input_and_validate_last_name
from validations import input_and_validate_outer_fabric
from validations import input_and_validate_outer_color
from validations import input_and_validate_inner_fabric
from validations import input_and_validate_inner_color
from validations import input_and_validate_handle_fabric
from validations import input_and_validate_handle_color
from google_sheets_api import update_name_worksheet, update_design_worksheet
from google_sheets_api import get_design_no_from_worksheet
from google_sheets_api import return_new_no_to_worksheet
from google_sheets_api import create_unique_id
from google_sheets_api import get_data_from_worksheets
from google_sheets_api import find_bag_design

init()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('design_your_own_tote_bag')  # Access Google sheet.


def intro():
    """
    Printed logo, welcome message and information on how to design
    your own bag.
    """
    # Idea for logo design from ASCII ART https://patorjk.com/software/taag,
    # but revised.
    print("""
     ______       _ __            ___
    (  /  _/_    ( /  )          ( / \ 
      /_  /  _    /--< _   _      /  /_  (  o  _   __
    _/(_)(__(/_  /__ /(_(_(_)_  (/__/(/_/_)_(_(_)_/ /_
                           /|                  /|
                          (/                  (/ \n
    """)

    print(colored("Welcome to Tote Bag Design!\n", "blue"))

    print("Here you can custom design your tote bag.")
    print("We reuse old spinnakers, scrap furnishing fabrics, "
          "and belts,")
    print("where you can choose from different fabrics "
          "and colors for the inside,")
    print("the outside and the handles.\n")

    print("You can also pick up a previously made design "
          "with the design ID you")
    print("get on creation.\n\n")

    time.sleep(7)


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
    find_bag_design()


main()
