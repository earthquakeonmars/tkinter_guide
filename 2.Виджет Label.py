from tkinter import Tk, Label, W, E, S, N, PhotoImage, LEFT, RIGHT, CENTER, SUNKEN, RAISED

root = Tk()
root.title('Моё приложение')
root.geometry('750x650+250+150')
root.iconbitmap('cat_PNG50525.ico')
root['bg'] = 'SeaShell2'
#-----------------------------------------------------------------------------------------------------------------------
# Аргументы инициализации объекта класса Label
# root - название окна на котором надо распологать лейбл
# text - текст внутри лейбла
# width - ширина лейбла
# height - высота лейбла
# bg - цвет фона лейбла
# fg - Цвет текста
# bd - толщина границы лейбла
# font - шрифт, размер, параметры шрифта (курсив, жирный и т. д.). Если название шрифта состоит из нескольких слов, то
# надо их писать в скобках (см. второй лейбл)
# padx - отсуп от границы лейбла до верхнего левого угла текста
# pady - отсуп от границы лейбла до верхнего левого угла текста
# cursor - как должен менятся курсор при наведении на лейбл
# justify - выравнивание текста
# relief - форма границы
# wraplength - макс. количество символов в одной строке
#-----------------------------------------------------------------------------------------------------------------------
# Аргументы метода pack
# anchor - где анкерить лейбл относительно окна в котором лейбл располагается (W - запад, E - восток и т. д.)
#-----------------------------------------------------------------------------------------------------------------------

Label(root,
      text='Текст внутри окна',
      width=25,
      height=2,
      bg='DarkOliveGreen3',
      fg='Gray',
      bd=1,
      font='Arial 15 bold',
      padx=5,
      pady=3,
      cursor='hand2',
      justify=LEFT,
      relief=RAISED,
      wraplength=140).pack(anchor=W)

Label(root,
      text='Другой текст внутри окна который чутка подлинне чем в первом лейбле',
      width=35,
      height=2,
      bg='LightGreen',
      fg='Red',
      bd=5,
      font=('Comic Sans MS', 12, 'italic'),
      cursor='hand2',
      justify=RIGHT,
      relief=SUNKEN).pack(anchor=E)

Label(root,
      image=PhotoImage(file='my_cat.png'),
      cursor='heart').pack(anchor=S)

root.mainloop()