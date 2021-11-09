from tkinter import *
from tkinter import messagebox

import tkinter as tk
from tkinter import ttk

class Page_convert(tk.Frame):

    def convert_base(self, num, to_base, from_base):

        if (from_base < 2) or (to_base < 2):
            messagebox.showerror(title='Ошибка преобразования', message='Основание системы счисления не может быть меньше 2х')
        elif (from_base == to_base):
            messagebox.showerror(title='Ошибка преобразования', message='Вы ввели одинаковые основания для системы счисления')
        elif (len(str(num)) < 1):
            messagebox.showerror(title='Ошибка преобразования', message='Пустое поле для числа')
        else:

            n = int(num, from_base) if isinstance(num, str) else num
            alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = ""
            while n > 0:
                n, m = divmod(n, to_base)
                res += alphabet[m]
            resu = "Результат перевода: " + str(num) + " в " + str(from_base) + "-ной системе счисления" + " = " + res[::-1] + " в " + str(to_base) + "-ной системе счисления"

            #return res[::-1]
            return resu

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        def convert():
            if (len(inpnum.get()) < 1) and (len(inpnum.get()) < 1) and (len(inpnum.get()) < 1):
                messagebox.showerror(title='Ошибка преобразования', message='Все поля ввода надо заполнить')
            elif not (inpnum.get().isdigit() and baseto.get().isdigit() and basefrom.get().isdigit()):
                messagebox.showerror(title='Ошибка преобразования', message='Вы ввели не целое число')

            else:
                out_text.configure(text=self.convert_base(inpnum.get(), int(baseto.get()), int(basefrom.get())))


        #window = Tk()
        #window.geometry('1100x500')

        #window.title("Перевод из одной сиситемы счисления в другую")

        lbl = Label(self, text="Перевести из системы счисления с основанием:", font=("Arial Bold", 14))
        lbl.grid(column=0, row=0)

        basefrom = Entry(self,width=10)
        basefrom.grid(column=1, row=0)
        basefrom.insert(0,"10")

        lbl = Label(self, text="в сиситему счисления с основанием:", font=("Arial Bold", 14))
        lbl.grid(column=2, row=0)

        baseto = Entry(self,width=10, text="2")
        baseto.grid(column=3, row=0)
        baseto.insert(0,"2")

        lbl = Label(self, text="Число:", font=("Arial Bold", 14))
        lbl.grid(column=0, row=1)

        inpnum = Entry(self,width=30)
        inpnum.grid(column=1, row=1)

        btn = Button(self, text="Перевести", command=convert)
        btn.grid(column=1, row=2)

        out_text = Label(self, text="Результат перевода: ", font=("Arial Bold", 15))
        out_text.place(x=75, y=85)

        backbtn = Button(self, text="В главное меню", command = lambda : controller.go_main(), height=4, width=20) #back
        backbtn.place(x=5, y=425)
