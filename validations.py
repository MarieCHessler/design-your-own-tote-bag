"""
Validations made to make sure user input is correct
"""
import time
import gspread
from google.oauth2.service_account import Credentials
from colorama import init
from termcolor import colored
from constants import NEW_DESIGN, EXISTING_DESIGN, OUTER_FABRIC_OPTIONS
from constants import OUTER_COLOR_OPTIONS, INNER_FABRIC_OPTIONS
from constants import INNER_COLOR_OPTIONS, HANDLE_FABRIC_OPTIONS
from constants import HANDLE_COLOR_OPTIONS
from run import intro

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


def new_or_existing_design():
    """
    Let user choose between picking up his/her existing design
    or creating a new one.
    """
    while True:
        # Have user choose if he/she wants to pick up his/her existing design
        # or create a new one.
        choice_e_or_n = input(colored("Would you like to pick up your "
                                      "existing design, or create a new one?\n"
                                      "Enter E for existing or N for new: \n",
                                      "cyan")).upper()
        # Validate choice
        try:
            if choice_e_or_n == EXISTING_DESIGN:
                find_and_validate_bag_design()
                break
            elif choice_e_or_n == NEW_DESIGN:
                break
            else:
                raise ValueError("\nPlease enter E for existing or N for "
                                 "new.\n")
        except ValueError as e:
            print(f"{e}\n")

    return choice_e_or_n


def input_and_validate_first_name():
    """
    Collect and validate user first name in a while True loop with a
    break statement.
    Make sure, using the True loop, the name is in letters, and starts
    with a capital letter.
    Raise ValueError if name is missing or is not in letters.
    """
    print(colored("\n\nOkay, let's start designing!\n", "blue"))

    while True:
        # Have user enter first name and make first letter capitalized.
        first_name = input(colored("Please give us your first name: \n",
                                   "cyan")).capitalize()

        try:
            # Make sure the name is in letters.
            if first_name.isalpha():
                print()
                break
            if not first_name:
                # State that no input has been made.
                print("\nSorry, we did not catch you first name.\n")
            else:
                # State that the input is incorrect.
                raise ValueError(f"\nYou wrote {first_name}, but we need the "
                                 "name, and in letters please.\n")
        except ValueError as e:
            print(f"{e}\n")

    return first_name


def input_and_validate_last_name(first_name):
    """
    Collect and validate user last name in a while True loop with a
    break statement.
    Make sure, using the True loop, the name is in letters, and starts
    with a capital letter.
    Raise ValueError if name is missing or is not in letters.
    Create a full name by combining first and last name.
    """
    while True:
        # Have user enter last name and make first letter capitalized.
        last_name = input(colored("And your last name, please: \n",
                                  "cyan")).capitalize()
        # Create full name from first and last name.
        full_name = first_name + " " + last_name

        try:
            # Make sure the name is in letters.
            if last_name.isalpha():
                print(colored(f"\n\nWelcome {full_name}!\n\n", "green"))
                break
            if not last_name:
                # State that no input has been made.
                print("\nSorry, we did not catch you last name.\n")
            else:
                # State that the input is incorrect.
                raise ValueError(f"\nYou wrote {last_name}, but we need the "
                                 "name, and in letters please.\n")
        except ValueError as e:
            print(f"{e}\n")

    time.sleep(3)
    return full_name


def input_and_validate_outer_fabric():
    """
    Collect and validate outer fabric in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not cotton,
    linen or denim.
    """
    while True:
        # Have user enter fabric.
        outer_fabric = input(colored("Would you like the outer fabric to be "
                                     "cotton, linen or denim?\n",
                                     "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right fabrics.
            if outer_fabric.isalpha() and outer_fabric in OUTER_FABRIC_OPTIONS:
                print(colored(f"\nYou chose {outer_fabric} for the outside. "
                              "Nice!\n", "green"))
                break
            if not outer_fabric:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
                raise ValueError(f"\nYou wrote {outer_fabric}, but we need a "
                                 "choice between cotton, linen and denim, "
                                 "in letters please.\n")
        except ValueError as e:
            print(f"{e}\n")

    return outer_fabric


def input_and_validate_outer_color():
    """
    Collect and validate outer color in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not blue,
    cream, pink or grey.
    """
    while True:
        # Have user enter color.
        outer_color = input(colored("Do you prefer the outer color to be "
                                    "blue, cream, pink or grey? \n",
                                    "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right colors.
            if outer_color.isalpha() and outer_color in OUTER_COLOR_OPTIONS:
                print(colored(f"\nYou chose {outer_color} for the outside. "
                              "Looks good!\n", "green"))
                break
            if not outer_color:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
                raise ValueError(f"\nYou wrote {outer_color}, but we need a "
                                 "choice between blue, cream, pink and grey, "
                                 "in letters please.\n")
        except ValueError as e:
            print(f"{e}\n")

    return outer_color


def input_and_validate_inner_fabric():
    """
    Collect and validate inner fabric in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not cotton
    or spinnaker.
    """
    while True:
        # Have user enter fabric.
        inner_fabric = input(colored("What kind of inner fabric do you "
                                     "prefer, cotton or spinnaker?\n",
                                     "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right fabrics.
            if inner_fabric.isalpha() and inner_fabric in INNER_FABRIC_OPTIONS:
                print(colored(f"\nYou chose {inner_fabric} for the inside. "
                              "Good choice!\n", "green"))
                break
            if not inner_fabric:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
                raise ValueError(f"\nYou wrote {inner_fabric}, but we need a "
                                 "choice between cotton and spinnaker, "
                                 "in letters please.\n")
        except ValueError as e:
            print(f"{e}\n")

    return inner_fabric


def input_and_validate_inner_color():
    """
    Collect and validate inner color in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not blue,
    white or black.
    """
    while True:
        # Have user enter color.
        inner_color = input(colored("Do you prefer the inner color to be "
                                    "blue, white or black? \n",
                                    "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right colors.
            if inner_color.isalpha() and inner_color in INNER_COLOR_OPTIONS:
                print(colored(f"\nYou chose {inner_color} for the inside. "
                              "Perfect!\n", "green"))
                break
            if not inner_color:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
                raise ValueError(f"\nYou wrote {inner_color}, but we need a "
                                 "choice between blue, white and black, "
                                 "in letters please.\n")
        except ValueError as e:
            print(f"{e}\n")

    return inner_color


def input_and_validate_handle_fabric():
    """
    Collect and validate handle fabric in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not cotton,
    or belt.
    """
    while True:
        # Have user enter fabric.
        handle_fabric = input(colored("For the handles, would you like them "
                                      "to be made from cotton or belt? \n",
                                      "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right fabrics.
            if handle_fabric.isalpha() and handle_fabric in HANDLE_FABRIC_OPTIONS:
                print(colored(f"\nYou chose {handle_fabric} for the handles. "
                              "Great!\n", "green"))
                break
            if not handle_fabric:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
                raise ValueError(f"\nYou wrote {handle_fabric}, but we need a "
                                 "choice between cotton and belt, "
                                 "in letters please.\n")
        except ValueError as e:
            print(f"{e}\n")

    return handle_fabric


def input_and_validate_handle_color():
    """
    Collect and validate handle color in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not blue,
    white or grey.
    """
    while True:
        # Have user enter color.
        handle_color = input(colored("Do you prefer the handle color to be "
                                     "blue, white or grey? \n",
                                     "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right colors.
            if handle_color.isalpha() and handle_color in HANDLE_COLOR_OPTIONS:
                print(colored(f"\nYou chose {handle_color} for the handles. "
                              "Stylish!\n", "green"))
                break
            if not handle_color:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
                raise ValueError(f"\nYou wrote {handle_color}, but we need a "
                                 "choice between blue, white and grey, "
                                 "in letters please.\n")
        except ValueError as e:
            print(f"{e}\n")

    return handle_color


def find_and_validate_bag_design():
    """
    Search for design ID in list of lists.
    Return a design info list using list comprehension and indexing.
    Create variables using indexing.
    """

    # Access Google Sheets worksheet to get all values in worksheet.
    all_info = SHEET.worksheet("all_info").get_all_values()
    # Have user enter unique ID
    while True:
        id_to_find = input(colored("\nWant to see a present or previous "
                                   "design? Enter your design ID: \n", "cyan"))
        # Get the correct row in the all values list, based on input value.
        if design_info_row := [i for i in all_info if id_to_find in i]:
            break
        else:
            print("\nID does not exist.\n")
            time.sleep(3)
            new_or_existing_design()

    # Select the first item from the row.
    design_row = design_info_row[0]

    # Select items from the design_row.
    # name_design[2] = user name
    # design_row[3] = outer color, design_row[4] = outer fabric
    # design_row[5] = inner color, design_row[6] = inner fabric
    # design_row[7] = handle color, design_row[8] = handle fabric
    name_design = design_row[2]
    outer_design = design_row[3] + " " + design_row[4]
    inner_design = design_row[5] + " " + design_row[6]
    handle_design = design_row[7] + " " + design_row[8]

    # Handle correct and incorrect input
    if design_info_row[0]:
        print(colored(f"\n{name_design}, your tote bag's outside is made "
                      f"of {outer_design},", "green"))
        print(colored(f"the inside is {inner_design}, and the handles "
                      f"{handle_design}.", "green"))
        print(colored("Looks very neat!\n", "green"))

    print("""
        ____
        |  |
       ------
      |  My  |
      | Tote |
       ------   \n
    """)

    time.sleep(7)
    print(colored("If you want to design a new tote bag, you can do so "
                  "shortly, when you have", "blue"))
    print(colored("been returned to the start page.\n", "blue"))
    print(colored("Thank you for designing your bag with us!\n", "blue"))

    time.sleep(5)
    print(colored("You will now be returned to the start page.\n", "blue"))

    intro()
