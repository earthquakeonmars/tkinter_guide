from tkinter import Tk, Button, DISABLED, ACTIVE, S, W, E, N, NW, NE, Label

root = Tk()
root.title('Моё приложение')
root.geometry('750x650+250+150')
root.iconbitmap('cat_PNG50525.ico')
root['bg'] = 'DarkGray'

#-----------------------------------------------------------------------------------------------------------------------
# root - окно на котором надо разместить кнопку
# text - текст на кнопке
# bg - бэкграунд (фон кнопки)
# fg - цвет текста на кнопке
# font - параметры шрифта текста
# activeforeground - цвет текста когда кнопка нажата
# activebackground - цвет фона кнопки когда кнопка нажата
# cursor - вид курсора
# borderwidth - ширина границы вокруг кнопки
# command - команда
#-----------------------------------------------------------------------------------------------------------------------

def create_lable():
    Label(root,
          text='Текст внутри окна',
          width=25,
          height=2,
          bg='DarkOliveGreen3',
          fg='Black',
          font='Arial 15'
          ).pack()

button1 = Button(root,
                 text='Start',
                 bg='LightGray',
                 fg='MidnightBlue',
                 font='Calibri 18',
                 activeforeground='DodgerBlue',
                 activebackground='Aquamarine',
                 cursor='hand2',
                 borderwidth=3,
                 command=create_lable)

button2 = Button(root,
                 text='Другая кнопка которая не активна',
                 state=DISABLED)

button1.pack(anchor=NE)
button2.pack(anchor=NW)

root.mainloop()