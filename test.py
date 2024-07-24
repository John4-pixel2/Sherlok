import tkinter as tk
from PIL import Image, ImageTk


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


def greet():
    main_text.config(text="Hello, welcome to our application!")
    hide_frame(button_frame)
    show_frame(secondary_frame)


def goodbye():
    main_text.config(text="Goodbye, thanks for using our application!")
    hide_frame(button_frame)
    show_frame(secondary_frame)


# Main application setup
root = tk.Tk()
root.title("Dynamic Button Application")

main_text = tk.Label(root, text="Please click a button...", font=('Helvetica', 16))
main_text.pack(pady=20)

# Loading and displaying an image
image = Image.open("Presentation.jpg")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

secondary_frame = tk.Frame(root)

# Creating primary buttons
create_button(button_frame, "Greet", greet)
create_button(button_frame, "Goodbye", goodbye)
create_button(button_frame, "test", goodbye)


# Creating secondary buttons
create_button(secondary_frame, "Follow-up 1", lambda: secondary_action("Secondary Action One triggered!"))
create_button(secondary_frame, "Follow-up 2", lambda: secondary_action("Secondary Action Two triggered!"))

hide_frame(secondary_frame)  # Initially hide the secondary frame

root.mainloop()