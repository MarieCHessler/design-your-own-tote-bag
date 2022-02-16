from termcolor import colored
from constants import INNER_COLOR_OPTIONS
# from run import find_bag_design


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
