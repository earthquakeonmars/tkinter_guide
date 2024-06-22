from tkinter import Tk, Button, DISABLED, ACTIVE, S, W, E, N, NW, NE, Label, Entry, END

root = Tk()
root.title('Моё приложение')
root.geometry('750x650+250+150')
root.iconbitmap('cat_PNG50525.ico')
root['bg'] = 'DarkGray'

#-----------------------------------------------------------------------------------------------------------------------
# root - на каком окне размещать виджет entry
# font - текс (шрифт, размер, параметр)
#-----------------------------------------------------------------------------------------------------------------------
# Метод insert
# Если надо добавить текст в Entry используется метод insert
# Можно указать индекс после которого следует вставить текст, а потом сам текст
# Либо можно указать константу, например если указать END - текст вставится в самый конец
#-----------------------------------------------------------------------------------------------------------------------
# Метод delete
# Удаляет из строки текст в диапазоне указанных индексов
#-----------------------------------------------------------------------------------------------------------------------


def add_str():
    textbox.insert(END, ' новая запись')

def clear_str():
    textbox.delete(0, END)

def get_str():
    content = textbox.get()
    label1['text'] = content

textbox = Entry(root,font='Arial 15 bold')
textbox.pack()

button_add = Button(root, text='Добавить текст', command=add_str)
button_add.pack(anchor=W)

button_delete = Button(root, text='Убрать текст', command=clear_str)
button_delete.pack(anchor=W)

button_print = Button(root, text='Показать текст', command=get_str)
button_print.pack(anchor=W)

label1 = Label(root, font='Arial 14 bold')
label1.pack(anchor=E)

root.mainloop()