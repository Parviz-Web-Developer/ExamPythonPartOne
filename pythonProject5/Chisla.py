import random
from tkinter import *
from tkinter import messagebox as ms

app = Tk()

num = random.randint(1, 1000)
print(num)

popitka = 12
def ask():
    global popitka
    global num
    popitka -= 1
    try:
        num_player = int(ent.get())
    except ValueError:
        ms.showinfo('Ошибка', 'Вы ввели не число, пожалуйста введите число')
        popitka += 1
    if popitka > -1:
        try:
            if num > num_player:
                lbl.configure(text=f'Моё число больше чем то, что вы вписали.\nУ тебя осталось {popitka} попыток.')
            elif num < num_player:
                lbl.configure(text=f'Моё число меньше чем то, что вы вписали.\nУ тебя осталось {popitka} попыток.')
            else:
                lbl.configure(text='Ты отгадал. Можешь бахнуть балтику.')
                ent.pack_forget()
                btn.pack_forget()
        except UnboundLocalError:
            print('')

    else:
        lbl.configure(text='У тебя осталось 0 попыток. Ты проиграл.\n Сильно не гоняй, ты еще маме нужен.')
        ent.pack_forget()
        btn.pack_forget()




lbl = Label(app, text='Я загадал число от 1 до 1000. Попробуй отгадай. \n У тебя есть 12 попыток', font='Monsterrat 40')
btn = Button(app, text='Ответить', font='Monsterrat 30', command=ask)
lbl_skip = Label(app, text='')
ent = Entry(app, font='Monsterrat 40')


lbl.pack()
ent.pack()
lbl_skip.pack()
btn.pack()
app.geometry('1500x700')
app.mainloop()
