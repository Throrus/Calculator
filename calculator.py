import tkinter as tk
from tkinter import font

# window setup
window = tk.Tk()
window.title("Calculator")
window.geometry('500x500')
window.resizable(0, 0)

# setting up the grid
rows = 0
while rows < 5:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows,weight=1)
    rows += 1

# font
font = font.Font(family='Helvetica', size=18, weight='bold')

# display field
display_text = tk.StringVar()
result_field = tk.Label(window, width = 25, height = 3, textvariable = display_text, font=font, fg = "black", bg = "white").grid(row = 0, columnspan = 3)

# arithmatic symbol
arith_symbol = "default"
result = 0

# value groups
num_set1 = ''
num_set2 = ''
float1 = False
float2 = False

# updating the arithmatic value
def update_symbol(sign):
    global arith_symbol
    global display_text
    if arith_symbol == 'default':
        arith_symbol = sign
        current = display_text.get()
        if sign == "add":
            current += " + "
        elif sign == "subtract":
            current += " - "
        elif sign == "multiply":
            current += " x "
        elif sign == "divide":
            current += " / "
        display_text.set(current)
    else:
        pass

# arithmatic functions
def calculate(arith_symbol, num_set1, num_set2, float1, float2):
    global result
    global display_text

    if float1 == True:
        num_set1 = float(num_set1)
    else:
        num_set1 = int(num_set1)
    if float2 == True:
        num_set2 = float(num_set2)
    else:
        num_set2 = int(num_set2)

    if arith_symbol == "add":
        result = (num_set1 + num_set2)
    elif arith_symbol == "subtract":
        result = (num_set1 - num_set2)
    elif arith_symbol == "multiply":
        result = (num_set1 * num_set2)
    elif arith_symbol == "divide":
        result = (num_set1 / num_set2)
    current = display_text.get()
    current = result
    display_text.set(current)



# functions that add the numbers
def add_num(num, arith_symbol):
    global display_text
    global num_set1
    global num_set2
    global float1
    global float2
    current = display_text.get()
    current += num
    display_text.set(current)
    if arith_symbol == 'default':
        num_set1 += num
        if num == ".":
            float1 = True
    else:
        num_set2 += num
        if num == ".":
            float2 = True


# clear the display
def clear():
    global display_text
    global arith_symbol
    global num_set1
    global num_set2
    current = display_text.get()
    current = ''
    display_text.set(current)
    arith_symbol = "default"
    num_set1 = ''
    num_set2 = ''

# button frame
class Calculator(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master)
        self.rowconfigure(0, minsize=kwargs.pop('height', None))
        self.columnconfigure(0, minsize=kwargs.pop('width', None))
        self.btn = tk.Button(self, **kwargs)
        self.btn.grid(row=0, column=0, sticky="nsew")
        self.config = self.btn.config

# number buttons
one = Calculator(window,text="1",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("1",arith_symbol)).grid(row=1, column=0)
two = Calculator(window,text="2",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("2",arith_symbol)).grid(row=1, column=1)
three = Calculator(window,text="3",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("3",arith_symbol)).grid(row=1, column=2)
four = Calculator(window,text="4",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("4",arith_symbol)).grid(row=2, column=0)
five = Calculator(window,text="5",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("5",arith_symbol)).grid(row=2, column=1)
six = Calculator(window,text="6",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("6",arith_symbol)).grid(row=2, column=2)
seven = Calculator(window,text="7",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("7",arith_symbol)).grid(row=3, column=0)
eight = Calculator(window,text="8",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("8",arith_symbol)).grid(row=3, column=1)
nine = Calculator(window,text="9",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("9",arith_symbol)).grid(row=3, column=2)
zero = Calculator(window,text="0",width=105, height=80 ,font=font, fg = "black", command = lambda: add_num("0",arith_symbol)).grid(row=4, column=1)

# math buttons
add_button = Calculator(window, width = 105, height = 80, text = "+", font=font, fg = "black", command = lambda: update_symbol("add")).grid(row = 1, column = 3)
sub_button = Calculator(window, width = 105, height = 80, text = "-", font=font, fg = "black", command = lambda: update_symbol("subtract")).grid(row = 2, column = 3)
mul_button = Calculator(window, width = 105, height = 80, text = "x", font=font, fg = "black", command = lambda: update_symbol("multiply")).grid(row = 3, column = 3)
div_button = Calculator(window, width = 105, height = 80, text = "/", font=font, fg = "black", command = lambda: update_symbol("divide")).grid(row = 4, column = 3)
dec_button = Calculator(window, width = 105, height = 80, text = ".", font=font, fg = "black", command = lambda: add_num(".", arith_symbol)).grid(row = 4, column = 0)
equ_button = Calculator(window, width = 105, height = 80, text = "=", font=font, fg = "black", command = lambda: calculate(arith_symbol, num_set1, num_set2, float1, float2)).grid(row = 4, column = 2)
clear_button = Calculator(window, width = 105, height = 80, text = "C", font=font, fg = "black", command = lambda: clear()).grid(row = 0, column = 3)

window.mainloop()
