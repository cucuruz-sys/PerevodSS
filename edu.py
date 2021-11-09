from tkinter import *
from tkinter import messagebox

import tkinter as tk
from tkinter import ttk

class Page_edu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #window = Tk()
        #window.geometry('1100x500')

        #window.title("Обучение переводу")
        lbl = Label(self, text="Выберите в какую систему счисления вы хотите научиться перводить", font=("Arial Bold", 14))
        lbl.grid(column=0, row=0)

        btn2 = Button(self, text="В двоичную", command=lambda : controller.go_edu(1), font=("Arial Bold", 14), height = 5, width = 20)
        btn2.grid(column=0, row=1)

        btn8 = Button(self, text="В восьмеричную", command=lambda : controller.go_edu(2), font=("Arial Bold", 14), height = 5, width = 20)
        btn8.grid(column=0, row=2)

        btn10 = Button(self, text="В десятичную", command=lambda : controller.go_edu(3), font=("Arial Bold", 14), height = 5, width = 20)
        btn10.grid(column=1, row=1)

        btn16 = Button(self, text="В шестнадцатиричную", command=lambda : controller.go_edu(4), font=("Arial Bold", 14), height=5, width=20)
        btn16.grid(column=1, row=2)

        backbtn = Button(self, text="В главное меню", command = lambda : controller.go_main(), height=4, width=20)
        backbtn.place(x=5, y=425)

class Page_edu_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = Frame(self)
        frame.place(x=25, y=5)

        canvas = Canvas(self, height=700, width=1150)
        canvas.pack()

        self.img = PhotoImage(file='edu/2_1.png')
        image = canvas.create_image(0, 0, anchor='nw', image=self.img)

        canvas.place(x=25, y=5)

        backbtn = Button(self, text="Назад", command=lambda : controller.go_edu(), height=4, width=20)
        backbtn.place(x=5, y=725)

class Page_edu_8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = Frame(self)
        frame.place(x=25, y=5)
        canvas = Canvas(self, height=700, width=1150)
        self.img = PhotoImage(file='edu/8_1.png')
        image = canvas.create_image(0, 0, anchor='nw', image=self.img)
        canvas.place(x=25, y=5)
        backbtn = Button(self, text="Назад", command=lambda : controller.go_edu(), height=4, width=20)
        backbtn.place(x=5, y=725)

class Page_edu_10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = Frame(self)
        frame.place(x=25, y=5)
        canvas = Canvas(self, height=700, width=1150)
        self.img = PhotoImage(file='edu/10_1.png')
        image = canvas.create_image(0, 0, anchor='nw', image=self.img)
        canvas.place(x=25, y=5)
        backbtn = Button(self, text="Назад", command=lambda : controller.go_edu(), height=4, width=20)
        backbtn.place(x=5, y=725)

class Page_edu_16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = Frame(self)
        frame.place(x=25, y=5)
        canvas = Canvas(self, height=700, width=1150)
        self.img = PhotoImage(file='edu/16_1.png')
        image = canvas.create_image(0, 0, anchor='nw', image=self.img)
        canvas.place(x=25, y=5)
        backbtn = Button(self, text="Назад", command=lambda : controller.go_edu(), height=4, width=20)
        backbtn.place(x=5, y=725)
