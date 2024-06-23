from tkinter import Tk, Button, Frame, CENTER, Label
from random import choice

def disable_buttons():
    rock['state'] = 'disabled'
    paper['state'] = 'disabled'
    scissors['state'] = 'disabled'

def enable_buttons():
    rock['state'] = 'normal'
    paper['state'] = 'normal'
    scissors['state'] = 'normal'

def play_stone():
    computer_choice = choice(['Камень', 'Ножницы', 'Бумага'])
    if computer_choice == 'Камень':
        display['text'] = 'Камень' + '\nНичья.'
    elif computer_choice == 'Ножницы':
        display['text'] = 'Ножницы' + '\nВы выиграли.'
        score_value_human['text'] = str(int(score_value_human['text']) + 1)
    else:
        display['text'] = 'Бумага' + '\nВы проиграли.'
        score_value_comp['text'] = str(int(score_value_comp['text']) + 1)
    restart_button['state'] = 'normal'
    disable_buttons()

def play_scissors():
    computer_choice = choice(['Камень', 'Ножницы', 'Бумага'])
    if computer_choice == 'Камень':
        display['text'] = 'Камень' + '\nВы проиграли.'
        score_value_comp['text'] = str(int(score_value_comp['text']) + 1)
    elif computer_choice == 'Ножницы':
        display['text'] = 'Ножницы' + '\nНичья.'
    else:
        display['text'] = 'Бумага' + '\nВы выиграли.'
        score_value_human['text'] = str(int(score_value_human['text']) + 1)
    restart_button['state'] = 'normal'
    disable_buttons()

def play_paper():
    computer_choice = choice(['Камень', 'Ножницы', 'Бумага'])
    if computer_choice == 'Камень':
        display['text'] = 'Камень' + '\nВы выиграли.'
        score_value_human['text'] = str(int(score_value_human['text']) + 1)
    elif computer_choice == 'Ножницы':
        display['text'] = 'Ножницы' + '\nВы проиграли.'
        score_value_comp['text'] = str(int(score_value_comp['text']) + 1)
    else:
        display['text'] = 'Бумага' + '\nНичья.'
    restart_button['state'] = 'normal'
    disable_buttons()

def start_again():
    display['text'] = 'Сделайте свой выбор'
    restart_button['state'] = 'disabled'
    enable_buttons()

root = Tk()
root.title('Rock paper scissors')
root.geometry('650x350+150+150')
root.resizable(width=False, height=False)
root.config(bg='gray70')

bottom_frame = Frame(root)
bottom_frame.place(rely=0.7, relx=0.5, anchor=CENTER)

restart = Frame(root)
restart.place(rely=0.85, relx=0.5, anchor=CENTER)

score_table = Frame(root)
score_table.place(rely=0.1, relx=0.15, anchor=CENTER)

restart_button = Button(restart,
                  text='Играть еще',
                  font='Arial 16',
                  cursor='hand2',
                  activebackground='gray45',
                  borderwidth=3,
                  activeforeground='white',
                  state='disabled',
                  command=start_again)

restart_button.grid(row=0, column=0)

display = Label(root, text='Сделайте свой выбор', font='Arial 16', height='3', width='25')
display.place(rely=0.4, relx=0.5, anchor=CENTER)

score_title_human = Label(score_table, text='Человек', font='Arial 12', borderwidth=2, relief='solid')
score_title_comp = Label(score_table, text='Компьютер', font='Arial 12', borderwidth=2, relief='solid')
score_value_human = Label(score_table, text='0', font='Arial 12', borderwidth=2, relief='solid')
score_value_comp = Label(score_table, text='0', font='Arial 12', borderwidth=2, relief='solid')

score_title_human.grid(row=0, column=0)
score_title_comp.grid(row=0, column=1)
score_value_human.grid(row=1, column=0)
score_value_comp.grid(row=1, column=1)

rock = Button(bottom_frame,
              text='Камень',
              font='Arial 16',
              cursor='hand2',
              activebackground='gray45',
              borderwidth=3,
              activeforeground='white',
              command=play_stone)

paper = Button(bottom_frame,
               text='Ножницы',
               font='Arial 16',
               cursor='hand2',
               activebackground='gray45',
               borderwidth=3,
               activeforeground='white',
               command=play_scissors)

scissors = Button(bottom_frame,
                  text='Бумага',
                  font='Arial 16',
                  cursor='hand2',
                  activebackground='gray45',
                  borderwidth=3,
                  activeforeground='white',
                  command=play_paper)

rock.grid(row=0, column=0)
paper.grid(row=0, column=1)
scissors.grid(row=0, column=2)

root.mainloop()