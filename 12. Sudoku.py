from tkinter import Tk, Frame, Label, W, NW, Event, Button, messagebox, ttk, VERTICAL, HORIZONTAL, Y


root = Tk()

#-----------------------------------------------------------------------------------------------------------------------
# Конфигурация основного окна
#-----------------------------------------------------------------------------------------------------------------------
root.title('Sudoku')
root.config(bg='Silver')
root.geometry('1050x650+150+150')
root.resizable(width=False, height=False)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Конфигурация фрейма, на котором располагается сетка
#-----------------------------------------------------------------------------------------------------------------------
frame_sudoku_grid = Frame(root)
frame_sudoku_grid.place(x=20, rely=0.525, anchor=W)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Конфигурация фрейма, на котором располагаются кнопки «Правила», «Управление», «О программе»
#-----------------------------------------------------------------------------------------------------------------------
frame_ribbon = Frame(root)
frame_ribbon.place(x=20, rely=0.0125, anchor=NW)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Информационные окна, появляющиеся при нажатии на кнопки, расположенные на ленте
#-----------------------------------------------------------------------------------------------------------------------
def messagebox_rules() -> None:
    messagebox.showinfo(title='Правила', message='Правила судоку можно посмотреть в интернете.')

def messagebox_controls() -> None:
    messagebox.showinfo(title='Управление', message='ЛКМ-увеличить число, ПКМ-уменьшить число, колесо-отметить клетку.')

def messagebox_about() -> None:
    messagebox.showinfo(title='О программе', message='Судоку')
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Конфигурация кнопок ленточного интерфейса приложения
#-----------------------------------------------------------------------------------------------------------------------
button_rules = Button(frame_ribbon, text='Правила игры',
                      bg='gray95', fg='black', font='Arial 13', bd=2, relief='raised',
                      cursor='hand2', activebackground='gray80', command=messagebox_rules)
button_rules.grid(row=0, column=0)

button_controls = Button(frame_ribbon, text='Управление',
                         bg='gray95', fg='black', font='Arial 13', bd=2, relief='raised',
                         cursor='hand2', activebackground='gray80', command=messagebox_controls)
button_controls.grid(row=0, column=1)

button_about = Button(frame_ribbon, text='О программе',
                      bg='gray95', fg='black', font='Arial 13', bd=2, relief='raised',
                      cursor='hand2', activebackground='gray80', command=messagebox_about)
button_about.grid(row=0, column=2)

button_language = Button(frame_ribbon, text='Рус',
                      bg='gray95', fg='black', font='Arial 13', bd=2, relief='raised',
                      cursor='hand2', activebackground='gray80')
button_language.grid(row=0, column=3)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Функции для того, что менять клетку
#-----------------------------------------------------------------------------------------------------------------------
def highlight(event: Event) -> None:
    """Подсвечивает фон клетки при наведении на нее курсора мыши"""
    event.widget['background'] = 'sky blue'

def downplay(event: Event) -> None:
    """Возвращает цвет фона клетки в исходный"""
    event.widget['background'] = 'white'

def increase(event: Event) -> None:
    """Увеличивает число в клетке на единицу"""
    curr = event.widget['text']
    if not curr:
        event.widget['text'] = '1'
    else:
        curr = int(curr)
        curr = curr + 1
        if curr > 9:
            event.widget['text'] = ''
        else:
            event.widget['text'] = str(curr)

def decrease(event: Event) -> None:
    """Уменьшает число в клетке на единицу"""
    curr = event.widget['text']
    if not curr:
        event.widget['text'] = '9'
    else:
        curr = int(curr)
        curr = curr - 1
        if curr > 0:
            event.widget['text'] = str(curr)
        else:
            event.widget['text'] = ''

def mark(event: Event) -> None:
    """Отмечает клетку другим цветом"""
    if event.widget['text']:
        curr_fg = event.widget['fg']
        if curr_fg == 'black':
            event.widget['fg'] = 'red'
        else:
            event.widget['fg'] = 'black'
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# Конфигурация сетки судоку
#-----------------------------------------------------------------------------------------------------------------------
for row in range(9):
    for col in range(9):
        cell = Label(frame_sudoku_grid,
                     text='', width=6, height=3,
                     bg='white', fg='black', font='Arial 13 bold',
                     bd=2, relief='groove')
        cell.grid(row=row, column=col)
        print(cell.winfo_width())
        print(cell.winfo_height())
        cell.bind('<Enter>', highlight)
        cell.bind('<Leave>', downplay)
        cell.bind('<Button-1>', increase)
        cell.bind('<Button-2>', mark)
        cell.bind('<Button-3>', decrease)
#-----------------------------------------------------------------------------------------------------------------------

root.mainloop()
