from tkinter import *
from tkinter import ttk


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    Text_Input.set(operator)


def ClearDisplay():
    global operator
    operator = " "
    Text_Input.set("")



def btnEquliis():
    global operator
    sumps = str(eval(operator))
    Text_Input.set(sumps)


def close():
    exit()



root = Tk()
root.title("Calculator")
style = ttk.Style()
style.theme_use('classic')


style.configure('TButton', width=4, font=('arial', 20, 'bold'), height=12, bd=4)




operator = " "

Text_Input = StringVar()

Text_display = Entry(root,font=('arial', 20, 'bold'), width=25 ,textvariable=Text_Input ,insertwidth=4, justif='right', bd=12 )
Text_display.grid(columnspan=4,)

btnClear = ttk.Button(root, width=25, text=" C ", command=ClearDisplay).grid(columnspan=4, row=1, ipady=14)
ExitBtn = ttk.Button(root, width=25, text=" OFF ", command=lambda :close()).grid(columnspan=4, row=2, ipady=14)

# ===========  ROW NUMBER ONE  ====================
btn7 = ttk.Button(root,text=" 7 ", command=lambda: btnClick(7)).grid(row=3, column=0, ipady=14)
btn8 = ttk.Button(root,  text=" 8 ", command=lambda: btnClick(8)).grid(row=3, column=1, ipady=14)
btn9 = ttk.Button(root, text=" 9 ", command=lambda: btnClick(9)).grid(row=3, column=2,ipady=14)
addiction = ttk.Button(root, text=" + ", command=lambda: btnClick("+")).grid(row=3, column=3, ipady=14)
# =========== END ROW NUMBER ONE  =================

# ===========  ROW NUMBER TOO  ====================
btn4 = ttk.Button(root, text=" 4 ", command=lambda: btnClick(4)).grid(row=4, column=0, ipady=14)
btn5 = ttk.Button(root, text=" 5 ", command=lambda: btnClick(5)).grid(row=4, column=1, ipady=14)
btn6 = ttk.Button(root, text=" 6 ", command=lambda: btnClick(6)).grid(row=4, column=2, ipady=14)
Subtraction = ttk.Button(root,text=" - ", command=lambda: btnClick("-")).grid(row=4, column=3, ipady=14)
# =========== END ROW NUMBER TOO  =================

# ===========  ROW NUMBER TREE  ====================
btn1 = ttk.Button(root, text=" 1 ", command=lambda: btnClick(1)).grid(row=5, column=0, ipady=14)
btn2 = ttk.Button(root, text=" 2 ", command=lambda: btnClick(2)).grid(row=5, column=1, ipady=14)
btn3 = ttk.Button(root,  text=" 3 ", command=lambda: btnClick(3)).grid(row=5, column=2, ipady=14)
Multiyply = ttk.Button(root, text=" × ", command=lambda: btnClick("*")).grid(row=5, column=3, ipady=14)
# =========== END ROW NUMBER TREE  =================

# ===========  ROW NUMBER TOO  ====================
btn0 = ttk.Button(root, text=" 0 ", command=lambda: btnClick(0)).grid(row=6, column=0, ipady=14)
aa = ttk.Button(root ,text=" . ",command=lambda: btnClick(".")).grid(column=1, row=6, ipady=14)
btnEquals = ttk.Button(root, text=" = ", command=btnEquliis).grid(row=6, column=2, ipady=14)
Divistion = ttk.Button(root, text=" / ", command=lambda: btnClick("/")).grid(row=6, column=3, ipady=14)
# =========== END ROW NUMBER TOO  =================

root.mainloop()