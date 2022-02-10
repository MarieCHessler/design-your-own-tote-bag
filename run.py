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
    Collect and validate user first name in a while True loop with a
    break statement.
    Make sure, using the True loop, the name is in letters, and starts
    with a capital letter.
    Raise ValueError if name is missing or is not in letters.
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
    Collect and validate user last name in a while True loop with a
    break statement.
    Make sure, using the True loop, the name is in letters, and starts
    with a capital letter.
    Raise ValueError if name is missing or is not in letters.
    Create a full name by combining first and last name.
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
    Update the Google Sheets name worksheet with the full name, using
    the append() method.
    """
    print("Your name is being saved...\n")
    name_worksheet = SHEET.worksheet("name")  # Access Google Sheets worksheet
    # The name is saved in the worksheet
    name_worksheet.append_row([full_name])
    print("Now we have your name, thanks :-)\n")


def get_and_validate_outer_fabric():
    """
    Collect and validate outer fabric in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not cotton,
    linen or denim.
    """
    while True:
        o_fabric_options = ["cotton", "linen", "denim"]
        o_fabric = input(colored("Would you like the outer fabric to be "
                                 "cotton, linen or denim? \n", "cyan")).lower()

        try:
            if o_fabric.isalpha() and o_fabric in o_fabric_options:
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
    Collect and validate outer color in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not blue,
    cream, pink or grey.
    """
    while True:
        o_color_options = ["blue", "cream", "pink", "grey"]
        o_color = input(colored("Do you prefer the outer color to be "
                        "blue, cream, pink or grey? \n", "cyan")).lower()

        try:
            if o_color.isalpha() and o_color in o_color_options:
                print(colored(f"\nYou chose {o_color} for the outside. "
                              "Looks good!\n", "green"))
                break
            if not o_color:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {o_color}, but we need a choice "
                                 "between blue, cream, pink and grey, "
                                 "in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return o_color


def get_and_validate_inner_fabric():
    """
    Collect and validate inner fabric in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not cotton
    or spinnaker.
    """
    while True:
        i_fabric_options = ["cotton", "spinnaker"]
        i_fabric = input(colored("What kind of inner fabric do you prefer, "
                                 "cotton or spinnaker? \n", "cyan")).lower()

        try:
            if i_fabric.isalpha() and i_fabric in i_fabric_options:
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
    Collect and validate inner color in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not blue,
    white or black.
    """
    while True:
        i_color_options = ["blue", "white", "black"]
        i_color = input(colored("Do you prefer the inner color to be "
                        "blue, white or black? \n", "cyan")).lower()

        try:
            if i_color.isalpha() and i_color in i_color_options:
                print(colored(f"\nYou chose {i_color} for the inside. "
                              "Perfect!\n", "green"))
                break
            if not i_color:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {i_color}, but we need a choice "
                                 "between blue, white and black, in letters "
                                 "please.")
        except ValueError as e:
            print(f"{e}\n")

    return i_color


def get_and_validate_handle_fabric():
    """
    Collect and validate handle fabric in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not cotton,
    or belt.
    """
    while True:
        h_fabric_options = ["cotton", "belt"]
        h_fabric = input(colored("For the handles, would you like them to be "
                                 "made from cotton or belt? \n",
                                 "cyan")).lower()

        try:
            if h_fabric.isalpha() and h_fabric in h_fabric_options:
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
    Collect and validate handle color in a while True loop with a
    break statement.
    Make sure, using the True loop, the choice is the correct word, in letters,
    and lower case.
    Raise ValueError if choice is missing, is not in letters, or is not blue,
    white or grey.
    """
    while True:
        h_color_options = ["blue", "white", "grey"]
        h_color = input(colored("Do you prefer the handle color to be "
                                "blue, white or grey? \n", "cyan")).lower()

        try:
            if h_color.isalpha() and h_color in h_color_options:
                print(colored(f"\nYou chose {h_color} for the handles. "
                              "Stylish!\n", "green"))
                break
            if not h_color:
                print("\nYou forgot to make a choice.\n")
            else:
                raise ValueError(f"You wrote {h_color}, but we need a choice "
                                 "between blue, white and grey, "
                                 "in letters please.")
        except ValueError as e:
            print(f"{e}\n")

    return h_color


def update_design_worksheet(o_color, o_fabric, i_color, i_fabric,
                            h_color, h_fabric):
    """
    Update the Google Sheets design worksheet with the collected choices of
    fabrics, colors and handles using the append() method.
    """
    print("Your design choices are being saved...\n")
    # Access Google Sheets worksheet
    design_worksheet = SHEET.worksheet("design")
    # The choices are saved in the design worksheet
    design_worksheet.append_row([o_color, o_fabric, i_color, i_fabric,
                                 h_color, h_fabric])
    print("Your choices have been saved successfully.\n")


def get_design_no_from_worksheet():
    """
    Get present design number from the design no worksheet.
    """
    all_nos = SHEET.worksheet("design_no").get_all_values()
    design_no_row = all_nos[-1]  # Slice final item from the list
    present_no = design_no_row[0]

    return present_no


def return_new_no_to_worksheet(present_no):
    """
    Increment the present design number by one, to create a
    new number.
    Pass the new number to the worksheet.
    """
    new_no = present_no
    new_no = int(new_no) + 1

    print("A design number is being created...\n")
    # Access Google Sheets worksheet
    design_no_worksheet = SHEET.worksheet("design_no")
    # The number is saved in the id worksheet
    design_no_worksheet.append_row([new_no])
    print("The number has been saved successfully.\n")


def create_unique_id():
    """
    Remove white space between first and last name using the
    replace() method.
    Combine design number and full name to create a unique design ID.
    """
    all_names = SHEET.worksheet("name").get_all_values()
    your_id_name_row = all_names[-1]  # Slice final item from the list
    your_id_name = your_id_name_row[0].lower()
    youridname = your_id_name.replace(" ", "")

    all_nos = SHEET.worksheet("design_no").get_all_values()
    design_no_row = all_nos[-1]  # Slice final item from the list
    design_no = design_no_row[0]

    unique_new_id = design_no + youridname
    print("Your unique design ID is being created...\n")
    # Access Google Sheets worksheet
    unique_id_worksheet = SHEET.worksheet("unique_id")
    # The unique ID is saved in the unique ID worksheet
    unique_id_worksheet.append_row([unique_new_id])
    print("Your unique design ID has been saved successfully\n")


def get_data_from_worksheets():
    """
    Get the data back from the Google Sheets name and design worksheets.
    Use slice and index methods to get the correct row and
    combine choices.
    Sum up the tote bag design, by showing the selection of fabrics, colors
    and handles, and the design ID to the user in a print statement.
    """
    print("Your tote bag is now being designed...\n")
    all_names = SHEET.worksheet("name").get_all_values()
    user_name_row = all_names[-1]  # Slice final item from the list
    user_name = user_name_row[0]

    all_choices = SHEET.worksheet("design").get_all_values()
    choices_row = all_choices[-1]  # Slice final item from the list
    o_choice = choices_row[0] + " " + choices_row[1]
    i_choice = choices_row[2] + " " + choices_row[3]
    h_choice = choices_row[4] + " " + choices_row[5]

    all_unique_ids = SHEET.worksheet("unique_id").get_all_values()
    unique_id_row = all_unique_ids[-1]  # Slice final item from the list
    unique_id = unique_id_row[0]

    print(colored(f"You are a great designer {user_name}! Your own cool tote "
                  f"bag is made from an outside of {o_choice}, an inside "
                  f"of {i_choice}, and {h_choice} handles. Your unique design "
                  f"ID is {unique_id}, and you can use it to see your design."
                  "\n\n", "green"))

    print("""
         _______
         |     |
       -----------
      |           |
      |           |
      |           |
      |  My Tote  |
       -----------    \n\n
    """)

    print(colored("Thank you for designing your bag with us!\n\n", "blue"))


def find_bag_design():
    """
    Search for design ID in list of lists.
    Return a design info list using list comprehension and indexing.
    Create variables using indexing.
    """
    all_info = SHEET.worksheet("all_info").get_all_values()
    id_to_find = input(colored("Want to see a present or previous design? "
                               "Enter your design ID: \n", "cyan"))

    # Tip from tutor on different ways to go about using the ID to extract
    # the correct list
    design_info_row = [list for list in all_info if id_to_find in list]
    design_row = design_info_row[0]

    unique_id_design = design_row[1]
    name_design = design_row[2]
    o_design = design_row[3] + " " + design_row[4]
    i_design = design_row[5] + " " + design_row[6]
    h_design = design_row[7] + " " + design_row[8]

    print(colored(f"\n{name_design}, your design ID number is "
                  f"{unique_id_design}. The bag is made from an "
                  f"outside of {o_design}, an inside of {i_design}, "
                  f"and {h_design} handles. Looks very neat!"
                  "\n\n", "green"))


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
    present_no = get_design_no_from_worksheet()
    return_new_no_to_worksheet(present_no)
    create_unique_id()
    get_data_from_worksheets()
    find_bag_design()


main()
