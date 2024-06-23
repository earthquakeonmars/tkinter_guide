from tkinter import Tk, Label, Frame, CENTER
from random import random

def change(event):
    label1['text'] = 'До свидания' if label1['text'] == 'Добрый день' else 'Добрый день'

def highlight(event):
    label1['background'] = 'LightBlue'

def restore_bg(event):
    label1['background'] = 'White'

def run_away(event):
    new_x = random()
    new_y = random()
    label2.place(relx=new_x, rely=new_y)

root = Tk()
root.geometry('650x450+150+150')
root.config(bg='gray70')
frame1 = Frame(root, borderwidth=2)
frame1.place(rely=0.5, relx=0.5, anchor=CENTER)
label1 = Label(frame1, text='Добрый день', font='Arial 12' , width=26, height=2, borderwidth=2)
label1.grid()
label2 = Label(root, text='Несметные богатства', font='Calibri 12' , width=26, height=2)
label2.place(relx=0.1, rely=0.1)
label2.bind('<Motion>', run_away)

label1.bind('<Button-1>', change)
label1.bind('<Enter>', highlight)
label1.bind('<Leave>', restore_bg)
root.mainloop()

