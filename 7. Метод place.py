from tkinter import Tk, Button, CENTER, W

root = Tk()
root.geometry('1050x750+50+50')
root.config(bg='gray70')
#-----------------------------------------------------------------------------------------------------------------------
# x - координата виджета по x
# y - координата виджета по y
# height - высота лейбла
# width - ширина лейбла
# anchor - место размещения виджета
#-----------------------------------------------------------------------------------------------------------------------
Button(root, text='Файл', font='Arial 13', activebackground='gray55').place(x=5, y=5)
Button(root, text='Правка', font='Arial 13', activebackground='gray55').place(x=65, y=5)
Button(root, text='Вид', font='Arial 13', activebackground='gray55').place(x=138, y=5)
Button(root, text='Помощь', font='Arial 13', activebackground='gray55').place(x=188, y=5, height=25)

root.mainloop()