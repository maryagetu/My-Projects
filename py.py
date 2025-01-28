#this is the code that i write .this have a function of calculator using python language



import tkinter as tk#import Tkinter module and  use tk as shorthand
from tkinter import *

# Initialize Tkinter window
root = Tk()
root.title("Simple Calculator")#sets the title of the window as simple calculator
root.geometry("570x600+300+100")#size of window 570*600 pixels on position (300,100)
root.resizable(False, False)#prevent from being resized
root.configure(bg="#17161b")#set back ground color to the dark shade

# Result display label
label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

# Function to update the label with button press
def click(event):#defines a function to handel button clicks
    text = event.widget.cget("text")#retrieve the text on the clicks button
    if text == "=":
        try:
            result = str(eval(label_result['text']))
            label_result['text'] = result
        except Exception as e:
            label_result['text'] = "Error"
    elif text == "C":#checks if the "c"button was clicked and clears the label
        label_result['text'] = ""
    else:#if any other button is clicked appends the button text to the current text.
        label_result['text'] += text

# Button frame to group buttons together
button_frame = Frame(root, bg="#17161b")#create a frame widget to contain the buttons ad set background color.
button_frame.pack()#add the frame to the window.

# Adding buttons
buttons = [
    '7', '8', '9', 'C',
    '4', '5', '6', '/',
    '1', '2', '3', '*',
    '0', '.', '=', '+',
    '-', '(', ')'
]

row = 0  #initialize row and columns counters for button placement.
col = 0

for button in buttons:  #iterates through the list of button labels.
    b = Button(button_frame, text=button, width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5")
    b.grid(row=row, column=col, padx=10, pady=10)
    b.bind("<Button-1>", click)  #blinds the click event to the click function.
    col += 1  #moves to the next column
    if col > 3:
        col = 0
        row += 1

# Main loop to run the application
root.mainloop()  #starts the main event loop ,wait for user interactions
