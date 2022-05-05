from tkinter import *
import random

class testeIdiota():
        def __init__(self):

                self.janelaPrincipal = Tk()
                self.janelaPrincipal.geometry('400x300')
                self.janelaPrincipal.resizable(0, 0)
                self.janelaPrincipal.config(background='gray')

                self.labelDaJanelaPrincipal = Label(self.janelaPrincipal, text='Você é um idiota?\nTESTE AGORA', background='gray')
                self.labelDaJanelaPrincipal.pack()

                self.botaoSim = Button(text='Sim', command=self.funcaoDoBotaoSim, width=10)
                self.botaoSim.place(x=100, y=250)

                self.botaoNao = Button(text='Não', command=self.posicaoAleatoriaDoBotaoNao, width=10)
                self.botaoNao.place(x=250, y=250)

                self.janelaPrincipal.mainloop()

        def posicaoAleatoriaDoBotaoNao(self):

                self.botaoNao.destroy
                self.y_nao = random.randint(50, 250)
                self.x_nao = random.randint(50, 330)
                self.botaoNao.place(x=self.x_nao, y=self.y_nao)
        
        def funcaoDoBotaoSim(self):
                self.janelaPrincipal.destroy()

                self.janelaDoBotaoSim= Tk()
                self.janelaDoBotaoSim.geometry('300x200')
                self.janelaDoBotaoSim.resizable(0, 0)

                self.labelDaJanelaDoBotaoSim = Label(self.janelaDoBotaoSim, text=':D Eu já sabia, OTÁRIO :D')
                self.labelDaJanelaDoBotaoSim.place(x=85, y=70)

                self.janelaDoBotaoSim.mainloop 

testeIdiota()