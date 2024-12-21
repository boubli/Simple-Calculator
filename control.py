from tkinter import *
from tkinter import ttk
import math

# Function to handle button clicks
def btn_click(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)

# Function to clear the display
def clear_display():
    global operator
    operator = ""
    text_input.set("")

# Function to calculate the result
def btn_equals():
    global operator
    try:
        result = str(eval(operator))
        text_input.set(result)
        operator = result
    except Exception as e:
        text_input.set("Error")
        operator = ""

# Function to delete the last character
def backspace():
    global operator
    operator = operator[:-1]
    text_input.set(operator)

# Function to calculate the square root
def square_root():
    global operator
    try:
        result = str(math.sqrt(float(operator)))
        text_input.set(result)
        operator = result
    except Exception as e:
        text_input.set("Error")
        operator = ""

# Function to calculate percentage
def percentage():
    global operator
    try:
        result = str(eval(operator) / 100)
        text_input.set(result)
        operator = result
    except Exception as e:
        text_input.set("Error")
        operator = ""

# Function to close the application
def close():
    root.destroy()

# Initialize the main window
root = Tk()
root.title("Calculator")
root.geometry("400x600")

# Style configuration
style = ttk.Style()
style.theme_use('classic')
style.configure('TButton', width=4, font=('Arial', 20, 'bold'))

# Initialize operator and text input variable
operator = ""
text_input = StringVar()

# Display Entry
text_display = Entry(root, font=('Arial', 20, 'bold'), width=25, textvariable=text_input, insertwidth=4, justify='right', bd=12)
text_display.grid(row=0, column=0, columnspan=4, pady=10)

# Row for Clear and OFF buttons
btn_clear = ttk.Button(root, text="C", command=clear_display).grid(row=1, column=0, columnspan=2, ipadx=30, ipady=10)
btn_off = ttk.Button(root, text="OFF", command=close).grid(row=1, column=2, columnspan=2, ipadx=30, ipady=10)

# Row 2
btn7 = ttk.Button(root, text="7", command=lambda: btn_click(7)).grid(row=2, column=0, ipady=10)
btn8 = ttk.Button(root, text="8", command=lambda: btn_click(8)).grid(row=2, column=1, ipady=10)
btn9 = ttk.Button(root, text="9", command=lambda: btn_click(9)).grid(row=2, column=2, ipady=10)
btn_add = ttk.Button(root, text="+", command=lambda: btn_click("+")).grid(row=2, column=3, ipady=10)

# Row 3
btn4 = ttk.Button(root, text="4", command=lambda: btn_click(4)).grid(row=3, column=0, ipady=10)
btn5 = ttk.Button(root, text="5", command=lambda: btn_click(5)).grid(row=3, column=1, ipady=10)
btn6 = ttk.Button(root, text="6", command=lambda: btn_click(6)).grid(row=3, column=2, ipady=10)
btn_subtract = ttk.Button(root, text="-", command=lambda: btn_click("-")).grid(row=3, column=3, ipady=10)

# Row 4
btn1 = ttk.Button(root, text="1", command=lambda: btn_click(1)).grid(row=4, column=0, ipady=10)
btn2 = ttk.Button(root, text="2", command=lambda: btn_click(2)).grid(row=4, column=1, ipady=10)
btn3 = ttk.Button(root, text="3", command=lambda: btn_click(3)).grid(row=4, column=2, ipady=10)
btn_multiply = ttk.Button(root, text="\u00D7", command=lambda: btn_click("*")).grid(row=4, column=3, ipady=10)

# Row 5
btn0 = ttk.Button(root, text="0", command=lambda: btn_click(0)).grid(row=5, column=0, ipady=10)
btn_dot = ttk.Button(root, text=".", command=lambda: btn_click(".")).grid(row=5, column=1, ipady=10)
btn_equals = ttk.Button(root, text="=", command=btn_equals).grid(row=5, column=2, ipady=10)
btn_divide = ttk.Button(root, text="/", command=lambda: btn_click("/")).grid(row=5, column=3, ipady=10)

# Additional Buttons Row
btn_sqrt = ttk.Button(root, text="\u221A", command=square_root).grid(row=6, column=0, ipady=10)
btn_percent = ttk.Button(root, text="%", command=percentage).grid(row=6, column=1, ipady=10)
btn_backspace = ttk.Button(root, text="\u232B", command=backspace).grid(row=6, column=2, ipady=10)

# Run the application
root.mainloop()
