"""
Import of time module to set times for pause.
Import of colorama and termcolor modules to be able to color text
and thus improve readability and accessibility for the user.
"""
import time
from colorama import init
from termcolor import colored

# Needed by Colorama and Termcolor to run on Windows.
init()


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

    print(colored("Welcome to Tote Bag Design!\n", "blue", attrs=["bold"]))

    print(colored("Here you can custom design your tote bag :-)\n\n"

          "We reuse old spinnakers, scrap furnishing fabrics, "
          "and belts,\n"
          "where you can choose from different fabrics "
          "and colors for the inside,\n"
          "the outside and the handles.\n\n"

          "You can also pick up a previously made design "
          "with the design ID you\n"
          "get on creation.\n\n", "blue"))

    time.sleep(6)
