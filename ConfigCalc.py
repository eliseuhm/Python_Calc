""" Modulo de configuracao da calculadora """


# Muda icone do app
def icon(icone):
    icone.iconbitmap('ico\Atom_physics.ico')

# Fixa o tamanho da janela
def fixaTamanhoJanela(janela):
    janela.resizable(0, 0)
    janela.configure(background='#424242')

# Centraliza o tamanho da janela
def WindCenter(janela):
    """ Centraliza uma janela """
    janela.update_idletasks()
    width = janela.winfo_width()
    frm_width = janela.winfo_rootx() - janela.winfo_x()
    win_width = width + 2 * frm_width
    height = janela.winfo_height()
    titlebar_height = janela.winfo_rooty() - janela.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = janela.winfo_screenwidth() // 2 - win_width // 2
    y = janela.winfo_screenheight() // 2 - win_height // 2
    janela.geometry('{}x{}+{}+{}'.format(width, height, x, y))
