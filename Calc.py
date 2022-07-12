"""	####################################################
	# UFRPE - Universidade Federal Rural de Pernambuco #
    # Introducao a Computacao - LF1 - Lic. em Fisica   #
	# Projeto 02 - Calculadora Cientifica para Fisica  #
	# (V1.7) de 28/08/2017                             #
	#################################################### """

from tkinter import Tk, Button, Frame, Entry, END, RIDGE, RAISED, INSERT, SUNKEN, LEFT, RIGHT, Canvas, Toplevel, Label, Menu
from math import sqrt, sin, cos, pi, tan,log as ln, exp, log
from ConfigCalc import *
from FisicaEqCalc import *
from SobreCalc import *
from FuncxCalc import *

import math 
import numpy as np
import matplotlib.pyplot as plt


def volta(self):
            tam = len(self.entry.get())
            self.entry.delete(tam-1,tam)

def zeraprim(self):
            self.entry.delete(0,END)
            
######## Frame equacoes ########
class CalcF(Frame):
    'Equacoes de fisica'
    
    def __init__(self, parent=None):
        'Construtor do frame'
        Frame.__init__(self, parent)
        self.pack(side=RIGHT)

        self.labelF = Label(self, text="Physics Calc - UFRPE",width=30, bg='#424242',fg='#ff8800',font=('bold', 5))
        self.labelF.grid(row=0, column=0, columnspan=7)
        # rótulos de botão de calculadora em uma lista 2D
        buttons = [['Vm', 'Fr'],
                   ['Epg',  'Epe'],
                   ['Ec',  'A'],
                   ['Em',    'Q'],
                   ['T',   'S' ]]

        # cria e posiciona botões em linha e coluna apropriadas
        for r in range(5):
            for c in range(2):
                # função cmd() é definida, de modo que, quando chamada
                # sem um argumento de entrada, executa
                # self.click(buttons[r][c])
                def cmd(x=buttons[r][c]):
                    self.click(x)

                b = Button(self,  # botão para símbolo buttons[r][c]
                           text=buttons[r][c],
                           width=7,
                           height=1,
                           relief=RAISED,
                           command=cmd,bg='#ff8800',fg='white')  # cmd() é o manipulador
                b.grid(row=r + 1, column=c)  # entrada é na linha 0
                
    def click(self, key):
        'manipulador para evento de pressionar tecla rotulada do botao'

        if key == 'Vm':
            WindVm(self)

        elif key == 'Fr':
            WindFr(self)

        elif key == 'Epg':
            WindEpg(self)

        elif key == 'Epe':
            WindEpe(self)

        elif key == 'Ec':
            WindEc(self)

        elif key == 'A':
            WindA(self)

        elif key == 'Em':
            WindEm(self)

        elif key == 'Q':
            WindQ(self)

        elif key == 'T':
            WindT(self)

        elif key == 'S':
            WindS(self)

######## Frame Calculadora ########
class Calc(Frame):
    'Uma calculadora'

    def __init__(self, parent=None):
        'Construtor da calc'
        Frame.__init__(self, parent)
        self.pack(side=LEFT)

        self.memory = ''  # memoria
        self.expr = ''  # expressao atual
        self.startOfNextOperand = True  # inicio do novo operando

        # usa o widget Entry para exibição
        self.entry = Entry(self, relief=RIDGE, borderwidth=5,
                           width=31, bg='#2b2b2b', fg='#ff8800',
                           font=('Helvetica', 18))
        self.entry.grid(row=0, column=0, columnspan=7)

        # rótulos de botão de calculadora em uma lista 2D
        buttons = [['MR', 'MC', 'M+', 'M-','ln', '(', ')'],
                   ['CE', 'C', '←', '-', 'sin', 'x²','n!'],
                   ['7', '8', '9','/','cos','\u221a', '%'],
                   ['4', '5', '6', '*','tan', 'x³', '1/x'],
                   ['1', '2', '3', '+','π', 'e', 'tan(x)'],
                   ['0', '=', '±', '.','cos(x)', 'sin(x)', ' ']]

        # cria e posiciona botões em linha e coluna apropriadas
        for r in range(6):
            for c in range(7):
                # função cmd() é definida, de modo que, quando chamada
                # sem um argumento de entrada, executa
                # self.click(buttons[r][c])
                def cmd(x=buttons[r][c]):
                    self.click(x)

                b = Button(self,  # botão para símbolo buttons[r][c]
                           text=buttons[r][c],
                           width=7,
                           relief=RAISED,
                           command=cmd,bg='#424242',fg='white')  # cmd() é o manipulador
                b.grid(row=r + 1, column=c)  # entrada é na linha 0

    def click(self, key):
        'manipulador para evento de pressionar tecla rotulada do botao'

        if key == '←':
            volta(self)

        elif key == 'cos(x)':
            CossenoX(self)

        elif key == 'sin(x)':
            SenoX(self)

        elif key == 'tan(x)':
            TanX(self)

        elif key == 'CE':
            zeraprim(self)

        
        elif key == '=':
            # avalia a expressão, incluindo o valor
            # exibido na entrada e o resultado apresentado
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(END, str(result))
                self.expr = ''
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Erro')


        elif key == '\u221a':
            # calcula e exibe raiz quadrada da entrada
            result = sqrt(eval(self.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(END, result)

        elif key == 'x²':
            # calcula e exibe o quadrado da entrada
            result = eval(self.entry.get()) ** 2
            self.entry.delete(0, END)
            self.entry.insert(END, result)


        elif key == "1/x":
            # exibe o resultado de um sobre o número de entrada
            result = float(1 / float(self.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(END, result)


        elif key == "sin":
            # retorna o seno do ângulo
            result = sin((float(self.entry.get()) / 180) * pi)
            self.entry.delete(0, END)
            self.entry.insert(END, result)


        elif key == "cos":
            # retorna o cosseno do ângulo
            result = cos((float(self.entry.get()) / 180) * pi)
            self.entry.delete(0, END)
            self.entry.insert(END, result)


        elif key == "tan":
            # retorna a tangente do ângulo
            result = tan((float(self.entry.get()) / 180) * pi)
            self.entry.delete(0, END)
            self.entry.insert(END, result)

        elif key == "%":

            result = ((float(self.entry.get())) * (1)) / 100
            self.entry.delete(0, END)
            self.entry.insert(END, result)

        elif key == 'ln':
            result= ln((float(self.entry.get())))
            self.entry.delete(0, END)
            self.entry.insert(END, result)
######## CALCULANDO O MESMO DO LN ########
        elif key == 'log':
            result = log((floatself.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(END, result)
            
##########################################
        elif key == 'e':
            result= exp((float(self.entry.get())))
            self.entry.delete(0, END)
            self.entry.insert(END, result)
        

        elif key == 'π':
            result= ((float(self.entry.get())* pi))
            self.entry.delete(0, END)
            self.entry.insert(END, result)

        elif key == "x²":

            result = ((float(self.entry.get()))**2)
            self.entry.delete(0, END)
            self.entry.insert(END, result)
            
        elif key == "x³":

            result = ((float(self.entry.get()))**3)
            self.entry.delete(0, END)
            self.entry.insert(END, result)

            
        elif key == "n!":
            i     = 1  # contador
            n_fat = 1            
            n= (int(self.entry.get()))
            while i <= n:
                        n_fat = n_fat * i 
                        i = i + 1
            self.entry.delete(0, END)
            self.entry.insert(END, n_fat)
                          
            
        elif key == 'C':
            # limpa a entrada
            self.entry.delete(0, END)

        elif key in {'M+', 'M-'}:
            # soma ou subtrai da memória o valor da entrada
            self.memory = str(eval(self.memory + key[1] + self.entry.get()))

        elif key == 'MR':
            # substitui valor na entrada pelo valor armazenado na memória
            self.entry.delete(0, END)
            self.entry.insert(END, self.memory)

        elif key == 'MC':
            # apaga a memória
            self.memory = ''

        elif key == '±':
            # troca entrada de positiva para negativa ou vice-versa
            # se não houver valor na entrada, não faz nada
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass


        else:
            # insere dígito ao final da entrada, ou como primeiro
            # dígito, se início do próximo operando
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand = False
            self.entry.insert(END, key)


if __name__ == '__main__':
    root = Tk()
    calc = Calc(root)
    calcf = CalcF(root)
    root.title('Calculadora Cientifica para Física v(1.7)')
    fixaTamanhoJanela(root)
    WindCenter(root)
    icon(root)
    root.geometry('235x247')
    root.configure(background='#424242')
    menubar = Menu(root)
    root.config(menu=menubar)

def quit():
        sys.exit()


def exit():
    import Utils


# cria os itens do menu principal, mas apenas na memória
itemMenuArquivo = Menu(menubar, tearoff=0)
itemMenuTipo = Menu(menubar, tearoff=0)
itemMenuHelp = Menu(menubar, tearoff=0)
    

# adiciona os itens do menu principal na barra de menu
menubar.add_cascade(label='Arquivo', menu=itemMenuArquivo)
menubar.add_cascade(label='Calculadora', menu=itemMenuTipo)
menubar.add_cascade(label='Ajuda (?)', menu=itemMenuHelp)


# fecha o programa, isto é, detroi o objeto da janela principal,
# sai do programa
# e libera a mémoria
def Quit():
    root.destroy()
    exit()

  
# adiciona uma linha separadora para agrupar subitens de menu
itemMenuArquivo.add_separator()
itemMenuArquivo.add_command(label='Sair', command=Quit)

# aumenta ou diminue root.geometry()
def Simplificar():
    root.geometry('235x247')
itemMenuTipo.add_separator()
itemMenuTipo.add_command(label='Padrão', command=Simplificar)
def Diminuir():
    root.geometry('415x247')
itemMenuTipo.add_command(label='Cientifica', command=Diminuir)

def Aumentar():
    root.geometry('533x247')
itemMenuTipo.add_command(label='Física',command=Aumentar)
itemMenuTipo.add_separator()


itemMenuHelp.add_separator()
itemMenuHelp.add_command(label='Sobre',command=windHelp)

# centraliza principal
WindCenter(root)
root.mainloop()
