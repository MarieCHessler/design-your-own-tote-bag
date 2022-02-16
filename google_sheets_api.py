"""
Move data to and from worksheets in Google Sheets
"""
import time
import gspread
from google.oauth2.service_account import Credentials
from colorama import init
from termcolor import colored
from validations import new_or_existing_design

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
    print(colored("Thank you for designing your bag with us!\n\n", "blue"))
    time.sleep(5)

    print(colored("You will now be returned to the start page.\n\n", "blue"))
    time.sleep(3)

    new_or_existing_design()
