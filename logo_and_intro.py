"""
Import of time module to set times for pause.
Import of colorama and termcolor modules to be able to color text
and thus improve readability and accessibility for the user.
"""
import time
from colorama import init
from termcolor import colored

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