from tkinter import *
from tkinter import messagebox

import tkinter as tk
from tkinter import ttk

from convert import *
from edu import *

class tkinterApp(tk.Tk):
    def go_main(self):
        self.geometry('1100x500')
        self.show_frame(StartPage)
    def go_edu(self, num=0):
        if num == 0:
            self.geometry('1100x500')
            self.show_frame(Page_edu)
        elif num == 1:
            self.geometry('1200x800')
            self.show_frame(Page_edu_2)
        elif num == 2:
            self.geometry('1200x800')
            self.show_frame(Page_edu_8)
        elif num == 3:
            self.geometry('1200x800')
            self.show_frame(Page_edu_10)
        elif num == 4:
            self.geometry('1200x800')
            self.show_frame(Page_edu_16)

    def go_convert(self):
        self.geometry('1100x500')
        self.show_frame(Page_convert)



    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('1100x500')
        self.resizable(False, False)
        main_menu = Menu(self)
        self.config(menu=main_menu)
        self.title("Системы счисления")

        main_menu.add_command(label='Главное меню', command=lambda : self.go_main())
        main_menu.add_command(label='Обучение', command=lambda : self.go_edu())
        main_menu.add_command(label='Перевод', command=lambda : self.go_convert())


        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, Page_convert, Page_edu, Page_edu_2, Page_edu_8, Page_edu_10, Page_edu_16):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #ttk.geometry('1100x500')
        #ttk.title("Главное меню")
        lbl = Label(self, text="Это программа по обученю по переводу чисел в разные системы счисления", font=("Arial Bold", 14))
        lbl.grid(column=0, row=0)
        lbl = Label(self, text="и проверки перевода в них", font=("Arial Bold", 14))
        lbl.grid(column=0, row=1)
        btn = Button(self, text="Обучение", command = lambda : controller.show_frame(Page_edu) ,font=("Arial Bold", 14), height = 5, width = 20)
        btn.place(x=125, y=85)
        btn = Button(self, text="Перевод", command = lambda : controller.show_frame(Page_convert), font=("Arial Bold", 14), height = 5, width = 20)
        btn.place(x=400, y=85)
app = tkinterApp()
app.mainloop()
