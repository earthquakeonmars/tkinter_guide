from tkinter import Tk, Frame, BOTTOM, Label, LEFT, CENTER, LabelFrame, W, SW

root = Tk()
root.geometry('1050x750+50+50')
root.config(bg='gray70')
root.resizable(False, False)

frame_bottom = Frame(root)
frame_bottom.pack(anchor=CENTER, side=LEFT)

Label(frame_bottom, text='Новый лейбл', font='Arial 13', activebackground='gray55').pack(side=LEFT, padx=5, pady=5)
Label(frame_bottom, text='Еще один лейбл', font='Arial 13', activebackground='gray55').pack(side=LEFT, padx=5, pady=50)

new1 = LabelFrame(root, labelanchor=SW)
new1.place(x=350, y=350)

Label(new1, text='Лейбл 1', font='Arial 10', activebackground='green').pack()

root.mainloop()