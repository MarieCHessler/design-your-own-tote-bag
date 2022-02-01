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
        user_fname = input("Please let us know your first name: \n").capitalize()
        user_lname = input("\nAnd your last name, please: \n").capitalize()
        user_name = user_fname + " " + user_lname

        try:
            if user_fname.isalpha() and user_lname.isalpha():
                print(f"\nWelcome {user_name}!\n")
                break
            if not user_fname:
                print("\nSorry, did not catch you first name.\n")
            if not user_lname:
                print("\nSorry, did not catch you last name.\n")
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
    name_worksheet = SHEET.worksheet("name")  # Access Google Sheets worksheet
    name_worksheet.append_row([new_name])  # The name is saved in the worksheet
    print("Your name has been saved successfully :-)\n")


def get_and_validate_outer_fabric():
    """
    Outer fabric choice is collected, and validated in a while True loop
    with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not cotton,
    linen or denim a ValueError is raised.
    """
    while True:
        o_fabric = input("Would you like the outer fabric to be "
                         "cotton, linen or denim? \n").lower()

        try:
            if o_fabric.isalpha():
                print(f"You chose {o_fabric} for the outside. Nice!\n")
                break
            else:
                raise ValueError(f"You wrote {o_fabric}, but we need a choice "
                                 "between cotton, linen and denim, "
                                 "in letters please.")
        except ValueError as e:
            print(f"Invalid entry: {e}\n")  # Input from CI's Love Sandwiches

    return o_fabric


def get_and_validate_inner_fabric():
    """
    Inner fabric choice is collected, and validated in a while True loop
    with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not cotton,
    linen or denim a ValueError is raised.
    """
    while True:
        i_fabric = input("What kind of inner fabric do you prefer, "
                         "cotton or spinnaker? \n").lower()

        try:
            if i_fabric.isalpha():
                print(f"You chose {i_fabric} for the inside. Good choice!\n")
                break
            else:
                raise ValueError(f"You wrote {i_fabric}, but we need a choice "
                                 "between cotton and spinnaker, "
                                 "in letters please.")
        except ValueError as e:
            print(f"Invalid entry: {e}\n")  # Input from CI's Love Sandwiches

    return i_fabric


def get_and_validate_handles_fabric():
    """
    Handles fabric choice is collected, and validated in a while True loop
    with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not cotton or belt
    a ValueError is raised.
    """
    while True:
        h_fabric = input("For the handles, would you like them to be made"
                         "from cotton or belt? \n").lower()

        try:
            if h_fabric.isalpha():
                print(f"You chose {h_fabric} for the handles. Great!\n")
                break
            else:
                raise ValueError(f"You wrote {h_fabric}, but we need a choice "
                                 "between cotton and belt, in letters please.")
        except ValueError as e:
            print(f"Invalid entry: {e}\n")  # Input from CI's Love Sandwiches

    return h_fabric


def update_design_worksheet():
    """
    Update the Google Sheets design worksheet with the collected choices of
    fabrics, colors and handles.
    """
    print("Your choices are being saved...\n")
    design_worksheet = SHEET.worksheet("design")  # Access Google Sheets worksheet
    design_worksheet.append_row([outer_fabric, inner_fabric, handles_fabric])  # The choices are saved in the design worksheet
    print("Your choices have been saved successfully :-)\n")


def get_data_from_worksheets():
    """
    Get the data back from the Google Sheets name and design worksheets to
    thank the user for creating a bag with a selection of fabrics, colors
    and handles.
    """
    print("Your tote bag is now being designed...\n")
    your_name = SHEET.worksheet("name").get_all_values()
    your_name_row = your_name[-1]
    choices = SHEET.worksheet("design").get_all_values()
    choices_row = choices[-1]
    print(f"{your_name_row}, you have created your own cool tote bag ")
    print(f"from {choices_row} \n\n")
    print("     _______      ")
    print("     |     |      ")
    print("   -----------    ")
    print("  |           |   ")
    print("  |           |   ")
    print("  |           |   ")
    print("  |  My Tote  |   ")
    print("   -----------    \n\n")
    print("Thank you for designing your bag with us!\n")


intro()
new_name = get_and_validate_name()
update_name_worksheet()
outer_fabric = get_and_validate_outer_fabric()
inner_fabric = get_and_validate_inner_fabric()
handles_fabric = get_and_validate_handles_fabric()
update_design_worksheet()
get_data_from_worksheets()
