from tkinter import Tk, PhotoImage

root = Tk()

# Название приложения, отображаемое в окошке
root.title('Моё приложение')

# Разрешение окна приложения, числа с плюсом нужны для того чтобы обозначить место, где появляется окно
root.geometry('750x650+250+150')

# Для того чтобы узнать ширину и высоту экрана существуют методы winfo_screenwidth и winfo_screenheight
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Изменение логотипа приложения, используя файл с расширением ico
root.iconbitmap('cat_PNG50525.ico') # Будет работать тольок с расширенями ico

# Изменение логотипа приложения, используя файл с расширением
root.tk.call('wm', 'iconphoto', root, PhotoImage(file='RF.png'))

# Изменение логотипа с помощью iconphoto
# если первый элемент False, то изображение будет только на одном окне, а на всех последующих будет стандартное изображение
root.iconphoto(True, PhotoImage(file='RF.png'))

# Запрет изменения размеров окна
root.resizable(width=False, height=False)

# Изменение фона окна
root.config(bg='Silver') # С использованием метода config
root['bg'] = 'Ivory' # Присваивание по ключу

# Запуск приложения во весь экран (как игра)
root.attributes('-fullscreen', False) # если указать второй параметр True, то

root.mainloop()