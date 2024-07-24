import tkinter as tk
import Text



# The main window of the app
def initialize_frame(master, content, buttons):
    frame = tk.Frame(master, padx=20, pady=20)
    label = tk.Label(frame, text=content, font=('Helvetica', 12))
    label.pack(pady=10)

    for text, command in buttons:
        button = tk.Button(frame, text=text, command=command)
        button.pack(pady=5, fill='x')

    frame.pack_forget()
    return frame

#John: Can we enumerate different frames to call them?
#list_of_frames=[]

def show_frame(frame):
    """
    Display the specified frame and hide all others.
    """
    for fr in frames:
        fr.pack_forget()
    frame.pack(expand=True, fill='both')


def quit_game():
    print("Quitting game...")
    root.destroy()


# Main application window
root = tk.Tk()
root.title("This game is brought to you by TJ-X")

# Frames for each stage of the game
frames = []

# Welcome frame with a 'Continue' button
welcome_text = "Welcome to the Game! Click 'Continue' to learn more about the game."
welcome_frame = initialize_frame(root, welcome_text, [("Continue", lambda: show_frame(description_frame))])
frames.append(welcome_frame)

# Description frame with 'Continue' or 'Quit' options
description_text = "You are about to start a challenging adventure. Do you wish to continue or quit?"
description_frame = initialize_frame(root, description_text, [("Continue", lambda: show_frame(level_one_frame)),
                                                              ("Quit", quit_game)])
frames.append(description_frame)

# Level One with different actions
level_one_text = "Level One: Choose your path. Each choice leads to different outcomes."
level_one_frame = initialize_frame(root, level_one_text, [("Option A", lambda: show_frame(option_a_frame)),
                                                          ("Option B", lambda: show_frame(option_b_frame))])
frames.append(level_one_frame)

# Outcome for Option A
option_a_text = "You chose Option A. This leads to a new challenge."
option_a_frame = initialize_frame(root, option_a_text, [("Continue", lambda: show_frame(level_two_frame)),
                                                        ("Quit", quit_game)])
frames.append(option_a_frame)

# Outcome for Option B
option_b_text = "You chose Option B. This leads to an alternative path."
option_b_frame = initialize_frame(root, option_b_text, [("Continue", lambda: show_frame(level_two_frame)),
                                                        ("Quit", quit_game)])
frames.append(option_b_frame)

# Level Two with more decisions
level_two_text = "Level Two: Final stage. Choose wisely to conclude the game."
level_two_frame = initialize_frame(root, level_two_text, [("Finish A", lambda: show_frame(conclusion_frame_a)),
                                                          ("Finish B", lambda: show_frame(conclusion_frame_b))])
frames.append(level_two_frame)

# Conclusion for Finish A
conclusion_text_a = "Congratulations, you've completed the game through Path A!"
conclusion_frame_a = initialize_frame(root, conclusion_text_a, [("Quit", quit_game)])
frames.append(conclusion_frame_a)

# Conclusion for Finish B
conclusion_text_b = "Congratulations, you've completed the game through Path B!"
conclusion_frame_b = initialize_frame(root, conclusion_text_b, [("Quit", quit_game)])
frames.append(conclusion_frame_b)

# Start the game
show_frame(welcome_frame)

root.mainloop()
