"""
Import of gspread library and Credentials class from Google auth library
and wireup APIS, based on instructions from CI's Love Sandwiches project
Import of colorama module to be able to color text and thus improve
readability and accessibility for the user
"""
import gspread
from google.oauth2.service_account import Credentials
from colorama import init
from termcolor import colored
init()

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

    print("""
     ______       _ __            ___
    (  /  _/_    ( /  )          ( / \ 
      /__ /  _    /--< __, _,     /  /_  (  o  _,  __
    _/(_)(__(/_  /__ /(_(_(_)_  (/\_/(/_/_)_(_(_)_/ /_
                           /|                  /|
                          (/                  (/ \n\n
    """)
    print(colored("Welcome to Tote Bag Design!\n", "blue"))
    print("Here you can custom design you tote bag.")
    print("You can choose from different fabrics and colors for ")
    print("the inside, the outside and the handles.\n")


def get_and_validate_fname():
    """
    User first name is collected, and the name is validated in a
    while True loop with a break statement.
    The True loop makes sure the name is in letters, and capitalizes them.
    If names are missing or are not in letters a ValueError is raised.
    """
    while True:
        fname = input(colored("Please give us your first name: \n",
                              "cyan")).capitalize()

        try:
            if fname.isalpha():
                print()
                break
            if not fname:
                print("\nSorry, we did not catch you first name.\n")
            else:
                raise ValueError(f"You wrote {fname}, but we need the "
                                 "name, and in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return fname


def get_and_validate_lname(fname):
    """
    User first and last names are collected, and the name is validated in a
    while True loop with a break statement.
    The True loop makes sure the names are in letters, and capitalizes them.
    If names are missing or are not in letters a ValueError is raised.
    """
    while True:
        lname = input(colored("And your last name, please: \n",
                              "cyan")).capitalize()
        full_name = fname + " " + lname

        try:
            if lname.isalpha():
                print(colored(f"\nWelcome {full_name}!\n", "green"))
                break
            if not lname:
                print("\nSorry, we did not catch you last name.\n")
            else:
                raise ValueError(f"You wrote {lname}, but we need the "
                                 "name, and in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return full_name


def update_name_worksheet(full_name):
    """
    Update the Google Sheets name worksheet with the collected name.
    """
    print("Your name is being saved...\n")
    name_worksheet = SHEET.worksheet("name")  # Access Google Sheets worksheet
    # The name is saved in the worksheet
    name_worksheet.append_row([full_name])
    print("Now we have your name, thanks :-)\n")


def get_and_validate_outer_fabric():
    """
    Outer fabric choice is collected, and validated in a while True loop
    with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not cotton,
    linen or denim a ValueError is raised.
    """
    while True:
        o_fabric = input(colored("Would you like the outer fabric to be "
                                 "cotton, linen or denim? \n", "cyan")).lower()

        try:
            if o_fabric.isalpha():
                print(colored(f"\nYou chose {o_fabric} for the outside. "
                              "Nice!\n", "green"))
                break
            if not o_fabric:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {o_fabric}, but we need a choice "
                                 "between cotton, linen and denim, "
                                 "in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return o_fabric


def get_and_validate_outer_color():
    """
    Outer color choice is collected, and validated in a while True loop
    with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not blue,
    cream or grey a ValueError is raised.
    """
    while True:
        o_color = input(colored("Do you prefer the outer color to be "
                        "blue, cream or grey? \n", "cyan")).lower()

        try:
            if o_color.isalpha():
                print(colored(f"\nYou chose {o_color} for the outside. "
                              "Looks good!\n", "green"))
                break
            if not o_color:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {o_color}, but we need a choice "
                                 "between blue, cream and grey, "
                                 "in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return o_color


def get_and_validate_inner_fabric():
    """
    Inner fabric choice is collected, and validated in a while True loop
    with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not cotton or
    spinnaker a ValueError is raised.
    """
    while True:
        i_fabric = input(colored("What kind of inner fabric do you prefer, "
                                 "cotton or spinnaker? \n", "cyan")).lower()

        try:
            if i_fabric.isalpha():
                print(colored(f"\nYou chose {i_fabric} for the inside. "
                              "Good choice!\n", "green"))
                break
            if not i_fabric:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {i_fabric}, but we need a choice "
                                 "between cotton and spinnaker, "
                                 "in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return i_fabric


def get_and_validate_inner_color():
    """
    Inner color choice is collected, and validated in a while True loop
    with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not black or white
    a ValueError is raised.
    """
    while True:
        i_color = input(colored("Do you prefer the inner color to be "
                        "black or white? \n", "cyan")).lower()

        try:
            if i_color.isalpha():
                print(colored(f"\nYou chose {i_color} for the inside. "
                              "Perfect!\n", "green"))
                break
            if not i_color:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {i_color}, but we need a choice "
                                 "between black and white, in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return i_color


def get_and_validate_handle_fabric():
    """
    Fabric choice for the handles is collected, and validated in a while True
    loop with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not cotton or belt
    a ValueError is raised.
    """
    while True:
        h_fabric = input(colored("For the handles, would you like them to be "
                                 "made from cotton or belt? \n",
                                 "cyan")).lower()

        try:
            if h_fabric.isalpha():
                print(colored(f"\nYou chose {h_fabric} for the handles. "
                              "Great!\n", "green"))
                break
            if not h_fabric:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {h_fabric}, but we need a choice "
                                 "between cotton and belt, in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return h_fabric


def get_and_validate_handle_color():
    """
    Color choice for the handlesis collected, and validated in a while True
    loop with a break statement.
    The True loop makes sure the choice is in letters, and lower case.
    If choice is missing, is not in letters, or is not blue,
    white or grey a ValueError is raised.
    """
    while True:
        h_color = input(colored("Do you prefer the handle color to be "
                                "blue, white or grey? \n", "cyan")).lower()

        try:
            if h_color.isalpha():
                print(colored(f"\nYou chose {h_color} for the handles. "
                              "Stylish!\n", "green"))
                break
            if not h_color:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {h_color}, but we need a choice "
                                 "between blue, cream and grey, "
                                 "in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return h_color


def update_design_worksheet(o_color, o_fabric, i_color, i_fabric,
                            h_color, h_fabric):
    """
    Update the Google Sheets design worksheet with the collected choices of
    fabrics, colors and handles.
    """
    print("Your choices are being saved...\n")
    # Access Google Sheets worksheet
    design_worksheet = SHEET.worksheet("design")
    # The choices are saved in the design worksheet
    design_worksheet.append_row([o_color, o_fabric, i_color, i_fabric,
                                 h_color, h_fabric])
    print("Your choices have been saved successfully :-)\n")


def get_id_from_worksheet():
    """
    Get present id from ID worksheet.
    """
    all_ids = SHEET.worksheet("id").get_all_values()
    id_row = all_ids[-1]
    present_id = id_row[0]

    print(f"This is the previous bag ID: {present_id}\n")

    return present_id


def return_new_id_to_worksheet(present_id):
    """
    Increment present ID and pass new ID to worksheet.
    """
    new_id = present_id
    new_id = int(new_id) + 1

    print("Your bag ID is being created...\n")
    # Access Google Sheets worksheet
    design_worksheet = SHEET.worksheet("id")
    # The choices are saved in the design worksheet
    design_worksheet.append_row([new_id])
    print("Your bag ID has been saved successfully :-)\n")


def get_data_from_worksheets():
    """
    Get the data back from the Google Sheets name and design worksheets to
    thank the user for creating a bag with a selection of fabrics, colors
    and handles.
    """
    print("Your tote bag is now being designed...\n")
    all_names = SHEET.worksheet("name").get_all_values()
    your_name_row = all_names[-1]
    your_name = your_name_row[0]
    all_choices = SHEET.worksheet("design").get_all_values()
    choices_row = all_choices[-1]
    o_choice = choices_row[0] + " " + choices_row[1]
    i_choice = choices_row[2] + " " + choices_row[3]
    h_choice = choices_row[4] + " " + choices_row[5]
    print(colored(f"{your_name}, you have created your own cool tote bag "
                  f"with an outside of {o_choice}, an inside of {i_choice}, "
                  f"and {h_choice} handles.\n\n", "green"))
    print("     _______      ")
    print("     |     |      ")
    print("   -----------    ")
    print("  |           |   ")
    print("  |           |   ")
    print("  |           |   ")
    print("  |  My Tote  |   ")
    print("   -----------    \n\n")
    print(colored("Thank you for designing your bag with us!\n", "blue"))


def main():
    """
    Run all functions
    """
    intro()
    fname = get_and_validate_fname()
    full_name = get_and_validate_lname(fname)
    update_name_worksheet(full_name)
    o_fabric = get_and_validate_outer_fabric()
    o_color = get_and_validate_outer_color()
    i_fabric = get_and_validate_inner_fabric()
    i_color = get_and_validate_inner_color()
    h_fabric = get_and_validate_handle_fabric()
    h_color = get_and_validate_handle_color()
    update_design_worksheet(o_color, o_fabric, i_color, i_fabric,
                            h_color, h_fabric)
    present_id = get_id_from_worksheet()
    return_new_id_to_worksheet(present_id)
    get_data_from_worksheets()


main()
