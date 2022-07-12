""" Modulo de equacoes fisicas da calculadora """

from tkinter import *
from math import *
from ConfigCalc import *

import math
import numpy as np
import matplotlib.pyplot as plt

def WindVm(root):
    diag1 = Toplevel(root)
    diag1.title("Velocidade Média")
    diag1.transient(root)
    diag1.grab_set()
    diag1.geometry('350x110')  # define o tamanho inicial da janela

    label0 = Label(diag1, text="Vmed = Δs/Δt",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag1, text="Δs(Varição do deslocamento):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag1,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag1, text="Δt(Variação do tempo):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag1,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)


    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        Res = enter1 / enter2
        Res = float(Res)
        lab2 = Label(diag1, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f m/s" % (Res)
        lab2.grid(row=3, column=1)
        
        # Define o grafico da funcao
        plt.axes([0.1, 0.15, 0.8, 0.75])
        x = [0,enter2]
        y = [0,enter1]

        plt.plot(x,y,'#ff8800',linewidth=2,marker="o")
        plt.ylim(ymin=0)
        plt.xlim(xmin=0)

        plt.title(r'Velocidade Média %.2f m/s'%(Res), fontsize=20)
        plt.xlabel(r"""Tempo ( s )""", fontsize=10)
        plt.ylabel(r"""Posição ( m )""", fontsize=10)
        plt.show()
        

    bOk = Button(diag1, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=2, column=2)

    fixaTamanhoJanela(diag1)
    WindCenter(diag1)
    icon(diag1)


def WindFr(root):
    diag2 = Toplevel(root)
    diag2.title("Força resultante")
    diag2.transient(root)
    diag2.grab_set()
    diag2.geometry('270x90')  # define o tamanho inicial da janela

    label0 = Label(diag2, text="Fres = m.a",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag2, text="m(massa):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag2,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag2, text="a(aceleração):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag2,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        Res = enter1 * enter2
        Res = float(Res)
        lab2 = Label(diag2, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f N" % (Res)
        lab2.grid(row=3, column=1)

        # Define o grafico da funcao
        plt.axes([0.1, 0.15, 0.8, 0.75])
        x = [0,Res]
        y = [0,enter2]

        plt.plot(x,y,'#ff8800',linewidth=2,marker="o")
        plt.ylim(ymin=0)
        plt.xlim(xmin=0)

        plt.title(r'Força resultante %.2f N'%(Res), fontsize=20)
        plt.xlabel(r"""Força resultante ( N )""", fontsize=10)
        plt.ylabel(r"""Aceleração ( m/s² )""", fontsize=10)
        plt.show()

    bOk = Button(diag2, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=2, column=2)

    fixaTamanhoJanela(diag2)
    WindCenter(diag2)
    icon(diag2)


def WindEpg(root):
    diag3 = Toplevel(root)
    diag3.title("Energia pontencial gravitacional")
    diag3.transient(root)
    diag3.grab_set()
    diag3.geometry('290x110')  # define o tamanho inicial da janela

    label0 = Label(diag3, text="Epg = m.g.h",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag3, text="m(massa):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag3,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag3, text="g(gravidade):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag3,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    label3 = Label(diag3, text="h(altura):",bg='#424242',fg='white')
    label3.grid(row=3, column=0)
    entrada3 = Entry(diag3,bg='#2b2b2b',fg='white')
    entrada3.grid(row=3, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter3 = entrada3.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        enter3 = float(enter3)
        Res = enter1 * enter2 * enter3
        Res = float(Res)
        lab2 = Label(diag3, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f J" % (Res)
        lab2.grid(row=4, column=1)

    bOk = Button(diag3, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=3, column=3)

    fixaTamanhoJanela(diag3)
    WindCenter(diag3)
    icon(diag3)


def WindEpe(root):
    diag4 = Toplevel(root)
    diag4.title("Energia pontencial elástica")
    diag4.transient(root)
    diag4.grab_set()
    diag4.geometry('330x110')  # define o tamanho inicial da janela

    label0 = Label(diag4, text="Epe = (1/2).k.x²",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag4, text="k(constante elástica):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag4,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag4, text="x(deslocamento da mola):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag4,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        Res = (1 / 2) * enter1 * (enter2 ** 2)
        Res = float(Res)
        lab2 = Label(diag4, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f J" % (Res)
        lab2.grid(row=3, column=1)

        # Define o grafico da funcao
        a=[]
        b=[]
        A1=int(enter2)
        for x in range(-A1 ,A1):
            y = x**2
            a.append(x)
            b.append(y)
            
        fig = plt.figure()
        axes = fig.add_subplot(111)
        axes.plot(a,b,'#ff8800',linewidth=2,marker="o")
        plt.ylim(ymin=0)
        #plt.xlim(xmin=0)
        plt.title(r'Energia pontencial elástica %.2f J'%(Res),fontsize=20)
        plt.xlabel(r"""x""",fontsize=10)
        plt.ylabel(r"""Epe""",fontsize=10)
        plt.show()

    bOk = Button(diag4, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=2, column=2)

    fixaTamanhoJanela(diag4)
    WindCenter(diag4)
    icon(diag4)


def WindEc(root):
    diag5 = Toplevel(root)
    diag5.title("Energia cinética")
    diag5.transient(root)
    diag5.grab_set()
    diag5.geometry('290x90')  # define o tamanho inicial da janela

    label0 = Label(diag5, text="K = m.v²/2",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag5, text="m(massa):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag5,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag5, text="v(velocidade):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag5,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        Res = (enter1 * (enter2 ** 2)) / 2
        Res = float(Res)
        if Res < 999999999999:
            lab2 = Label(diag5, text="",bg='#ff8800',fg='white')
            lab2["text"] = "%5.2f J" % (Res)
            lab2.grid(row=3, column=1)
        else:
            lab2 = Label(diag5, text="",bg='#ff8800',fg='white')
            lab2["text"] = "OverflowError: Result too large"
            lab2.grid(row=3, column=1)

        # Define o grafico da funcao
        a=[]
        b=[]
        A1=int(enter2)
        for x in range(-A1 ,A1):
            y = (-1*(x**2)) + (Res/2)
            a.append(x)
            b.append(y)
            
        fig = plt.figure()
        axes = fig.add_subplot(111)
        axes.plot(a,b,'#ff8800',linewidth=2,marker="o")
        plt.ylim(ymin=0)
        #plt.xlim(xmin=0)
        plt.title(r'Energia cinética %.2f J'%(Res),fontsize=20)
        plt.xlabel(r"""x""",fontsize=10)
        plt.ylabel(r"""Ec""",fontsize=10)
        plt.show()

    bOk = Button(diag5, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=2, column=2)

    fixaTamanhoJanela(diag5)
    WindCenter(diag5)
    icon(diag5)


def WindA(root):
    diag6 = Toplevel(root)
    diag6.title("Aceleração Média")
    diag6.transient(root)
    diag6.grab_set()
    diag6.geometry('330x100')  # define o tamanho inicial da janela

    label0 = Label(diag6, text="Amed = Δv/Δt",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag6, text="Δv(variação da velocidade):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag6,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag6, text="Δt(variação de tempo):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag6,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        Res = enter1 / enter2
        Res = float(Res)
        lab2 = Label(diag6, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f m/s²" % (Res)
        lab2.grid(row=3, column=1)

        # Define o grafico da funcao
        plt.axes([0.1, 0.15, 0.8, 0.75])
        x = [0,enter2]
        y = [0,enter1]

        plt.plot(x,y,'#ff8800',linewidth=2,marker="o")
        plt.ylim(ymin=0)
        plt.xlim(xmin=0)

        plt.title(r'Aceleração Média %.2f m/s²'%(Res), fontsize=20)
        plt.xlabel(r"""Variação do tempo ( s )""", fontsize=10)
        plt.ylabel(r"""Variação da velocidade ( m/s )""", fontsize=10)
        plt.show()

    bOk = Button(diag6, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=2, column=2)

    fixaTamanhoJanela(diag6)
    WindCenter(diag6)
    icon(diag6)


def WindEm(root):
    diag9 = Toplevel(root)
    diag9.title("Energia mecânica")
    diag9.transient(root)
    diag9.grab_set()
    diag9.geometry('340x90')  # define o tamanho inicial da janela

    label0 = Label(diag9, text="Em = Ec+Ep",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag9, text="Ec(energia cinética):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag9,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag9, text="Ep(energia potencial):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag9,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        Res = enter1 + enter2
        Res = float(Res)
        lab2 = Label(diag9, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f J" % (Res)
        lab2.grid(row=3, column=1)

        # Define o grafico da funcao
        plt.axes([0.1, 0.15, 0.8, 0.75])
        y = [Res,Res]

        plt.plot(y,'#ff8800',linewidth=2,marker="o")
        plt.ylim(ymin=0)
        plt.xlim(xmin=0)

        plt.title(r'Energia mecânica %.2f J'%(Res), fontsize=20)
        plt.xlabel(r"""x""", fontsize=10)
        plt.ylabel(r"""Em""", fontsize=10)
        plt.show()


    bOk = Button(diag9, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=2, column=2)

    fixaTamanhoJanela(diag9)
    WindCenter(diag9)
    icon(diag9)


def WindQ(root):
    diag7 = Toplevel(root)
    diag7.title("Quatidade de movimento")
    diag7.transient(root)
    diag7.grab_set()
    diag7.geometry('300x90')  # define o tamanho inicial da janela

    label0 = Label(diag7, text="Q = m.v",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag7, text="m(massa):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag7,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag7, text="v(velocidade):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag7,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        Res = enter1 * enter2
        Res = float(Res)
        lab2 = Label(diag7, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f Kg.m/s" % (Res)
        lab2.grid(row=3, column=1)

        # Define o grafico
        plt.axes([0.1, 0.15, 0.8, 0.75])
        x = [0,Res]
        y = [0,enter2]

        plt.plot(x,y,'#ff8800',linewidth=2,marker="o")
        plt.ylim(ymin=0)
        plt.xlim(xmin=0)

        plt.title(r'Quantidade de movimento %.2f Kg.m/s'%(Res), fontsize=20)
        plt.xlabel(r"""Quantidade de movimento ( Kg.m/s )""", fontsize=10)
        plt.ylabel(r"""Velocidade ( m/s )""", fontsize=10)
        plt.show()

    bOk = Button(diag7, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=2, column=3)

    fixaTamanhoJanela(diag7)
    WindCenter(diag7)
    icon(diag7)


def WindT(root):
    diag8 = Toplevel(root)
    diag8.title("Trabalho")
    diag8.transient(root)
    diag8.grab_set()
    diag8.geometry('350x110')  # define o tamanho inicial da janela

    label0 = Label(diag8, text="τ = F.Δx.cos(Θ)",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag8, text="F(força):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag8,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag8, text="Δx(variação do deslocamento):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag8,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    label3 = Label(diag8, text="Θ(ângulo):",bg='#424242',fg='white')
    label3.grid(row=3, column=0)
    entrada3 = Entry(diag8,bg='#2b2b2b',fg='white')
    entrada3.grid(row=3, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter3 = entrada3.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        enter3 = float(enter3)
        Res = (enter1 * enter2 * (math.cos(enter3)))
        Res = float(Res)
        lab2 = Label(diag8, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f J" % (Res)
        lab2.grid(row=4, column=1)

        # Define o grafico da funcao
        Ox = np.linspace(-Res, Res, 512, endpoint=True)
        Cosseno = np.cos(Ox)
        plt.plot(Ox, Cosseno, '#ff8800',linewidth=2,marker="o")

        plt.title(r'Trabalho %.2f J'%(Res), fontsize=20)
        plt.xlabel(r"""x""", fontsize=10)
        plt.ylabel(r"""y""", fontsize=10)
        plt.show()

    bOk = Button(diag8, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=3, column=2)

    fixaTamanhoJanela(diag8)
    WindCenter(diag8)
    icon(diag8)




def WindS(root):
    diag10 = Toplevel(root)
    diag10.title("Espaço")
    diag10.transient(root)
    diag10.grab_set()
    diag10.geometry('350x110')  # define o tamanho inicial da janela

    label0 = Label(diag10, text="S = So+(v.t)",bg='#424242',fg='white')
    label0.grid(row=0, column=1)

    label1 = Label(diag10, text="S(espaço inicial):",bg='#424242',fg='white')
    label1.grid(row=1, column=0)
    entrada1 = Entry(diag10,bg='#2b2b2b',fg='white')
    entrada1.grid(row=1, column=1)

    label2 = Label(diag10, text="v(velocidade):",bg='#424242',fg='white')
    label2.grid(row=2, column=0)
    entrada2 = Entry(diag10,bg='#2b2b2b',fg='white')
    entrada2.grid(row=2, column=1)

    label3 = Label(diag10, text="t(tempo):",bg='#424242',fg='white')
    label3.grid(row=3, column=0)
    entrada3 = Entry(diag10,bg='#2b2b2b',fg='white')
    entrada3.grid(row=3, column=1)

    def comm():
        # Define entradas
        enter1 = entrada1.get()
        enter2 = entrada2.get()
        enter3 = entrada3.get()
        enter1 = float(enter1)
        enter2 = float(enter2)
        enter3 = float(enter3)
        Res = (enter1 + (enter2 * enter3))
        Res = float(Res)
        lab2 = Label(diag10, text="",bg='#ff8800',fg='white')
        lab2["text"] = "%.2f m" % (Res)
        lab2.grid(row=4, column=1)

        # Define o grafico da funcao
        plt.axes([0.1, 0.15, 0.8, 0.75])
        y = [Res,Res]

        plt.plot(y,'#ff8800',linewidth=2,marker="o")
        plt.ylim(ymin=0)
        plt.xlim(xmin=0)

        plt.title(r'Espaço %.2f m'%(Res), fontsize=20)
        plt.xlabel(r"""x""", fontsize=10)
        plt.ylabel(r"""S""", fontsize=10)
        plt.show()

    bOk = Button(diag10, text="=",bg='#424242',fg='white')
    bOk["command"] = comm
    bOk.grid(row=3, column=2)

    fixaTamanhoJanela(diag10)
    WindCenter(diag10)
    icon(diag10)
