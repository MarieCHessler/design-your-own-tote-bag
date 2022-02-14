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
    # Idea from ASCII ART https://patorjk.com/software/taag, but revised.
    print("""
     ______       _ __            ___
    (  /  _/_    ( /  )          ( / \ 
      /__ /  _    /--< __, _,     /  /_  (  o  _,  __
    _/(_)(__(/_  /__ /(_(_(_)_  (/\_/(/_/_)_(_(_)_/ /_
                           /|                  /|
                          (/                  (/ \n\n
    """)
    print(colored("Welcome to Tote Bag Design!\n", "blue"))
    print("Here you can custom design your tote bag.")
    print("We reuse old spinnakers, scrap furnishing fabrics, "
          "and belts, where you can choose from different fabrics "
          "and colors for the inside, the outside and the handles.\n")
    
    print("You can also pick up a previously made design "
          "with the design ID you get on creation.\n\n")

    time.sleep(3)


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
        choice_e = "E"
        choice_n = "N"
        try:
            if choice_e_or_n == choice_e:
                find_bag_design()
                break
            elif choice_e_or_n == choice_n:
                break
            elif choice_e_or_n != choice_e or choice_e_or_n != choice_n:
                raise ValueError("\nPlease enter E for existing or N for "
                                 "new.\n")
            else:
                raise ValueError("\nPlease enter E for existing or N for "
                                 "new.\n")
        except ValueError as e:
            print(f"{e}\n")

    return choice_e_or_n


def get_and_validate_fname():
    """
    Collect and validate user first name in a while True loop with a
    break statement.
    Make sure, using the True loop, the name is in letters, and starts
    with a capital letter.
    Raise ValueError if name is missing or is not in letters.
    """
    print(colored("\nOkay, let's start designing!\n", "blue"))

    while True:
        # Have user enter first name and make first letter capitalized.
        fname = input(colored("Please give us your first name: \n",
                              "cyan")).capitalize()

        try:
            # Make sure the name is in letters.
            if fname.isalpha():
                print()
                break
            if not fname:
                # State that no input has been made.
                print("\nSorry, we did not catch you first name.\n")
            else:
                # State that the input is incorrect.
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
        # Have user enter last name and make first letter capitalized.
        lname = input(colored("And your last name, please: \n",
                              "cyan")).capitalize()
        # Create full name from first and last name.
        full_name = fname + " " + lname

        try:
            # Make sure the name is in letters.
            if lname.isalpha():
                print(colored(f"\nWelcome {full_name}!\n", "green"))
                break
            if not lname:
                # State that no input has been made.
                print("\nSorry, we did not catch you last name.\n")
            else:
                # State that the input is incorrect.
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
    name_worksheet = SHEET.worksheet("name")  # Access Google Sheets worksheet.
    # Save the full name in the worksheet.
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
        # Define the allowed words to use.
        o_fabric_options = ["cotton", "linen", "denim"]
        # Have user enter fabric.
        o_fabric = input(colored("Would you like the outer fabric to be "
                                 "cotton, linen or denim? \n", "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right fabrics.
            if o_fabric.isalpha() and o_fabric in o_fabric_options:
                print(colored(f"\nYou chose {o_fabric} for the outside. "
                              "Nice!\n", "green"))
                break
            if not o_fabric:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
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
        # Define the allowed words to use.
        o_color_options = ["blue", "cream", "pink", "grey"]
        # Have user enter color.
        o_color = input(colored("Do you prefer the outer color to be "
                        "blue, cream, pink or grey? \n", "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right colors.
            if o_color.isalpha() and o_color in o_color_options:
                print(colored(f"\nYou chose {o_color} for the outside. "
                              "Looks good!\n", "green"))
                break
            if not o_color:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
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
        # Define the allowed words to use.
        i_fabric_options = ["cotton", "spinnaker"]
        # Have user enter fabric.
        i_fabric = input(colored("What kind of inner fabric do you prefer, "
                                 "cotton or spinnaker? \n", "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right fabrics.
            if i_fabric.isalpha() and i_fabric in i_fabric_options:
                print(colored(f"\nYou chose {i_fabric} for the inside. "
                              "Good choice!\n", "green"))
                break
            if not i_fabric:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
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
        # Define the allowed words to use.
        i_color_options = ["blue", "white", "black"]
        # Have user enter color.
        i_color = input(colored("Do you prefer the inner color to be "
                        "blue, white or black? \n", "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right colors.
            if i_color.isalpha() and i_color in i_color_options:
                print(colored(f"\nYou chose {i_color} for the inside. "
                              "Perfect!\n", "green"))
                break
            if not i_color:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
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
        # Define the allowed words to use.
        h_fabric_options = ["cotton", "belt"]
        # Have user enter fabric.
        h_fabric = input(colored("For the handles, would you like them to be "
                                 "made from cotton or belt? \n",
                                 "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right fabrics.
            if h_fabric.isalpha() and h_fabric in h_fabric_options:
                print(colored(f"\nYou chose {h_fabric} for the handles. "
                              "Great!\n", "green"))
                break
            if not h_fabric:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
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
        # Define the allowed words to use.
        h_color_options = ["blue", "white", "grey"]
        # Have user enter color.
        h_color = input(colored("Do you prefer the handle color to be "
                                "blue, white or grey? \n", "cyan")).lower()

        try:
            # Make sure the text is in letters and one of the right colors.
            if h_color.isalpha() and h_color in h_color_options:
                print(colored(f"\nYou chose {h_color} for the handles. "
                              "Stylish!\n", "green"))
                break
            if not h_color:
                # State that no input has been made.
                print("\nYou forgot to make a choice.\n")
            else:
                # State that the input is incorrect.
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
    # Access Google Sheets worksheet.
    design_worksheet = SHEET.worksheet("design")
    # Save the choices in the design worksheet.
    design_worksheet.append_row([o_color, o_fabric, i_color, i_fabric,
                                 h_color, h_fabric])
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
    # Access Google Sheets worksheet to get all values in worksheet.
    all_names = SHEET.worksheet("name").get_all_values()
    user_name_row = all_names[-1]  # Slice final item from the list.
    user_name = user_name_row[0]  # Select the first item from the row.

    # Access Google Sheets worksheet to get all values in worksheet.
    all_choices = SHEET.worksheet("design").get_all_values()
    choices_row = all_choices[-1]  # Slice final item from the list.
    # Select items from the row.
    o_choice = choices_row[0] + " " + choices_row[1]
    i_choice = choices_row[2] + " " + choices_row[3]
    h_choice = choices_row[4] + " " + choices_row[5]

    # Access Google Sheets worksheet to get all values in worksheet.
    all_unique_ids = SHEET.worksheet("unique_id").get_all_values()
    unique_id_row = all_unique_ids[-1]  # Slice final item from the list.
    unique_id = unique_id_row[0]  # Select the first item from the row.

    print(colored(f"You are a great designer {user_name}! Your own cool tote "
                  f"bag is made from an outside of {o_choice}, an inside "
                  f"of {i_choice}, and {h_choice} handles. Your unique design "
                  f"ID is {unique_id}, and you can use it to revisit your "
                  "design.\n\n", "green"))

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

    time.sleep(3)
    print(colored("If you want to design a new tote bag, click the "
                  "Run Program button above the window \n", "blue"))
    print(colored("Thank you for designing your bag with us!\n\n", "blue"))

    quit()


def find_bag_design():
    """
    Search for design ID in list of lists.
    Return a design info list using list comprehension and indexing.
    Create variables using indexing.
    """

    # Access Google Sheets worksheet to get all values in worksheet.
    all_info = SHEET.worksheet("all_info").get_all_values()
    # Have user enter unique ID
    id_to_find = input(colored("\nWant to see a present or previous design? "
                               "Enter your design ID: \n", "cyan"))

    # Get the correct row in the all values list, based on input value.
    design_info_row = [list for list in all_info if id_to_find in list]
    # Select the first item from the row.
    design_row = design_info_row[0]

    # Select items from the row.
    unique_id_design = design_row[1]
    name_design = design_row[2]
    o_design = design_row[3] + " " + design_row[4]
    i_design = design_row[5] + " " + design_row[6]
    h_design = design_row[7] + " " + design_row[8]
    
    not_in_design_row = [unique_id_design != id_to_find]

    if id_to_find in all_info:
        print(colored(f"\n{name_design}, your tote bag's outside is made "
                      f"of {o_design}, the inside is {i_design}, "
                      f"and the handles {h_design}. Looks very neat!"
                      "\n\n", "green"))
    else:
        print("ID does not exist")

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

    time.sleep(3)
    print(colored("If you want to design a new tote bag, click the "
                  "Run Program button above the window \n", "blue"))
    print(colored("Thank you for designing your bag with us!\n\n", "blue"))

    quit()


def main():
    """
    Run all functions
    """
    intro()
    new_or_existing_design()
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
