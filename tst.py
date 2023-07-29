# math_label = Label(calculator, text='')
import re
import string

# def do():
    # print(button.cget('text'))
    # pass
#     alt = math_label.cget('text')
#     alt += str(buttons[0].cget('text'))
#     math_label.config(text=alt)
    # print(f"str(button.cget('text')) : { str(buttons[0].cget('text')) }")
#     print(math_label)

# buttons = list()
# for i in range(10):
#     button = CalcButton(calculator, text=i, command=do, bg='#47b39d', fg = '#252e25', font=('consolas', 20))
#     buttons.append(button.button)
# print(buttons)
# frame = Frame(calculator)
# print(buttons[0].cget('text'))

            
# buttons[0].grid(row=0, column=0)
# buttons[1].grid(row=0, column=1)
# buttons[2].grid(row=0, column=2)
# buttons[3].grid(row=1, column=0)
# buttons[4].grid(row=1, column=1)
# buttons[5].grid(row=1, column=2)
# buttons[6].grid(row=2, column=0)
# buttons[7].grid(row=2, column=1)
# buttons[8].grid(row=2, column=2)
# buttons[9].grid(row=3, column=1)
# buttons.append(Button(calculator, text=".", font=('consolas', 20), bg='#bcccbc'))
# buttons[10].grid(row=0, column=3)
# buttons.append(Button(calculator, text="=", font=('consolas', 20), bg='#bcccbc'))
# buttons[11].grid(row=1, column=3)
# buttons.append(Button(calculator, text="+", font=('consolas', 20), bg='#85a885'))
# buttons[12].grid(row=2, column=3)
# buttons.append(Button(calculator, text="-", font=('consolas', 20), bg='#85a885'))
# buttons[13].grid(row=3, column=3)
# buttons.append(Button(calculator, text="×", font=('consolas', 20), bg='#85a885'))
# buttons[14].grid(row=3, column=2)
# buttons.append(Button(calculator, text="÷", font=('consolas', 20), bg='#85a885'))
# buttons[15].grid(row=3, column=0)



mathemetical_list = list(input().split())
operators = list()
numbers = list()
alt = list()
cntr = 0
alt_revers = 1

def calculate(mathemetical_list):
    math_string = ''.join(mathemetical_list)
    if (re.search(r'[^0-9.]', math_string)) != None:
        span = re.search(r'[^0-9.]', math_string).span()
        match = math_string[span[0]:span[1]]
        print(match)
        operators.append(match)
        print(span)
        print(f'string:{math_string}')
        print(list(math_string.split(match)))
        alt = list(math_string.split(match))
        
        for i in range(len(alt)):
            if  alt[i].isnumeric() or ("." in alt[i]):
                numbers.append(alt[i])
                
        if match == '+':
            print('plus')
        elif match == '-':
            print('minus')
            pass
        elif match == '×':
            print('multiple')
            pass
        elif match == '÷':
            print('divisoin')
            pass
        elif match == '.':
            print('dot')
            pass
        print(f'alt: {alt}')
        print(f'operators {operators}')
        print(f'numbers {numbers}')
        alt.pop(0)
        calculate(alt)
    return numbers, operators

# print(calculate(mathemetical_list))


def calculate_math(numbers, operators):
    for i in numbers:
        print(i)
    for j in operators:
        print(j)

res = calculate(mathemetical_list)
calculate_math(res[0], res[1])