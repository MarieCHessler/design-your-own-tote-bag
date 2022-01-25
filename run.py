"""
Import of gspread library and Credentials class from Google auth library
and wireup APIS, based on instructions from CI's Love Sandwiches project
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('design_your_own_totebag')  # Access Google sheet


def intro():
    """
    Welcome and information on how to design your own bag
    """
    print(" ______       _ __            ___ ")                 
    print("(  /  _/_    ( /  )          ( / \ ")       
    print("  /__ /  _    /--< __, _,     /  /_  (  o  _,  __ ") 
    print("_/(_)(__(/_  /__ /(_(_(_)_  (/\_/(/_/_)_(_(_)_/ /_ ")
    print("                       /|                  /|")       
    print("                      (/                  (/ \n\n")    
    print("Welcome to Tote Bag Design!" 
          "Here you can create a custom design for your tote bag")

