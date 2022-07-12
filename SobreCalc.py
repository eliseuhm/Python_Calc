""" Modulo "help" """

from tkinter import *
from ConfigCalc import *

def windHelp():
    diag = Toplevel()
    diag.title("Sobre")
    diag.transient()
    diag.grab_set()
    diag.geometry('200x200')

    explan = """
Calculadora Cientifica para Física
v(1.7)
UFRPE
Introdução a Computação
Turma: LF1 - 2017.1
Lic. em Física

Grupo 02:
Eliseu H. M.
Flávia Eduarda
"""
    w = Label(diag, justify=CENTER,padx=10 , text=explan, bg='#424242',fg='#ff8800').pack()
    
    fixaTamanhoJanela(diag)
    WindCenter(diag)
    icon(diag)
