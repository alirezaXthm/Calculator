from tkinter import * 

class CalcButton():
    def __init__(self, master,text,command, bg, fg, font):
        self.text = text
        self.master = master
        self.command = command
        self.bg = bg
        self.fg = fg
        self.font = font
        
        self.button = Button(master=self.master, text=self.text, command=command, bg=self.bg, fg = self.fg , font = font)
        
    # def butt_pack(self):
    #     self.button.grid()
        
    def cget(self, text):
        self.button.cget(text)
    
# griding buttons with while loops

        # j = 1
        # i = 1
        # j_flag = False

        # while j < 3:
        #     column  = 0
        #     while i < len(buttons)+1:
        #         if i % 4 == 0:
        #             j_flag = False
        #             j += 1
        #         if column == 3:
        #             column = 0
        #         else:
        #             column += 1
        #         print(f'i:{i}, j:{j} c:{column}')
        #         buttons[i-1].grid(row=j, column=column)
        #         i += 1
        #     i += 1
        #     if j_flag:
        #         j += 1
        

#griding one by one


