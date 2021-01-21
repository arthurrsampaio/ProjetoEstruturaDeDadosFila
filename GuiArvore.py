from arvore import *
from tkinter import *


class GuiArvore():

    def __init__(self):

        self.arvore = inicializa_arvore()

        self.window_arvore = Tk()

        self.window_arvore.title("GUI Árvore")
        self.window_arvore.geometry("400x110")
        self.window_arvore.resizable(0, 0)


        self.frame = Frame(self.window_arvore)
        self.frame.pack(fill="x")

        self.botao_editar = Button(self.frame, text="Editar", pady=3, bd=5, command=lambda: self.toplevel_Editar())
        self.botao_editar.pack(fill="x")

        self.botao_imprimir = Button(self.frame, text="Imprimir", pady=3, bd=5, command=lambda: self.toplevel_imprimir())
        self.botao_imprimir.pack(fill="x")

        self.botao_imprimir = Button(self.frame, text="Excluir", pady=3, bd=5, command=lambda: self.toplevel_excluir())
        self.botao_imprimir.pack(fill="x")


        self.window_arvore.mainloop()


    def toplevel_Editar(self):



        top_editar = Toplevel()
        top_editar.geometry("250x300")
        top_editar.resizable(0,0)

        top = Frame(top_editar)
        top.pack()

        label_ID_origem = Label(top, text="ID do Nó: ")
        label_ID_origem.pack()

        ID_origem = Entry(top)
        ID_origem.pack(fill="x")

        label_categoria = Label(top, text="Categoria: ")
        label_categoria.pack()

        categoria = Entry(top)
        categoria.pack(fill="x")

        label_novo = Label(top, text="Nova Informação: ")
        label_novo.pack()

        novo = Entry(top)
        novo.pack(fill="x")

        botao_buscar = Button(top, text="Editar",
                              command=lambda: editar(self.arvore, categoria.get(), novo.get(), ID_origem.get()))
        botao_buscar.pack()


        botao_sair = Button(top, text="Voltar", command=lambda: top_editar.destroy()).pack()

    def toplevel_imprimir(self):

        def imprimirlista_resumida(arvore):

            impressao.delete(0, END)

            def imprimir(arvore):
                if (arvore != None):
                    imprimir(arvore.left)
                    impressao.insert(END, str(arvore.id))
                    impressao.insert(END, " " + str(arvore.original_title))
                    imprimir(arvore.right)

            imprimir(arvore)

        top_imprimir = Toplevel()
        top_imprimir.geometry("600x250")

        botao_imprimir = Button(top_imprimir, text="Imprimir",
                                command=lambda: imprimirlista_resumida(self.arvore))
        botao_imprimir.pack()

        impressao = Listbox(top_imprimir)
        impressao.pack(fill="both")

    def toplevel_excluir(self):

        top_excluir = Toplevel()
        top_excluir.geometry("250x300")
        top_excluir.resizable(0, 0)

        label_ID_origem = Label(top_excluir, text="ID do Nó: ")
        label_ID_origem.pack()

        ID_origem = Entry(top_excluir)
        ID_origem.pack(fill="x")

        botao_excluir = Button(top_excluir, text="Excluir",
                              command=lambda: removeno(self.arvore, ID_origem.get()))
        botao_excluir.pack()

        botao_sair = Button(top_excluir, text="Voltar", command=lambda: top_excluir.destroy()).pack()



if __name__ == '__main__':

    GuiArvore()