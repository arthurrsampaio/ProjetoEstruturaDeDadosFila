from lista import *
from tkinter import *

class GuiLista():

    def __init__(self):

        self.lista1 = inicializar_lista()

        self.window_lista = Tk()

        self.window_lista.title("GUI Lista")
        self.window_lista.geometry("400x110")
        self.window_lista.resizable(0, 0)


        self.frame = Frame(self.window_lista)
        self.frame.pack(fill="x")

        self.botao_editar = Button(self.frame, text="EDITAR", pady=3, bd=5, command=lambda: self.toplevel_editar()).pack(fill="x")
        self.botao_imprimir = Button(self.frame, text="IMPRIMIR", pady=3, bd=5, command=lambda: self.toplevel_imprimir()).pack(fill="x")
        self.botao_deletar = Button(self.frame, text="DELETAR", pady=3, bd=5, command=lambda: self.toplevel_deletar()).pack(fill="x")



        self.window_lista.mainloop()


    def toplevel_editar(self):
        top_editar = Toplevel()
        top_editar.geometry("300x120")

        label_id_editar = Label(top_editar, text="ID: ").grid(row=0, column=0)
        id_editar = Entry(top_editar)
        id_editar.grid(row=0, column=1)

        label_categoria_editar = Label(top_editar, text="Categoria: ").grid(row=1, column=0)
        categoria_editar = Entry(top_editar)
        categoria_editar.grid(row=1, column=1)

        label_novacategoria_editar = Label(top_editar, text="Novo Valor: ").grid(row=2, column=0)
        novacategoria_editar = Entry(top_editar)
        novacategoria_editar.grid(row=2, column=1)

        botao_editar = Button(top_editar, text="Editar", command=lambda: editar(self.lista1, int(id_editar.get()), categoria_editar.get(),
                                                                                novacategoria_editar.get())).grid(row=3, column=0, columnspan=2)

        botao_sair = Button(top_editar, text="Voltar", command=lambda: top_editar.destroy()).grid(row=4, column=0, columnspan=2)

    def toplevel_imprimir(self):

        def imprimirlista_resumida(lista, x):

            impressao.delete(0, END)

            imprimirlist = lista.prox

            for i in range(x):
                impressao.insert(END,"Filme =" + str(i+1))

                impressao.insert(END, "  " + str(imprimirlist.id))
                impressao.insert(END, "  " + str(imprimirlist.original_title))

                imprimirlist = imprimirlist.prox

        top_imprimir = Toplevel()
        top_imprimir.geometry("600x250")

        spin = Spinbox(top_imprimir, from_=1, to=100)
        spin.pack(fill="x")

        botao_imprimir = Button(top_imprimir, text="Imprimir", command=lambda: imprimirlista_resumida(self.lista1, int(spin.get())))
        botao_imprimir.pack()

        impressao = Listbox(top_imprimir)
        impressao.pack(fill="both")

        botao_sair = Button(top_imprimir, text="Voltar", command=lambda: top_imprimir.destroy()).pack()

    def toplevel_deletar(self):
        top_deletar = Toplevel()
        label = Label(top_deletar, text="Digite o id que deseja deletar: ").pack(side="left")
        entry = Entry(top_deletar)
        entry.pack(side="left")

        botao_deletar = Button(top_deletar, text="Deletar", command=lambda: delete(self.lista1, int(entry.get())))
        botao_deletar.pack()


        botao_sair = Button(top_deletar, text="Voltar", command=lambda: top_deletar.destroy()).pack(side=BOTTOM)

if __name__ == '__main__':
    GuiLista()