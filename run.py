"""
Import of gspread library and Credentials class from Google auth library
and wireup APIS, based on instructions from CI's Love Sandwiches project
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('design_your_own_tote_bag')  # Access Google sheet


def intro():
    """
    Printed logo, welcome message and information on how to design
    your own bag.
    """

    print(" ______       _ __            ___ ")
    print("(  /  _/_    ( /  )          ( / \ ")
    print("  /__ /  _    /--< __, _,     /  /_  (  o  _,  __ ")
    print("_/(_)(__(/_  /__ /(_(_(_)_  (/\_/(/_/_)_(_(_)_/ /_ ")
    print("                       /|                  /|")
    print("                      (/                  (/ \n\n")
    print("Welcome to Tote Bag Design!\n")
    print("Here you can custom design you tote bag.")
    print("You can choose from different fabrics and colors for ")
    print("the inside, the outside and the handles.\n")


def get_and_validate_name():
    """
    User first and last names are collected, and the name is validated in a
    while True loop with a break statement.
    The True loop makes sure the names are in letters, and capitalizes them.
    If names are missing or are not in letters a ValueError is raised.
    """
    while True:
        user_fname = input("Please let us know your first name: ").capitalize()
        user_lname = input("And your last name, please: ").capitalize()
        user_name = user_fname + " " + user_lname

        try:
            if user_fname.isalpha() and user_lname.isalpha():
                print(f"Welcome {user_name}!\n")
                break
            else:
                raise ValueError(f"You wrote {user_fname} {user_lname}, but "
                                 "we need both names, and in letters please.")
        except ValueError as e:
            print(f"Invalid entry: {e}\n")  # Input from CI's Love Sandwiches

    return user_name


def update_name_worksheet():
    """
    Update the Google Sheets name worksheet with the collected name.
    """
    print("Your name is being saved...\n")
    name_worksheet = SHEET.worksheet("name")  # Access name worksheet in Google Sheets
    name_worksheet.append_row([new_name])  # The name is saved in the name worksheet
    print("Your name has been saved successfully :-)\n")


def get_and_validate_outer_choice():
    """
    Outer fabric choice is collected, and validated in a
    while True loop with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not cotton, linen or denim a ValueError is raised.
    """
    while True:
        choice_o_fabric = input("Please choose fabric (cotton, linen or denim): ").lower()

        try:
            if choice_o_fabric.isalpha():
                print(f"You chose {choice_o_fabric} for the outside of the bag. Great!\n")
                break
            else:
                raise ValueError(f"You wrote {choice_o_fabric}, but we need a choice "
                                 "between cotton, linen and denim, in letters please.")
        except ValueError as e:
            print(f"Invalid entry: {e}\n")  # Input from CI's Love Sandwiches

    return choice_o_fabric


def update_design_worksheet_outer():
    """
    Update the Google Sheets design worksheet with the collected choice of outer fabric.
    """
    print("Your choice is being saved...\n")
    name_worksheet = SHEET.worksheet("design")  # Access design worksheet in Google Sheets
    name_worksheet.append_row([outer_choice])  # The choice is saved in the design worksheet
    print("Your choice has been saved successfully :-)\n")


intro()
new_name = get_and_validate_name()
update_name_worksheet()
outer_choice = get_and_validate_outer_choice()
update_design_worksheet_outer()
