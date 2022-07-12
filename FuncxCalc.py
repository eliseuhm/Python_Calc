''' Modulo de funcoes '''

from tkinter import *
from math import *
from ConfigCalc import *

import math
import numpy as np
import matplotlib.pyplot as plt

def CossenoX(root):
    diag = Toplevel(root)
    diag.title("f(x)=cos(x)")
    diag.transient(root)
    diag.grab_set()
    diag.geometry('204x45')  # define o tamanho inicial da janela

    label1 = Label(diag, text="f(x)=cos(x)",bg='#424242',fg='white')
    label1.grid(row=0, column=0)
    entrada1 = Entry(diag,bg='#2b2b2b',fg='white')
    entrada1.grid(row=0, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter1 = float(enter1)
        lab2 = Label(diag, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f" % (enter1)
        lab2.grid(row=4, column=1)

        # Define o grafico da funcao
        Ox = np.linspace(-enter1, enter1, 512, endpoint=True)
        Cosseno = np.cos(Ox)
        plt.plot(Ox, Cosseno, '#ff8800',linewidth=1)

        plt.title(r'f(x)=cos(x) %.2f'%(enter1), fontsize=20)
        plt.xlabel(r"""x""", fontsize=10)
        plt.ylabel(r"""y""", fontsize=10)
        plt.show()

    bOk = Button(diag, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=0, column=2)

    fixaTamanhoJanela(diag)
    WindCenter(diag)
    icon(diag)

def SenoX(root):
    diag = Toplevel(root)
    diag.title("f(x)=sin(x)")
    diag.transient(root)
    diag.grab_set()
    diag.geometry('204x45')  # define o tamanho inicial da janela

    label1 = Label(diag, text="f(x)=sin(x)",bg='#424242',fg='white')
    label1.grid(row=0, column=0)
    entrada1 = Entry(diag,bg='#2b2b2b',fg='white')
    entrada1.grid(row=0, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter1 = float(enter1)
        lab2 = Label(diag, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f" % (enter1)
        lab2.grid(row=4, column=1)

        # Define o grafico da funcao
        Ox = np.linspace(-enter1, enter1, 512, endpoint=True)
        Seno = np.sin(Ox)
        plt.plot(Ox, Seno, '#ff8800',linewidth=1)

        plt.title(r'f(x)=sin(x) %.2f'%(enter1), fontsize=20)
        plt.xlabel(r"""x""", fontsize=10)
        plt.ylabel(r"""y""", fontsize=10)
        plt.show()

    bOk = Button(diag, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=0, column=2)

    fixaTamanhoJanela(diag)
    WindCenter(diag)
    icon(diag)

def TanX(root):
    diag = Toplevel(root)
    diag.title("f(x)=tan(x)")
    diag.transient(root)
    diag.grab_set()
    diag.geometry('204x45')  # define o tamanho inicial da janela

    label1 = Label(diag, text="f(x)=tan(x)",bg='#424242',fg='white')
    label1.grid(row=0, column=0)
    entrada1 = Entry(diag,bg='#2b2b2b',fg='white')
    entrada1.grid(row=0, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter1 = float(enter1)
        lab2 = Label(diag, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f" % (enter1)
        lab2.grid(row=4, column=1)

        # Define o grafico da funcao
        Ox = np.linspace(-enter1, enter1, 512, endpoint=True)
        Tangente = np.tan(Ox)
        plt.plot(Ox, Tangente, '#ff8800',linewidth=1)

        plt.title(r'f(x)=tan(x) %.2f'%(enter1), fontsize=20)
        plt.xlabel(r"""x""", fontsize=10)
        plt.ylabel(r"""y""", fontsize=10)
        plt.show()

    bOk = Button(diag, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=0, column=2)

    fixaTamanhoJanela(diag)
    WindCenter(diag)
    icon(diag)
