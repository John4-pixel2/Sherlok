from text import AGENCY_INFO, CANT_FETCH_ADDRESS, CHOOSE_LOCATION, AGENCY_MESSAGE, EXPLAIN_MESSAGE, FILM_STUDIOS_INFO, FINAL_MESSAGE, FOLLOW_MESSAGE, HOME_ADDRESS_MESSAGE, HOME_MESSAGE, INTRO_MESSAGE, LAPD_INFO, LAPD_MESSAGE, MACHINE_INTRODUCTION_MESSAGE, MARILYNS_DEATH_INFO, NEWSPAPER_ARTICLE, STUDIO_INFO, STUDIO_MESSAGE, TALENT_AGENCY_INFO, TIME_MACHINE_MESSAGE, TIME_TRAVEL_MESSAGE, WELCOME_MESSAGE, FINAL_MESSAGE, SECOND_MESSAGE
import API
import time
import tkinter as tk
from PIL import Image, ImageTk


"""
def main():
  def create_button(frame, text, command):
      button = tk.Button(frame, text=text, command=command)
      button.pack(side=tk.LEFT, padx=10)


  def show_frame(frame):
      frame.pack(pady=10)


  def hide_frame(frame):
      frame.pack_forget()


  def secondary_action(action_text):
      main_text.config(text=action_text)
      hide_frame(secondary_frame)


  def newspaper_article():
      main_text.config(text=NEWSPAPER_ARTICLE)
      hide_frame(button_frame)
      show_frame(secondary_frame)


  def goodbye():
      main_text.config(text="Goodbye, thank you for using our application!")
      hide_frame(button_frame)
      show_frame(secondary_frame)


  # Main application setup
  root = tk.Tk()
  root.title("This game is brought to you by TJ-X")

  main_text = tk.Label(root, text=INTRO_MESSAGE, font=('Helvetica', 12))
  main_text.pack(pady=10)

  # Loading and displaying an image
  # image = Image.open("Presentation.jpg")
  # photo = ImageTk.PhotoImage(image)
  # image_label = tk.Label(root, image=photo)
  # image_label.pack(pady=20)

  button_frame = tk.Frame(root)
  button_frame.pack(pady=10)

  secondary_frame = tk.Frame(root)

  # Creating primary buttons
  create_button(button_frame, "Read the article?", newspaper_article)
  create_button(button_frame, "Skip article", goodbye) #not goodbye but the continue of the story


  # Creating secondary buttons
  create_button(secondary_frame, "Continue", lambda: secondary_action(INTRO_MESSAGE))
  create_button(secondary_frame, "Quit",goodbye)

  hide_frame(secondary_frame)  # Initially hide the secondary frame

  root.mainloop()


# def main():
#   play = True
#   while play:
#     gameplay.print_intro()
#     # UI.print_window('intro', INTRO_MESSAGE, {'1': 'continue', '2': 'exit game'})
#     gameplay.continue_or_exit()
#     gameplay.ask_if_read_article()
#     gameplay.continue_or_exit()
#     gameplay.ask_where_to_go()
#     gameplay.continue_or_exit()
#     gameplay.go_to_home()
#     print()
#     print("\033[95mGAME OVER\n")
#     ask_play_again = input("Do you want to play again? \033[32m")
#     print("\033[96m")
#     if ask_play_again == 'yes':
#       print("\033[00m")
#       play = True
#     elif ask_play_again == 'no':
#       print("Thanks for playing, goodbye!")
#       play = False
"""


#root = tk.Tk()
#root.title("This game is brought to you by TJ-X")

#main_text = tk.Label(root, text=INTRO_MESSAGE, font=('Helvetica', 12))
#main_text.pack(pady=10)


# The main window of the app
def initialize_frame(master, content, title, buttons, image_path=None):
    frame = tk.Frame(master, padx=10, pady=10, bg=master.cget("bg"))

    label = tk.Label(frame, text=title, font=('Times New Roman', 18, 'bold'), bg=master.cget("bg"), fg='grey')
    label.pack(pady=10)

    return frame
    
    #AddingBackround-Image in choosen frame
    if image_path:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        bg_image = tk.Label(frame, image=photo)
        bg_image.image = photo  # Keep a reference to the image
        bg_image.pack(fill='both', expand=True)
        
    return frame,label    
    
#Example
#frame1_title = initialize_frame(root, "Content 1", "Title 1", [("Button 1", command1)], image_path="image1.png-your image") 
#frame2_title = initialize_frame(root, "Content 2", "Title 2", [("Button 2", command2)], image_path="image2.png-your image")


def show_frame(frame1, frame2):
    if frame1 is not None:
        frame1.tkraise()

    for fr in [frame1, frame2]:
        if fr is not None:
            fr.pack_forget()
        fr.pack(expand=True, fill='both')
        
#Call the show_frame-Function with just a single argument
#frames = [frame1, frame2]
#The show_frame(frame1,frame2) will receive frame1 and frame2 as separate arguments
#Therefore You can call the function show_frame(frame1) also with just one argument.
 
frame1 = initialize_frame(root, "Frame 1 Content", "Frame 1 Title", [("Button1", lambda: print("Button 1 Clicked"))]) #feature you can add - image_path="image1.png") 
frame2 = initialize_frame(root, "Frame 2 Content", "Frame 2 Title", [("Button2", lambda: print("Button 2 Clicked"))]) #feature you can add- mage_path="image2.png")


#2 main Features of each Frame:

#1) Using Widgets in each Frame
#"Frame1 and/or Frame2 - Content" refer to the widgets and elements that will be displayed within the Frame

#2) Using a second Frame for each called Frame1 or Frame2 at the same time.
#"Frame1 and/or Frame2 - Title" is the title or heading displayed at the top of the frame.
#If you don't need the Frame 1 Content or Titel, you can simply pass an empty string "" or None as the second argument / or leave it empty. 

#Test the show_frame function
def show_frame(frame1, frame2): 
    if frame1 is not None: 
        frame1.tkraise()

#The show_frame function will receive frame1 and frame2 as separate arguments
#You can call the function show_frame() with just one argument (frame1).
frames = [frame1, frame2] 

#Example
#frame1 = initialize_frame(root, "Frame 1 Content", "Frame 1 Title", [("Button1", lambda: print("Button 1 Clicked"))])

#frame2 = initialize_frame(root, "Frame 2 Content", "Frame 2 Title", [("Button2", lambda: print("Button 2 Clicked"))])


#show_frame(frame1)
# original from 10. Juli
#def initialize_frame(master, content, title, buttons, image_path=None):
 #   frame = tk.Frame(master, padx=10, pady=10, bg=master.cget("bg"))
    
    #AddingBackround-Image
    #if image_path:
    #    image = Image.open(image_path)
    #    photo = ImageTk.PhotoImage(image)
    #    bg_image = tk.Label(frame, image=photo)
    #    bg_image.image = photo  # Keep a reference to the image
    #    bg_image.pack(fill='both', expand=True)

#Example
#frame1 = initialize_frame(root, "Content 1", "Title 1", [("Button 1", command1)], image_path="image1.jpg")
#frame2 = initialize_frame(root, "Content 2", "Title 2", [("Button 2", command2)], image_path="image2.jpg")
        
#label = tk.Label(frame, text=title, font=('Times New Roman', 18, 'bold'), bg=master.cget("bg"), fg='grey')
#label.pack(pady=10)


"""
def initialize_frame(root, info, buttons):
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap=tk.WORD)
    text.pack(fill=tk.BOTH, expand=True, )

    text.insert(tk.END, info)

    for button_text, command in buttons:
        button = tk.Button(frame, text=button_text, command=command)
        button.pack()

    return frame"""


#def show_frame(frame):
 #   if frame is not None:
  #      frame.tkraise()
   # """
   # Display the specified frame and hide all others.
    #"""
   # for fr in frames:
    #    if fr is not None:
     #       fr.pack_forget()
    #frame.pack(expand=True, fill='both')
        
       
#def show_final_frame(frame):
    #frame.tkraise()
    # """
    #Display the specified frame and shows the last frame at the same time.
    #"""
    #for fr in frames:
    #    fr.pack_forget()
    #frame.pack(expand=True, fill='both')


# Final Top Level Show Frame 
#def show_final_message():
 # final_message_frame = initialize_frame(root, "Play Again?", [("Play #Again", lambda: show_frame(intro_frame)), ("Quit Game", quit_game), #("Donate to Wikipedia", lambda: API.donate())])
#  final_message_frame.pack()

#intro_frame= tk.Frame(root)
#intro_label = tk.Label(intro_frame, text"=Welcome to to the Final #Message!")
#intro_label.pack()

# play_button= tk.Label(inro_frame, text="Play again!, command=show_final_message")

#frames.apped(intro_frame)
    

def quit_game():
    print("Quitting game...")
    root.destroy()

root = tk.Tk()
root.title("This game is brought to you by TJ-X")

# Main application window

# Frames for each stage of the game
frames = []

# Frame 1- Welcome Frame #with feature to import Image replace image1.jpg
welcome_frame = initialize_frame(root, WELCOME_MESSAGE, "Welcome", [("Start Game", lambda: show_frame(intro_frame))])
frames.append(welcome_frame)

#Frame 2- Intro Frame
intro_frame = initialize_frame(root, INTRO_MESSAGE, "Game Intro", [("Read Article", lambda: show_frame(newspaper_frame)), ("Skip Article", lambda: show_frame(machine_introduction_frame))])
frames.append(intro_frame)

# Frame 3 - Newspaper Frame
newspaper_frame = initialize_frame(root, NEWSPAPER_ARTICLE, "Newspaper Article", [("Continue", lambda: show_frame(machine_introduction_frame))])
frames.append(newspaper_frame)

# Frame 4 - Machine Introduction Frame
machine_introduction_frame = initialize_frame(root, MACHINE_INTRODUCTION_MESSAGE, "Time Machine Introduction", [("Do Some Research", lambda: show_frame(research_frame)), ("Go Back In Time", lambda: show_frame(time_travel_msg_frame))])
frames.append(machine_introduction_frame)

# Frame 4.1 - Research Frame
research_frame = initialize_frame(root, TIME_MACHINE_MESSAGE, "Research", [("Marilyn's Death", lambda: show_frame(marilyns_death_frame)), ("Marilyn's Talent Agency", lambda: show_frame(talent_agency_frame)), ("20th Century Fox Studios", lambda: show_frame(film_studios_frame)), ("Go Back To Machine Features", lambda: show_frame(machine_introduction_frame)), ("Change fetched Article Language", lambda: API.change_language())])
frames.append(research_frame)

# Frame 4.1.1 - Marilyn's Death Frame
marilyns_death_frame = initialize_frame(root, MARILYNS_DEATH_INFO, "Marilyn's Death", [("Go Back", lambda: show_frame(research_frame))])
#frames = [marilyns_death_frame]
frames.append(marilyns_death_frame)

# Frame 4.1.2 - Talent Agency Frame
talent_agency_frame = initialize_frame(root, TALENT_AGENCY_INFO, "Talent Agency", [("Go Back", lambda: show_frame(research_frame))])
frames.append(talent_agency_frame)

# Frame 4.1.3 - Film Studios
film_studios_frame = initialize_frame(root, FILM_STUDIOS_INFO, "Film Studios", [("Go Back", lambda: show_frame(research_frame))])
frames.append(film_studios_frame)

# Frame 4.2 - Time Travel msg frame
time_travel_msg_frame = initialize_frame(root, TIME_TRAVEL_MESSAGE, "Time Travel", [("Continue", lambda: show_frame(choose_location_frame))])
frames.append(time_travel_msg_frame)

# Frame 6 - Where To Go Msg Frame 
# Specific frame
choose_location_frame = initialize_frame(root, CHOOSE_LOCATION, "Where To Go?", [("Go to Her Agency", lambda: show_frame(agency_msg_frame)), ("Go to Hollywood", lambda: show_frame(studio_msg_frame)), ("Go to LA Police Department", lambda: show_frame(lapd_msg_frame)),("Go to Monroe's Home", lambda: show_frame(cant_fetch_address_frame))])
frames.append(choose_location_frame)

# Frame 6.0.1
cant_fetch_address_frame = initialize_frame(root, CANT_FETCH_ADDRESS, "Marilyn's Address", [("Go Back", lambda: show_frame(choose_location_frame))])
frames.append(cant_fetch_address_frame)

#Frame 6.1 - Agency Msg Frame
agency_msg_frame = initialize_frame(root, AGENCY_MESSAGE, "Talent Agecny", [("Keep Digging", lambda: show_frame(agency_info_frame)), ("Go Back", lambda: show_frame(choose_location_frame))])
frames.append(agency_msg_frame)

# Frame 6.2 - Agency Info
agency_info_frame = initialize_frame(root, AGENCY_INFO, "Talent Agency", [("Go Back", lambda: show_frame(choose_location_frame))])
frames.append(agency_info_frame)

# Frame 7 - Studio Msg Frame
studio_msg_frame = initialize_frame(root, STUDIO_MESSAGE, "Film Studios", [("Storm In", lambda: show_frame(studio_info_frame)), ("Go Back", lambda: show_frame(choose_location_frame))])    
frames.append(studio_msg_frame)

# Frame 7.1 - Studio Info
studio_info_frame = initialize_frame(root, STUDIO_INFO, "Film Studios", [("Go Back", lambda: show_frame(choose_location_frame))])
frames.append(studio_info_frame)

# Frame 8 - LAPD Msg Frame
lapd_msg_frame = initialize_frame(root, LAPD_MESSAGE, "LAPD", [("Insist", lambda: show_frame(home_address_frame)), ("Go Back", lambda: show_frame(choose_location_frame))])
frames.append(lapd_msg_frame)

# Frame 8.1 - LAPD Info
lapd_info_frame = initialize_frame(root, LAPD_INFO, "LAPD", [("Go To Marilyn's Home", lambda: show_frame(monroes_home_frame))])
frames.append(lapd_info_frame)

# Frame 9 - Home Address Frame
home_address_frame = initialize_frame(root, HOME_ADDRESS_MESSAGE, "LAPD", [("Go To Marilyn's Home", lambda: show_frame(monroes_home_frame))])
frames.append(home_address_frame)

# Frame 9.1 - Marilyn's Home Frame
monroes_home_frame = initialize_frame(root, HOME_MESSAGE, "Marylin's Home", [("Follow Me", lambda: show_frame(win_message_frame)), ("Explain", lambda: show_frame(lose_message_frame))])
frames.append(monroes_home_frame)

#Frame 10 - Lose Message
lose_message_frame = initialize_frame(root, EXPLAIN_MESSAGE, "Game Lost", [("Finish Game", lambda: show_frame(final_message_frame))])
frames.append(lose_message_frame)

#Frame 11 - Win Message
win_message_frame = initialize_frame(root, FOLLOW_MESSAGE, "Game Won", [("Finish Game", lambda: show_frame(image_frame))])
frames.append(win_message_frame)

#Frame 12 - Final Message
final_message_frame = initialize_frame(root, FINAL_MESSAGE, "Play Again?", [("Play Again", lambda: show_frame(intro_frame)), ("Quit Game", quit_game), ("Donate to Wikipedia", lambda: API.donate())])
frames.append(final_message_frame)

# Frame 13 - Image
image_frame = initialize_frame(root, FINAL_MESSAGE, "Play Again?", [("Play Again", lambda: show_frame(intro_frame)), ("Quit Game", quit_game), ("Donate to Wikipedia", lambda: API.donate())], image_path="Presentation2.png")
frames.append(image_frame)

# Start the game
show_frame(welcome_frame, None)

root.mainloop()


if __name__ == "__main__":
    
  main()
