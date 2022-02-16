"""
Validate to make sure user input is correct
"""
import time
from termcolor import colored
from constants import NEW_DESIGN, EXISTING_DESIGN, OUTER_FABRIC_OPTIONS
from constants import OUTER_COLOR_OPTIONS, INNER_FABRIC_OPTIONS
from constants import INNER_COLOR_OPTIONS, HANDLE_FABRIC_OPTIONS
from constants import HANDLE_COLOR_OPTIONS
# from run import find_bag_design


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
                find_bag_design()
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
