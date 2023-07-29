from tkinter import*

def press_button(num):
    global show_string
    show_string =show_string+str(num)
    show_label.set(show_string)


def equals():
    try:
        global show_string
        total = str(eval(show_string))
        show_label.set(total)
        show_string =''

    except ZeroDivisionError:
        show_label.set('zero error')

    except SyntaxError:
        show_label.set('syntax error')


def clear():
    global show_string

    show_label.set('')

    show_string= ''


window =Tk()

window.geometry('500x500')
window.title('simple cal')

show_string=''

show_label= StringVar()

label =Label(window,textvariable=show_label ,bg='white',width=24,height=2,font=('consolas',20))
label.pack()

frame =Frame(window)
frame.pack()

button1 =Button(frame,text=1,height=4,width=9,font=35,command=lambda:press_button(1))
button1.grid(row=0,column=0)

button2 =Button(frame,text=2,height=4,width=9,font=35,command=lambda:press_button(2))
button2.grid(row=0,column=1)

button3 =Button(frame,text=3,height=4,width=9,font=35,command=lambda:press_button(3))
button3.grid(row=0,column=2)

button4 =Button(frame,text=4,height=4,width=9,font=35,command=lambda:press_button(4))
button4.grid(row=1,column=0)

button5 =Button(frame,text=5,height=4,width=9,font=35,command=lambda:press_button(5))
button5.grid(row=1,column=1)

button6 =Button(frame,text=6,height=4,width=9,font=35,command=lambda:press_button(6))
button6.grid(row=1,column=2)

button7 =Button(frame,text=7,height=4,width=9,font=35,command=lambda:press_button(7))
button7.grid(row=2,column=0)

button8 =Button(frame,text=8,height=4,width=9,font=35,command=lambda:press_button(8))
button8.grid(row=2,column=1)

button9 =Button(frame,text=9,height=4,width=9,font=35,command=lambda:press_button(9))
button9.grid(row=2,column=2)

button0 =Button(frame,text=0,height=4,width=9,font=35,command=lambda:press_button(0))
button0.grid(row=3,column=1)

equals_button= Button(frame,text='=',height=4,width=9,font=35,command=equals)
equals_button.grid(row=3,column=2)

add_button=Button(frame,text="+",height=4,width=9,font=35,command=lambda:press_button('+'))
add_button.grid(row=0,column=4)

mines_button=Button(frame,text="-",height=4,width=9,font=35,command=lambda:press_button('-'))
mines_button.grid(row=1,column=4)

multy_button=Button(frame,text="*",height=4,width=9,font=35,command=lambda:press_button('*'))
multy_button.grid(row=2,column=4)

divide_button=Button(frame,text="/",height=4,width=9,font=35,command=lambda:press_button('/'))
divide_button.grid(row=3,column=4)

ponkt =Button(frame,text='.',font=35,width=9,height=4,command=lambda:press_button('.'))
ponkt.grid(row=3,column=0)

clear_button=Button(window,text="clear",height=4,width=12,font=35,command=clear)
clear_button.pack()
window.mainloop()