from tkinter import Tk, PhotoImage, Entry, Button

root = Tk()
root.title('Change')
root.geometry('750x750+150+150')
root.tk.call('wm', 'iconphoto', root, PhotoImage(file='apple.png'))
root['bg'] = 'DarkGray'

def change():
    root['bg'] = textbox.get()

textbox = Entry(root, font='Arial 15')
textbox.pack()

button1 = Button(root, text='Сменить цвет', font='Arial 12', command=change)
button1.pack()

root.mainloop()