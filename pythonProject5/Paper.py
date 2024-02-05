import random
from tkinter import *
from PIL import ImageTk, Image
import sys

app = Tk()

image_stone = ImageTk.PhotoImage(file='icons/stone.png')
image_nojnici = ImageTk.PhotoImage(file='icons/nojnici.png')
image_paper = ImageTk.PhotoImage(file='icons/paper.png')

random_num = random.randint(1, 3)

def start_game():
    lbl.configure(text='Выбирай: ')
    btn_stone.grid(column=2, row=0)
    btn_nojnic.grid(column=3, row=0)
    btn_paper.grid(column=4, row=0)
    btn_yes.grid_forget()
    btn_no.grid_forget()

def end_game():
    sys.exit()

def stone():
    global random_num
    if random_num == 1:
        lbl.configure(text='Я выбрал камень. Ничья.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()

    elif random_num == 2:
        lbl.configure(text='Я выбрал ножницы. Я проиграл.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()

    else:
        lbl.configure(text='Я выбрал бумагу. Я выиграл.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()


def nojnici():
    global random_num
    if random_num == 1:
        lbl.configure(text='Я выбрал камень. Я выиграл.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()

    elif random_num == 2:
        lbl.configure(text='Я выбрал ножницы. Ничья.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()

    else:
        lbl.configure(text='Я выбрал бумагу. Я проиграл.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()


def paper():
    global random_num
    if random_num == 1:
        lbl.configure(text='Я выбрал камень. Я проиграл.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()

    elif random_num == 2:
        lbl.configure(text='Я выбрал ножницы. Я выиграл.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()

    else:
        lbl.configure(text='Я выбрал бумагу. Ничья.')
        btn_stone.grid_forget()
        btn_nojnic.grid_forget()
        btn_paper.grid_forget()


lbl = Label(app, text='Привет! Давай сыграем в Камень, Ножницы, Бумагу?', font='Monsterrat 40')
lbl_skip = Label(app, text='', font='Monsterrat 50')
lbl_skip2 = Label(app, text='', font='Monsterrat 50')

btn_yes = Button(app, text='Давай!', font='Monsterrat 25', command=start_game)
btn_no = Button(app, text='Нет, не хочу', font='Monsterrat 25', command=end_game)
btn_stone = Button(app, image=image_stone, font='Monsterrat 50', command=stone)
btn_nojnic = Button(app, image=image_nojnici, font='Monsterrat 50', command=nojnici)
btn_paper = Button(app, image=image_paper, font='Monsterrat 50', command=paper)

lbl.grid(column=0, row=0)
lbl_skip.grid(column=0, row=1)
btn_yes.grid(column=0, row=2)
btn_no.grid(column=0, row=3)
app.geometry('1350x500')
app.mainloop()
