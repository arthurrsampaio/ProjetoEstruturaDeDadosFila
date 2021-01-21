from fila import *
from tkinter import *


class GuiFila():

    def __init__(self):

        self.fila = inicializa_fila()

        self.window_fila = Tk()

        self.window_fila.title("GUI Fila")
        self.window_fila.geometry("400x110")
        self.window_fila.resizable(0, 0)


        self.frame = Frame(self.window_fila)
        self.frame.pack(fill="x")

        self.botao_editar = Button(self.frame, text="EDITAR", pady=3, bd=5, command=lambda: self.toplevel_editar())
        self.botao_editar.pack(fill="x")

        self.botao_imprimir = Button(self.frame, text="IMPRIMIR", pady=3, bd=5, command=lambda: self.toplevel_imprimir())
        self.botao_imprimir.pack(fill="x")

        self.botao_deletar = Button(self.frame, text="POP(Deletar)", pady=3, bd=5, command=lambda: popid(self.fila))
        self.botao_deletar.pack(fill="x")



        self.window_fila.mainloop()


    def toplevel_editar(self):
        top_editar = Toplevel()
        top_editar.geometry("300x120")

        label_categoria_editar = Label(top_editar, text="Categoria: ").grid(row=1, column=0)
        categoria_editar = Entry(top_editar)
        categoria_editar.grid(row=1, column=1)

        label_novacategoria_editar = Label(top_editar, text="Novo Valor: ").grid(row=2, column=0)
        novacategoria_editar = Entry(top_editar)
        novacategoria_editar.grid(row=2, column=1)

        botao_editar = Button(top_editar, text="Editar", command=lambda: editar(self.fila, categoria_editar.get(),
                                                                                novacategoria_editar.get())).grid(row=3, column=0, columnspan=2)

        botao_sair = Button(top_editar, text="Voltar", command=lambda: top_editar.destroy()).grid(row=4, column=0, columnspan=2)

    def toplevel_imprimir(self):

        def imprimirfila_resumida(fila, x):

            impressao.delete(0, END)

            imprimirfila = fila.inicio

            for i in range(x):
                impressao.insert(END, "Filme =" + str(i+1))

                impressao.insert(END, "  " + str(imprimirfila.id))
                impressao.insert(END, "  " + str(imprimirfila.original_title))

                imprimirfila = imprimirfila.prox

        top_imprimir = Toplevel()
        top_imprimir.geometry("600x250")
        spin = Spinbox(top_imprimir, from_=1, to=100)
        spin.pack(fill="x")

        botao_imprimir = Button(top_imprimir, text="Imprimir", command=lambda: imprimirfila_resumida(self.fila, int(spin.get())))
        botao_imprimir.pack()

        impressao = Listbox(top_imprimir)
        impressao.pack(fill="both")

        botao_sair = Button(top_imprimir, text="Voltar", command=lambda: top_imprimir.destroy()).pack()


if __name__ == '__main__':

    GuiFila()