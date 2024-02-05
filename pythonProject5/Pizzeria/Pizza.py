from tkinter import *
from PIL import Image, ImageTk
import sys

class Pizzas:
    def __init__(self, tk):
        self.tk = tk
        self.price = 0
        self.pizzas = []
        self.lbl_title = Label(self.tk, text='Добро пожаловать в Bellissimo Pizza!', font='Monsterrat 30')
        self.btn_accept = Button(self.tk, text='Продолжить', font='Monsterrat 20', command=self.start)
        self.btn_cancel = Button(self.tk, text='Выход', font='Monsterrat 20', command=self.close)
        self.btn_chek = Button(self.tk, text='Подтвердить', font='Monsterrat 22', command=self.chek)
        self.btn_cont = Button(self.tk, text='Продолжить', font='Monsterrat 22', command=self.cont)
        self.btn_dost = Button(self.tk, text='Оформить доставку', font='Monsterrat 22', command=self.dostav)
        self.btn_otm = Button(self.tk, text='Выход', font='Monsterrat 22', command=self.close)
        self.lbl_title2 = Label(self.tk, text='', font='Monsterrat 30')
        self.lbl_title3 = Label(self.tk, text='', font='Monsterrat 30')

    def start(self):
        self.lbl_title.configure(text='Выберите какую пиццу хотите заказать.')
        self.btn_accept.grid_forget()
        self.btn_cancel.grid_forget()
        self.btn_pizza1.grid(row=1, column=0, padx=(0, 900))
        self.btn_pizza2.grid(row=1, column=0, padx=(200, 0))
        self.btn_pizza3.grid(row=1, column=0, padx=(1100, 0))
        self.btn_chek.grid(row=2, column=0, pady=40)

    def close(self):
        sys.exit()

    def chek(self):
        if len(self.pizzas) > 0:
            self.btn_pizza1.grid_forget()
            self.btn_pizza2.grid_forget()
            self.btn_pizza3.grid_forget()
            pizzas_str = ', '.join(self.pizzas)
            self.lbl_title.configure(text=f'Вот ваш заказ: \n{pizzas_str}\nОкончательная цена: {self.price}$')
            self.btn_chek.grid_forget()
            self.btn_cont.grid(row=3, column=0)
        elif len(self.pizzas) <= 0:
            self.btn_pizza1.grid_forget()
            self.btn_pizza2.grid_forget()
            self.btn_pizza3.grid_forget()
            self.btn_chek.grid_forget()
            self.lbl_title.configure(text='Вы ничего не заказали')
            self.btn_otm.grid(row=1, column=0)

    def cont(self):
        self.btn_cont.grid_forget()
        self.lbl_title.configure(text='Подождите. Ваш заказ обрабатывается...')
        self.lbl_title2.configure(text='Заказ принят. Идет готовка.')
        self.lbl_title3.configure(text='Заказ готов.')
        self.btn_dost.grid(row=3, column=0)
        self.lbl_title2.grid(row=1, column=0)
        self.lbl_title3.grid(row=2, column=0)

    def dostav(self):
        self.lbl_title2.grid_forget()
        self.lbl_title3.grid_forget()
        self.lbl_title.configure(text='Спасибо за покупку!')
        self.btn_dost.grid_forget()

class PeperoniPizza(Pizzas):
    def __init__(self, tk):
        super().__init__(tk)
        self.btn_pizza1 = Button(self.tk, image=img_pizza1, text='Пеперони 15$', compound='top', font='Monsterrat 25', command=self.peperoni)
        self.btn_pizza2 = Button(self.tk, image=img_pizza2, text='Маргарита 11$', compound='top', font='Monsterrat 25', command=self.margarita)
        self.btn_pizza3 = Button(self.tk, image=img_pizza3, text='Гавайская 20$', compound='top', font='Monsterrat 25', command=self.gavaiska)

    def peperoni(self):
        self.pizzas.append('Пеперони')
        self.price += 15
        print(self.price)

    def margarita(self):
        self.pizzas.append('Маргарита')
        self.price += 11
        print(self.price)

    def gavaiska(self):
        self.pizzas.append('Гавайская')
        self.price += 20
        print(self.price)

class MargaritaPizza(Pizzas):
    def __init__(self, tk):
        super().__init__(tk)
        self.btn_pizza1 = Button(self.tk, image=img_pizza1, text='Пеперони 15$', compound='top', font='Monsterrat 25', command=self.peperoni)
        self.btn_pizza2 = Button(self.tk, image=img_pizza2, text='Маргарита 11$', compound='top', font='Monsterrat 25', command=self.margarita)
        self.btn_pizza3 = Button(self.tk, image=img_pizza3, text='Гавайская 20$', compound='top', font='Monsterrat 25', command=self.gavaiska)

    def peperoni(self):
        self.pizzas.append('Пеперони')
        self.price += 15
        print(self.price)

    def margarita(self):
        pass

    def gavaiska(self):
        pass

class GavaiskaPizza(Pizzas):
    def __init__(self, tk):
        super().__init__(tk)
        self.btn_pizza1 = Button(self.tk, image=img_pizza1, text='Пеперони 15$', compound='top', font='Monsterrat 25', command=self.peperoni)
        self.btn_pizza2 = Button(self.tk, image=img_pizza2, text='Маргарита 11$', compound='top', font='Monsterrat 25', command=self.margarita)
        self.btn_pizza3 = Button(self.tk, image=img_pizza3, text='Гавайская 20$', compound='top', font='Monsterrat 25', command=self.gavaiska)

    def peperoni(self):
        self.pizzas.append('Пеперони')
        self.price += 15
        print(self.price)

    def margarita(self):
        pass

    def gavaiska(self):
        pass

tk = Tk()

img_pizza1 = Image.open('icons/peperoni.png')
img_pizza2 = Image.open('icons/margarita.png')
img_pizza3 = Image.open('icons/gavaiska.png')

img_pizza1 = ImageTk.PhotoImage(img_pizza1)
img_pizza2 = ImageTk.PhotoImage(img_pizza2)
img_pizza3 = ImageTk.PhotoImage(img_pizza3)

peperoni_pizza = PeperoniPizza(tk)
margarita_pizza = MargaritaPizza(tk)
gavaiska_pizza = GavaiskaPizza(tk)

peperoni_pizza.lbl_title.grid(column=0, row=0)
peperoni_pizza.btn_accept.grid(column=0, row=1)
peperoni_pizza.btn_cancel.grid(column=2, row=1)

tk.title('Bellissimo Pizza')
tk.geometry('1600x1000')
tk.iconbitmap('icons/pizza_icon.ico')
tk.mainloop()
