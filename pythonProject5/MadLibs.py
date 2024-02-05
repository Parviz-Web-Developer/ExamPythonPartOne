import sys
from tkinter import *

app = Tk()

def start_game():
        ent.pack()
        btn_okay.pack()
        btn_close.pack_forget()
        btn_start.pack_forget()
        btn_okay.pack()
        lbl.configure(text='Хорошо, начнем. Для начала назови мне какое нибудь имя.')

def func_name():
        global user
        btn_okay.pack_forget()
        user = ent.get()
        print(user)
        btn_okay2.pack()
        ent.delete(0, END)
        lbl.configure(text='Теперь любой предмет.')

def func_item():
        global item
        btn_okay2.pack_forget()
        item = ent.get()
        print(item)
        ent.delete(0, END)
        btn_okay3.pack()
        lbl.configure(text='Любой город.')

def func_city():
        global city
        btn_okay3.pack_forget()
        city = ent.get()
        print(city)
        btn_okay4.pack()
        ent.delete(0, END)
        lbl.configure(text='Еще одно любое имя.')

def func_sec_name():
        global name2
        btn_okay4.pack_forget()
        name2 = ent.get()
        print(name2)
        btn_okay5.pack()
        ent.delete(0, END)
        lbl.configure(text='Любой напиток.')

def func_drink():
        global drink
        btn_okay5.pack_forget()
        btn_okay6.pack()
        drink = ent.get()
        print(drink)
        ent.delete(0, END)
        lbl.configure(text='Любое транспортное средство (даже военное).')

def func_car():
        global car
        btn_okay6.pack_forget()
        btn_okay7.pack()
        car = ent.get()
        print(car)
        ent.delete(0, END)
        lbl.configure(text='Любую планету (не существующую можно).')

def func_planet():
        global planet
        btn_okay7.pack_forget()
        btn_okay8.pack()
        planet = ent.get()
        print(planet)
        ent.delete(0, END)
        lbl.configure(text='Любое не существующее или выдуманное существо.')

def func_monster():
        global monster
        monster = ent.get()
        print(monster)
        btn_okay8.pack_forget()
        btn_final.pack()
        ent.pack_forget()
        ent.delete(0, END)
        lbl.configure(text='Готовы увидеть результат?')

def final():
        btn_final.pack_forget()
        story = f'Однажды {user} вышел погулять. На полу он увидел {item} и поднял его.\n ' \
                f'Решил он тогда приготовить \n{item} и пошел домой. Дом его находился\n в {city}. Пришел он на кухню и включил плиту.' \
                f'Достал сковороду и\n масло, и поставил на огонь, налив в сковороду масла.\n Затем пришел {name2} и он очень хотел ' \
                f'пить. Открыв холодос достал от туда {drink}. \nА потом выпрыгнул в окно и приземлился\n ' \
                f'как супер герой на {car}e. Сел в {car} и уехал\n на {planet}. И жил там долго и счастливо поженившись на {monster}е.'
        lbl.configure(text=story, font='Monsterrat 30')
        print(story)

def close_game():
        sys.exit()


lbl = Label(app, text='Привет! Сыграем в MadLibs?', font='Monsterrat 40')
lbl_skip = Label(app, text=' ', font='Monsterrat 20')

btn_start = Button(app, text='Да!', font='Monsterrat 30', command=start_game)
btn_close = Button(app, text='Я не хочу, дай балтику!', font='Monsterrat 30', command=close_game)

btn_okay = Button(app, text='Готово', font='Monsterrat 30', command=func_name)
btn_okay2 = Button(app, text='Готово', font='Monsterrat 30', command=func_item)
btn_okay3 = Button(app, text='Готово', font='Monsterrat 30', command=func_city)
btn_okay4 = Button(app, text='Готово', font='Monsterrat 30', command=func_sec_name)
btn_okay5 = Button(app, text='Готово', font='Monsterrat 30', command=func_drink)
btn_okay6 = Button(app, text='Готово', font='Monsterrat 30', command=func_car)
btn_okay7 = Button(app, text='Готово', font='Monsterrat 30', command=func_planet)
btn_okay8 = Button(app, text='Готово', font='Monsterrat 30', command=func_monster)

btn_final = Button(app, text='Узнать ответ', font='Monsterrat 30', command=final)

ent = Entry(app, font='Monsterrat 30')

lbl.pack()

lbl_skip.pack()
btn_start.pack()
lbl_skip.pack()
btn_close.pack()
app.geometry('1600x1000')
app.mainloop()

