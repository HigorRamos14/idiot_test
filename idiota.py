from tkinter import *
import random

def random_y_and_x():
    nao.destroy
    y_nao = random.randint(50, 250)
    x_nao = random.randint(50, 330)
    nao.place(x=x_nao,
        y=y_nao)

def pressed_sim():
    wind_prin.destroy()
    wind_sim= Tk()
    wind_sim.geometry('300x200')
    wind_sim.resizable(0, 0)

    label = Label(wind_sim, text=':D Eu já sabia, OTÁRIO :D')

    label.place(x=85,
                y=70)

    wind_sim.mainloop


wind_prin = Tk()

# config da janela
wind_prin.geometry('400x300')

wind_prin.resizable(0, 0)


# label
label = Label(text='Você é um idiota?',)


# botoes
sim = Button(text='Sim', command=pressed_sim,
            width=10)

nao = Button(text='Não', command=random_y_and_x,
            width=10)

x_nao = 250
y_nao = 250


# .pack, .place
label.pack()
sim.place(x=100,
        y=250)

nao.place(x=x_nao,
        y=y_nao)


wind_prin.mainloop()
