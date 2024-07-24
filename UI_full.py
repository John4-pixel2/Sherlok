import tkinter as tk
from tkinter import *
import random
from tkinter import PhotoImage


class GameInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Sherlock Holmes: The Marilyn Monroe Case - Game")
        self.root.geometry("800x600")

        self.current_view = 0

        self.views = [self.create_main_view, self.create_intro_view, self.create_scenarios_view, self.show_final_scenario_view]
        self.views[self.current_view]()

#Example 1: Main View
#The main view should display the background image, title, and a "Play Now" button.
#Expected Output: Main view with background image, title, and button. game.create_main_view()
 #   def create_main_view(self):
        background_image = tk.PhotoImage(file="Toolbox URL") #backround Picture
        background_label = tk.Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_label = tk.Label(self.root, text="Time Machine Adventure Game", font=("Helvetica", 24), bg="black", fg="white")
        title_label.place(relx=0.5, rely=0.4, anchor="center")

        play_button = tk.Button(self.root, text="Play Now", command=self.show_intro_view)
        play_button.place(relx=0.5, rely=0.6, anchor="center")

#The intro view should display the introduction text and a button to proceed to scenarios.
#Expected Output: Intro view with introduction text and button.
#game.create_intro_view()
    def show_intro_view(self):
        self.current_view += 1
        self.clear_view()
        self.views[self.current_view]()

    def create_intro_view(self):
        intro_label = tk.Label(self.root, text="Once upon a time...\nYou are a time traveler named Alex. Your mission is to save the world from destruction.", font=("Helvetica", 16))
        intro_label.pack()

        time_machine_button = tk.Button(self.root, text="Use Time Machine Now!", command=self.show_scenarios_view)
        time_machine_button.pack()

#Example 3: Scenarios View
#The scenarios view should display shuffled scenarios with entry fields for answers.
    def show_scenarios_view(self):
        self.current_view += 1
        self.clear_view()
        self.views[self.current_view]()

    def create_scenarios_view(self):
        scenarios = ["Scenario 1: Modeling Agency. You meet your future self. What do you say to him/her?",
                     "Scenario 2: Acting Theatre. You travel back to the dinosaur age. What dinosaur do you encounter?",
                     "Scenario 3: You land in ancient Egypt. How do you communicate with the locals?",
                     "Scenario 4: You find a treasure chest in the middle ages. What's inside?",
                     "Scenario 5: LA Police Department. What gift do you offer them?"]

#Expected Output: Scenarios view with shuffled scenarios and entry fields.
#game.create_scenarios_view()
        random.shuffle(scenarios)

        for scenario in scenarios:
            scenario_label = tk.Label(self.root, text=scenario, font=("Helvetica", 12))
            scenario_label.pack()

            answer_entry = tk.Entry(self.root)
            answer_entry.pack()

        final_scenario_button = tk.Button(self.root, text="Proceed to Final Scenario", command=self.show_final_scenario_view)
        final_scenario_button.pack()

#Example 4: Final Scenario View
#The final scenario view should compare user answers with correct answers and show message accordingly.
#Expected Output: Congratulations message if answers are correct, Oops message if answers are wrong.
#game.show_final_scenario_view()
    def show_final_scenario_view(self):
        answers = ["Hello, it's nice to meet you!", "Tyrannosaurus Rex", "Use hand gestures", "Gold coins", "Peace symbol"]
        user_answers = [entry.get() for entry in self.root.winfo_children() if isinstance(entry, tk.Entry)]

        if user_answers == answers:
            messagebox.showinfo("Congratulations", "You have successfully completed the game and saved Marilyn Monroe!")
        else:
            messagebox.showinfo("Oops", "You have entered the wrong answers.  Try again!")

    def clear_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game_interface = GameInterface(root)
    root.mainloop()
