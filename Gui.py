from GuiArvore import *
from GuiGrafo import *
from GuiFila import *
from GuiPilha import *
from GuiLista import *

class Gui():

    def __init__(self):

        self.window = Tk()

        self.window.title("GUI Estrutura de Dados")
        self.window.geometry("400x180")
        self.window.resizable(0, 0)

        self.botao_lista = Button(self.window, text="Lista", pady=3, bd=5,
                                   command=lambda: GuiLista()).pack(fill="x")
        self.botao_fila = Button(self.window, text="Fila", pady=3, bd=5,
                                     command=lambda: GuiFila()).pack(fill="x")
        self.botao_pilha = Button(self.window, text="Pilha", pady=3, bd=5,
                                    command=lambda: GuiPilha()).pack(fill="x")
        self.botao_arvore = Button(self.window, text="Árvore", pady=3, bd=5,
                                    command=lambda: GuiArvore()).pack(fill="x")
        self.botao_grafo = Button(self.window, text="Grafo", pady=3, bd=5,
                                    command=lambda: GuiGrafo()).pack(fill="x")

        self.window.mainloop()

if __name__ == "__main__":

    Gui()