from tkinter import Tk, PhotoImage, Label, BOTTOM, LEFT, RIGHT, X, Y

root = Tk()
root.title('Окно1')
root.geometry('750x750+150+150')
root.tk.call('wm', 'iconphoto', root, PhotoImage(file='apple.png'))
root['bg'] = 'DarkGray'

#-----------------------------------------------------------------------------------------------------------------------
# side - сторона расположения виджета (значение по умолчанию TOP, еще есть LEFT, RIGHT, BOTTOM)
# expand - если expand == True, то виджет заполняет все пространство контейнера (виджет будет посередине окна)
# fill - заполнить по X, заполнить по Y. Если надо заполнить по обоим осям, то надо прописывать значение BOTH
# anchor - позиционирование элементов по частям света
# padx - отступ по x
# pady - отступ по y
#-----------------------------------------------------------------------------------------------------------------------

label1 = Label(root, text='Новый текст', background='Red', height='2', fg='Black').pack(side=BOTTOM, expand=False, fill=X)
label1 = Label(root, text='Другой текст', background='green', height='2', fg='Yellow').pack(expand=False, fill=X, side=RIGHT)

root.mainloop()