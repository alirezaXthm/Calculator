from tkinter import *
from button import CalcButton
import re

calculator = Tk()
calculator.geometry('340x500')


mathemetical_list = list()
operators = list()
numbers = list()
alt = list()
cntr = 0
alt_revers = 1

def set_calculate(mathemetical_list):
    math_string = ''.join(mathemetical_list)
    if (re.search(r'[^0-9.]', math_string)) != None:
        span = re.search(r'[^0-9.]', math_string).span()
        match = math_string[span[0]:span[1]]

        operators.append(match)

        alt = list(math_string.split(match))
        
        for i in range(len(alt)):
            if  alt[i].isnumeric() or ("." in alt[i]):
                numbers.append(alt[i])
                
        if match == '+':
            print('plus')
        elif match == '-':
            print('minus')

        elif match == '×':
            print('multiple')

        elif match == '÷':
            print('divisoin')

        elif match == '.':
            print('dot')

        print(f'alt: {alt}')
        print(f'operators {operators}')
        print(f'numbers {numbers}')
        alt.pop(0)
        set_calculate(alt)
    return numbers, operators

print(set_calculate(mathemetical_list))
def do_0():
    print(button_0['text'])
    mathemetical_list.append(button_0['text'])

def do_1():
    print(button_1['text'])
    mathemetical_list.append(button_1['text'])

def do_2():
    print(button_2['text'])
    mathemetical_list.append(button_2['text'])

def do_3():
    print(button_3['text'])
    mathemetical_list.append(button_3['text'])

def do_4():
    print(button_4['text'])
    mathemetical_list.append(button_4['text'])
    
def do_5():
    print(button_5['text'])
    mathemetical_list.append(button_5['text'])

def do_6():
    print(button_6['text'])
    mathemetical_list.append(button_6['text'])

def do_7():
    print(button_7['text'])
    mathemetical_list.append(button_7['text'])

def do_8():
    print(button_8['text'])    
    mathemetical_list.append(button_8['text'])
    
def do_9():
    print(button_9['text'])    
    mathemetical_list.append(button_9['text'])

def plus():
    mathemetical_list.append(button_plus['text'])


def minus():
    mathemetical_list.append(button_minus['text'])


def multiple():
    mathemetical_list.append(button_multiple['text'])

def division():
    mathemetical_list.append(button_division['text'])

def dot():
    mathemetical_list.append(button_dot['text'])

def equals():
    set_calculate(mathemetical_list)



button_0 = (Button(calculator, text="0", command = do_0, font=('consolas', 20), bg='#85a885'))
button_0.grid(row=0, column=0)

button_1 = (Button(calculator, text="1", command = do_1, font=('consolas', 20), bg='#85a885'))
button_1.grid(row=0, column=1)

button_2 = (Button(calculator, text="2", command = do_2, font=('consolas', 20), bg='#85a885'))
button_2.grid(row=0, column=2)

button_3 = (Button(calculator, text="3", command = do_3, font=('consolas', 20), bg='#85a885'))
button_3.grid(row=1, column=0)

button_4 = (Button(calculator, text="4", command = do_4, font=('consolas', 20), bg='#85a885'))
button_4.grid(row=1, column=1)

button_5 = (Button(calculator, text="5", command = do_5, font=('consolas', 20), bg='#85a885'))
button_5.grid(row=1, column=2)

button_6 = (Button(calculator, text="6", command = do_6, font=('consolas', 20), bg='#85a885'))
button_6.grid(row=2, column=0)

button_7 = (Button(calculator, text="7", command = do_7, font=('consolas', 20), bg='#85a885'))
button_7.grid(row=2, column=1)

button_8 = (Button(calculator, text="8", command = do_8, font=('consolas', 20), bg='#85a885'))
button_8.grid(row=2, column=2)

button_9 = (Button(calculator, text="9", command = do_9, font=('consolas', 20), bg='#85a885'))
button_9.grid(row=3, column=1)

button_plus = (Button(calculator, text="+", command = plus, font=('consolas', 20), bg='#85a885'))
button_plus.grid(row=0, column=3)

button_minus = (Button(calculator, text="-", command = minus, font=('consolas', 20), bg='#85a885'))
button_minus.grid(row=1, column=3)

button_multiple = (Button(calculator, text="×", command = multiple, font=('consolas', 20), bg='#85a885'))
button_multiple.grid(row=2, column=3)

button_division = (Button(calculator, text="÷", command = division , font=('consolas', 20), bg='#85a885'))
button_division.grid(row=3, column=3)

button_dot = (Button(calculator, text=".", command = dot, font=('consolas', 20), bg='#85a885'))
button_dot.grid(row=3, column=0)

button_equals = (Button(calculator, text="=", command = equals, font=('consolas', 20), bg='#85a885'))
button_equals.grid(row=3, column=2)

calculator.mainloop()
