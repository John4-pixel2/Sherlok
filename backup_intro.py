def print_welcome():
    welcome_message = "Welcome to Sherlock Holmes: Marilyn Monroe Case"
    border_length = len(welcome_message) + 4
    border = '*' * border_length
    print(border)
    print(f"* {welcome_message} *")
    print(border)


def print_sherlock():
    print("Sherlock Holmes, the genius detective, has a time machine. \n"
          "He uses it to travel back and forth through time to \n"
          "solve mysterious crimes marked as closed cases.\n")


def print_mission():
    print("Your mission is to find and save Marilyn Monroe.")


def print_time_machine():
    print(
        "The time machine can only provide the predicted time of death for someone. \n"
        "Any other information about where or how they die will be blacked out."
    )


def print_marilyn_case():
    print(
        "In Marilyn Monroe's case, because we don't know the exact location of her death, \n"
        "the time machine will drop you off at the park nearest to her home address."
    )


def print_how_to_save():
    print(
        "Once you find her before her predicted time of death, \n"
        "press the button on your time watch to bring her into your time machine. \n"
        "Once her death time passes, she will be saved.")


def print_warning():
    print("Remember, you have only one hour to stay in another time zone. \n"
          "After one hour, you will disappear from the universe \n"
          "and will never be able to return to earth.")


def print_updated_warning(time):
    print(
        f"Hurry up, you have Now only {time} minutes before you disappear form earth."
    )


def intro():
    print_welcome()
    print_sherlock()
    print_mission()
    print_time_machine()
    print_marilyn_case()
    print_how_to_save()
    print_warning()
    print_updated_warning()
