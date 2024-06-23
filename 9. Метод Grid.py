from tkinter import Tk, Frame, Button, CENTER, W

root = Tk()
root.geometry('1050x750+50+50')
root.config(bg='gray70')
root.resizable(False, False)
f = Frame(root)
f.place(x=250, y=250)
Button(f, text='Новая кнопка 1', pady=20, padx=20).grid(row=0, column=0, padx=15, pady=10)
Button(f, text='Новая кнопка 2', pady=20, padx=20).grid(row=0, column=1, padx=15, pady=10)
Button(f, text='Новая кнопка 3', pady=20, padx=20).grid(row=1, column=0, padx=15, pady=10)
Button(f, text='Новая кнопка 4', pady=20, padx=20).grid(row=1, column=1, padx=15, pady=10)
Button(f, text='Новая кнопка 5', pady=20, padx=20, width=30).grid(row=2, column=1, columnspan=2, rowspan=2, sticky=W)

for i in range(5):
    Button(root, text=f'Button {i}').place(x=50*i, y=15)

root.mainloop()