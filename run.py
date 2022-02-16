"""
Import of gspread library and Credentials class from Google auth library
and wireup APIS, based on instructions from CI's Love Sandwiches project
Import of colorama module to be able to color text and thus improve
readability and accessibility for the user.
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
from validations import new_or_existing_design, get_and_validate_inner_color
from validations import input_and_validate_first_name, input_and_validate_last_name
from validations import 

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











def update_name_worksheet(full_name):
    """
    Update the Google Sheets name worksheet with the full name, using
    the append() method.
    """
    print("Your name is being saved...\n")

    # Access Google Sheets worksheet.
    name_worksheet = SHEET.worksheet("name")
    # Save the full name in the worksheet.
    name_worksheet.append_row([full_name])

    print("Now your name is in place. Thanks!\n\n")


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


def update_design_worksheet(outer_color, outer_fabric, inner_color,
                            inner_fabric, handle_color, handle_fabric):
    """
    Update the Google Sheets design worksheet with the collected choices of
    fabrics, colors and handles using the append() method.
    """
    print("\nYour design choices are being saved...\n")

    # Access Google Sheets worksheet.
    design_worksheet = SHEET.worksheet("design")
    # Save the choices in the design worksheet.
    design_worksheet.append_row([outer_color, outer_fabric, inner_color,
                                 inner_fabric, handle_color, handle_fabric])

    print("Your choices have been saved successfully.\n")


def get_design_no_from_worksheet():
    """
    Get present design number from the design no worksheet.
    """
    # Access Google Sheets worksheet to get all values in worksheet.
    all_nos = SHEET.worksheet("design_no").get_all_values()
    design_no_row = all_nos[-1]  # Slice final item from the list.
    present_no = design_no_row[0]  # Select the first item from the row.

    return present_no


def return_new_no_to_worksheet(present_no):
    """
    Increment the present design number by one, by creating a new
    design number variable, making it an integer and adding 1.
    Pass the new number to the worksheet.
    """
    new_no = present_no  # Create new design number variable from present.
    new_no = int(new_no) + 1  # Increment the new design number by one.

    print("A design number is being created...\n")

    # Access Google Sheets worksheet.
    design_no_worksheet = SHEET.worksheet("design_no")
    # Save the number in the design number worksheet.
    design_no_worksheet.append_row([new_no])

    print("The number has been saved successfully.\n")


def create_unique_id():
    """
    Remove white space between first and last name using the
    replace() method.
    Combine design number and full name to create a unique design ID.
    """
    # Access Google Sheets worksheet to get all values in worksheet.
    all_names = SHEET.worksheet("name").get_all_values()
    your_id_name_row = all_names[-1]  # Slice final item from the list.
    your_id_name = your_id_name_row[0].lower()  # Select the first item.
    youridname = your_id_name.replace(" ", "")  # Remove white space.

    # Access Google Sheets worksheet to get all values in worksheet.
    all_nos = SHEET.worksheet("design_no").get_all_values()
    design_no_row = all_nos[-1]  # Slice final item from the list.
    design_no = design_no_row[0]  # Select the first item from the row.
    # Create unique ID from name and design number.
    unique_new_id = youridname + design_no

    print("Your unique design ID is being created...\n")

    # Access Google Sheets worksheet.
    unique_id_worksheet = SHEET.worksheet("unique_id")
    # Save the unique ID in the unique ID worksheet.
    unique_id_worksheet.append_row([unique_new_id])

    print("Your unique design ID has been saved successfully\n\n")
    time.sleep(3)


def get_data_from_worksheets():
    """
    Get the data back from the Google Sheets name and design worksheets.
    Use slice and index methods to get the correct row and
    combine choices.
    Sum up the tote bag design, by showing the selection of fabrics, colors
    and handles, and the design ID to the user in a print statement.
    """
    print("Your tote bag is now being designed...\n\n")
    time.sleep(3)

    # Access Google Sheets worksheet to get all values in worksheet.
    all_names = SHEET.worksheet("name").get_all_values()
    user_name_row = all_names[-1]  # Slice final item from the list.
    user_name = user_name_row[0]  # Select the first item from the row.

    # Access Google Sheets worksheet to get all values in worksheet.
    all_choices = SHEET.worksheet("design").get_all_values()
    choices_row = all_choices[-1]  # Slice final item from the list.

    # Select items from the choices_row.
    # choices_row[0] = outer color, choices_row[1] = outer fabric
    # choices_row[2] = inner color, choices_row[3] = inner fabric
    # choices_row[4] = handle color, choices_row[5] = handle fabric
    outer_choice = choices_row[0] + " " + choices_row[1]
    inner_choice = choices_row[2] + " " + choices_row[3]
    handle_choice = choices_row[4] + " " + choices_row[5]

    # Access Google Sheets worksheet to get all values in worksheet.
    all_unique_ids = SHEET.worksheet("unique_id").get_all_values()
    unique_id_row = all_unique_ids[-1]  # Slice final item from the list.
    unique_id = unique_id_row[0]  # Select the first item from the row.

    print(colored(f"You are a great designer {user_name}!\n", "green"))
    print(colored(f"Your own cool tote bag is made from an outside of "
                  f"{outer_choice},", "green"))
    print(colored(f"an inside of {inner_choice}, and {handle_choice} handles.",
                  "green"))
    print(colored(f"The unique ID for your design is {unique_id}, and you can "
                  "use it to revisit", "green"))
    print(colored("your design.\n", "green"))

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
    print(colored("If you want to design a new tote bag, or look at a "
                  "previous one, you can do so", "blue"))
    print(colored("shortly, when you have been returned to the start "
                  "page.\n", "blue"))
    print(colored("Thank you for designing your bag with us!\n", "blue"))

    time.sleep(5)
    print(colored("You will now be returned to the start page.\n", "blue"))

    intro()


def find_bag_design():
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
    else:
        print("\nID does not exist.\n")

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
    handles_fabric = input_and_validate_handle_fabric()
    handles_color = input_and_validate_handle_color()
    update_design_worksheet(o_color, o_fabric, i_color, i_fabric,
                            h_color, h_fabric)
    present_no = get_design_no_from_worksheet()
    return_new_no_to_worksheet(present_no)
    create_unique_id()
    get_data_from_worksheets()
    find_bag_design()


main()
