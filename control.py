from tkinter import *
from tkinter import ttk

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    Text_Input.set(operator)


def ClearDisplay():
    Text_Input.set(" ")


def btnEquliis():
    global operator
    sumps = str(eval(operator))
    Text_Input.set(sumps)





root = Tk()
root.title("Calculator")
style = ttk.Style()
style.configure('TButton', background="#0f5ddb")

operator = " "

Text_Input = StringVar()

Text_display = Entry(root, font=('arial', 20, 'bold'), textvariable=Text_Input, bd=30, insertwidth=4, bg='powder blue', justif='right')
Text_display.grid(columnspan=4)

# ===========  ROW NUMBER ONE  ====================
btn7 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 7 ", command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 8 ", command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 9 ", command=lambda: btnClick(9)).grid(row=1, column=2)
addiction = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" + ", command=lambda: btnClick("+")).grid(row=1, column=3)
# =========== END ROW NUMBER ONE  =================

# ===========  ROW NUMBER TOO  ====================
btn4 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 4 ", command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 5 ", command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 6 ", command=lambda: btnClick(6)).grid(row=2, column=2)
Subtraction = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" - ", command=lambda: btnClick("-")).grid(row=2, column=3)
# =========== END ROW NUMBER TOO  =================

# ===========  ROW NUMBER TREE  ====================
btn1 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 1 ", command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 2 ", command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 3 ", command=lambda: btnClick(3)).grid(row=3, column=2)
Multiyply = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" * ", command=lambda: btnClick("*")).grid(row=3, column=3)
# =========== END ROW NUMBER TREE  =================

# ===========  ROW NUMBER TOO  ====================
btn0 = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" 0 ", command=lambda: btnClick(0)).grid(row=4, column=0)
btnClear = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" C ", command= ClearDisplay).grid(row=4, column=1)
btnEquals = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" = ", command=btnEquliis).grid(row=4, column=2)
Divistion = Button(root, padx=23, fg='black', font=('arial', 20, 'bold'), text=" / ", command=lambda: btnClick("/")).grid(row=4, column=3)
# =========== END ROW NUMBER TOO  =================

root.mainloop()