import API

WELCOME_MESSAGE = "Welcome to the Game! Click 'Start Game' to start."

INTRO_MESSAGE = """<<< Sherlock Holmes: Marilyn Monroe Case >>>\n
Sherlock Holmes, the genius consulting detective possesses the one and only time traveling machine. The detective travels back in time to solve mysterious cases. With the help of his time machine, Sherlock acquires crucial, yet sometimes questionable information. You take upon yourself the case of Marilyn Monroe; the mysterious death of the famous american figure that was officially signed off as a suicide. 

This time, you want to make your own research and gather your own leads in order to save the star's life.

Do you want to read a summary of the Wiki article about Marilyn Monroe's Death?."""

NEWSPAPER_ARTICLE = """Marilyn Monroe (June 1, 1926 – August 4, 1962) was an American actress and model. Known for playing comic 'blonde bombshell' characters, she became one of the most popular sex symbols of the 1950s and early 1960s. Marilyn contracted with the William Morris Agency in August 1945. The agency deemed Monroe's figure more suitable for pin-up than high fashion modeling at the time. One year later Marilyn signed a contract with 20th Century-Fox learning acting, singing, and dancing. Her contract was renewed in February 1947. On the evening of August 4, 1962, the American actress Marilyn Monroe died at age 36 of a 'barbiturate overdose' between 8:30 p.m. and 10:30 p.m. inside her home.

YOUR MISSION: FIND AND SAVE MARILYN!"""

MACHINE_INTRODUCTION_MESSAGE = """Here are your machine's features:

1. Research On Wikipedia
2. Initiate Time Travel

What would you like to do?"""

TIME_MACHINE_MESSAGE = """In your time machine, you have implemented a program that allows you to access information from present day Wikipedia,
the extremely trustworthy source of information that every great detective uses.

What would you like to read about?"""

RESEARCH_OPTIONS = """Here are some Wiki articles of interest,
which one would you like to read about?:"""

MARILYNS_DEATH_INFO = f"Fetching information about Marilyn's Death from Wikipedia...\n{API.fetch_summary('Death of Marilyn Monroe')}"

TALENT_AGENCY_INFO = f"Fetching information about Marilyn's Talent Agency prior to her death...\n{API.fetch_summary('William Morris Agency')}"

FILM_STUDIOS_INFO = f"Fetching information about 20th Century Fox Studios...\n{API.fetch_summary('20 Century Studios')}"

TIME_TRAVEL_MESSAGE = """You have succesfully traveled back in time!
Your location is: Barrington Recreation Center & Park.
Today's date is August 4, 1962, 2 hours before Marilyn's death."""

CHOOSE_LOCATION = """Start your Investigation, save Marilyn's life!

Where would you like to go to?"""

AGENCY_MESSAGE = f"Fetching Agency Adress:\n{API.get_address('William Morris Agency')}\n\nYou have decided to visit Marilyn's work place. You look around for her, but nothing's there."

AGENCY_INFO = """There's no one at the reception, but an employee walks up to you.
They're suspicious of your British accent. They condescendingly tell you Marilyn is a famous actress who works in Hollywood.
Perhaps you want to check there."""

STUDIO_MESSAGE = f"Fetching Studio Address:\n{API.get_address('20th Century Studios')}\n\nYou have arrived at 20th Century Fox Studios, where Marilyn has been working on her latest film prior to her mysterious death. You look around, but there's not a sign of Marilyn.\n\nDo you want to storm into one of the ongoing productions or go back?"

STUDIO_INFO = """You see the trailer park of the production of the movie 'Something's Got to Give'.
You storm into the trailer of director George Cukor and ask about Marilyn.
He tells you today is Marylin's day off. She hasn't been at work at all"""

LAPD_MESSAGE = f"Fetching LAPD Address:\n{API.get_address('Los Angeles Police Department')}\n\nYou have arrived at the LA Police Department.\nYou approach an officer, say that you are a private investigator and that you have reason to believe Marilyn Monroe is in danger. \nThe officer is suspicious of you and refuses to confirm or deny that she is aware of any existing threats to the star's life."

LAPD_INFO = f"The officer gives you Marilyn's home address:\n{API.get_address('Death of Marilyn Monroe')}"

CANT_FETCH_ADDRESS = """Whoops, your program couldn't find Marilyn's Address on her Wiki page!"""

HOME_ADDRESS_MESSAGE = f"The officer gave you Marilyn's address!\n{API.get_address('Death of Marilyn Monroe')}\n\nYou can now go to her home!"

HOME_MESSAGE = f"You have arrived at Monroe's Address:\n{API.get_address('Death of Marilyn Monroe')}\n\nHurry up, there is little time!\n\nYou can tell her to follow you if she wants to see another day,\nor explain to her that you are from the future and have come to save her life!\n\nWhat do you choose to do?"

FOLLOW_MESSAGE = """Marilyn trusts your confidence. She agrees to come with you. You managed to save her in the nick of time. Get her somewhere safe and call it a day.

Well Done!"""

EXPLAIN_MESSAGE = """Marilyn is deeply distressed. She doesn't believe you and storms out of the building. Upon escaping you, she runs into traffic and gets hit.

You have altered the time line but didn't save Marilyn."""

SECOND_MESSAGE = """"""

FINAL_MESSAGE = """Game over, would you like to play again?

Wikipedia has been a source of help on your investigation, consider donating to help keep it online!"""