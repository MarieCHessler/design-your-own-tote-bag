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


def intro_validate_name():
    """
    Printed logo, welcome message and information on how to design
    your own bag.
    User first and last names are collected, and the name is validated in a
    while True loop with a break statement.
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

    while True:
        try:
            user_fname = input("Please let us know your first name: ").capitalize()
            user_lname = input("And your last name, please: ").capitalize()
            # user_name = user_fname + " " + user_lname
            if user_fname.isalpha() and user_lname.isalpha():
                print(f"Welcome {user_fname} {user_lname}!")
                break
            else:
                raise ValueError(f"You wrote {user_fname} {user_lname}, "
                                 "but we need your names in letters please.")
        except ValueError as e:
            print(f"Invalid entry: {e}\n")


intro_validate_name()
