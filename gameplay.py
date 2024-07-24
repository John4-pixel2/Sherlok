from Text import AGENCY_MESSAGE, EXPLAIN_MESSAGE, FOLLOW_MESSAGE, HOME_MESSAGE, INTRO_MESSAGE, LAPD_MESSAGE, NEWSPAPER_ARTICLE, PRESSURE_MESSAGE, STUDIO_MESSAGE, TIME_MACHINE_MESSAGE, TIME_TRAVEL_MESSAGE
import API
import time


def continue_or_exit():
  continue_or_quit = input("\033[47mEnter to continue or 'quit' to exit ")
  print("\033[00m" + "\033[40m")
  if continue_or_quit == 'quit':
    print('\033[40m', end='')
    quit()


def print_intro():
  print(INTRO_MESSAGE)


def ask_if_read_article():
  user_input = input("Would you like to read the newspaper article about Marilyn Monroe's death? (yes/no) \033[32m")
  print("\033[00m")
  if user_input == 'yes':
    print(API.get_death_summary())
    print()

  elif user_input == 'no':
    pass

def initiate_time_travel():
  print()
  print(TIME_TRAVEL_MESSAGE)


def introduce_time_machine():
  print(TIME_MACHINE_MESSAGE)


def ask_where_to_go():
  print("\033[35mIt's time for you to investigate!\n")
  while True:
    print("\033[36mWhere would you like to go?")
    print("1. Talent Agency")
    print("2. Film Studios")
    print("3. Marilyn's Home")
    print("4. LA Police Department\n")
    user_choice = input("Enter your choice (1/2/3/4): \033[32m")
    print("\033[00m")
    if user_choice == '1':
      print("Here's the address of her talent agency:")
      print(API.get_address("William Morris Agency"))
      print()
      print(AGENCY_MESSAGE)
      print()
      ask_info_at_agency()
      continue
    elif user_choice == '2':
      print("Here's the address of 20th Century Fox Studios:")
      print(API.get_address("20th Century Studios"))
      print()
      print(STUDIO_MESSAGE)
      print()
      ask_info_at_studio()
      continue
    elif user_choice == '3':
      print("You don't know Marilyn's address!")
      print()
      continue
    
    elif user_choice == '4':
      print("Here's the address of the Los Angeles Police Department:")
      print(API.get_address("Los Angeles Police Department"))
      print()
      print(LAPD_MESSAGE)
      print()
      ask_info_at_lapd()
      break
      
    else:
      print("Please choose 1/2/3/4")
    


def ask_info_at_agency():
  choice = input("Ask someone for information or leave to the next place? (ask/leave): \033[32m").strip().lower()
  print("\033[00m")
  if choice == "ask":
      print("There was no one at the reception, but an employee walks up to you. They're suspicious of your British accent. They tell you Marilyn is a famous actress who works in Hollywood. Maybe you want to check there.")
      print()
  elif choice == "leave":
      print("You can pick a different scene.")
  else:
      print("Invalid choice. Please type 'ask' or 'leave'.")


def ask_info_at_studio():
  choice = input("Storm into one of the on going productions or leave to the next place? (storm/leave): \033[32m").strip().lower()
  print("\033[00m")
  if choice == "storm":
      print("You walk up to director George Cukor and ask about Marilyn. He tells you today is Marylin's day off. She hasn't been at work at all.")
      print()
  elif choice == "leave":
      print("You can pick a different scene.")
  else:
      print("Invalid choice. Please type 'ask' or 'leave'.")


def ask_info_at_lapd():
  choice = input("Ask for further information or leave to the next place? (ask/leave): \033[32m").strip().lower()
  print("\033[00m")
  if choice == "ask":
    print("The officer gives you Marilyn's home address:")
    print(API.get_address("Death of Marilyn Monroe"))
    print()
  elif choice == "leave":
      ask_where_to_go()
  else:
      print("Invalid choice. Please type 'ask' or 'leave'.")


def go_to_home():
  print(HOME_MESSAGE)
  print()
  print(PRESSURE_MESSAGE)
  print()
  user_input = input("(follow/explain): \033[32m")
  print("\033[00m")
  if user_input == 'explain':
    print(EXPLAIN_MESSAGE)
  elif user_input == 'follow':
    print(FOLLOW_MESSAGE)
  else:
    print("Hurry up! What will it be?")
    go_to_home()
    

import time


"""
# Comment Xhefri:
import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
from bs4 import BeautifulSoup

# Creating the main window
root = tk.Tk()
root.title("Sherlock Holmes: The Marilyn Monroe Case")
root.geometry("800x600")

# Defining scenarios
scenarios = ["Modeling Agency", "Acting Theater", "LA Police Department"]
# scenario Marylin's Address unlocked after going to the police and the other scenarios
# Create a label
label = tk.Label(root, text="Choose a Scenario", font=("Helvetica", 16))
label.pack(pady=10)

# Create a listbox to display scenarios
scenario_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 14))
for scenario in scenarios:
    scenario_listbox.insert(tk.END, scenario)
scenario_listbox.pack(pady=10, expand=True, fill=tk.BOTH)

# Create a text area for displaying data
data_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 12))
data_text.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)
"""
"""
1. TODO add the function to get the links of the scenarios
"""
"""
# # Here you go: (from Tom)
# from API import get_studio_address, get_url
# # get_url(title -> str) returns url
# from API import get_lapd_address
# # get_address("Los Angeles Police Department") returns address as str
# from API import get_home_address
# # get_home_address() returns address as str
# from API import get_agency_address
# # get_agency_address() returns modelling agency address as str

# Creating a button to confirm the selection
# select_button = tk.Button(root, text="Select Scenario", command=select_scenario, font=("Helvetica", 12))
# select_button.pack(pady=20)

# Run the application
root.mainloop()
# TODO: 1. add the url coresponding to the scenario. 
#       2. add story(hints)/ interaction for the player
#       3. show the remainig choices the user has.

"""