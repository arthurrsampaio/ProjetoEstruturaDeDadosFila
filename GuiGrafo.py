from grafo import *
from tkinter import *


class GuiGrafo():

    def __init__(self):

        self.grafo = inicializa_grafo()

        self.window_grafo = Tk()

        self.window_grafo.title("GUI Grafo")
        self.window_grafo.geometry("400x110")
        self.window_grafo.resizable(0, 0)


        self.frame = Frame(self.window_grafo)
        self.frame.pack(fill="x")

        self.botao_editar = Button(self.frame, text="Dijsktra", pady=3, bd=5, command=lambda: self.toplevel_Dijsktra())
        self.botao_editar.pack(fill="x")

        self.botao_imprimir = Button(self.frame, text="Imprimir", pady=3, bd=5, command=lambda: self.toplevel_imprimir())
        self.botao_imprimir.pack(fill="x")


        self.window_grafo.mainloop()


    def toplevel_Dijsktra(self):

        def caminho(inicial, final, listas):
            newlist = []
            i = final
            j = 0
            while i != inicial and j < 10:
                j += 1
                newlist.append(i)
                i = listas.p[i]
            if j < 10:
                newlist.append(inicial)
                newlist.reverse()
                impressao.insert(END,"Caminho: " + str(newlist))


        def dijsktra(grafo, vertice, final):
            aberto = []
            listas = initD(vertice)
            for i in range(grafo.nvert):
                aberto.append(1)
            while isopen(grafo, aberto):
                u = smallerdist(grafo, aberto, listas)
                aberto[u] = 0
                ad = grafo.verticies[u].cabeca
                while ad:
                    relaxa(grafo, listas, u, ad.vertice)
                    ad = ad.prox
            if int(listas.d[final]) != 50000:
                impressao.insert(END,"Distância: " + str(listas.d[final]))
                caminho(vertice, final, listas)
            else:
                impressao.insert(END, "Não existe caminho")


        top_Dijsktra = Toplevel()
        top_Dijsktra.geometry("250x300")
        top_Dijsktra.resizable(0,0)

        top = Frame(top_Dijsktra)
        top.pack()

        label_ID_origem = Label(top, text="ID de origem: ")
        label_ID_origem.pack()

        ID_origem = Entry(top)
        ID_origem.pack(fill="x")

        label_ID_destino = Label(top, text="ID de Destino: ")
        label_ID_destino.pack()
        ID_destino = Entry(top)
        ID_destino.pack(fill="x")

        botao_buscar = Button(top, text="Buscar",
                              command=lambda: dijsktra(self.grafo, buscar(self.grafo, ID_origem.get()),
                                                       buscar(self.grafo, ID_destino.get())))
        botao_buscar.pack()

        bottom = Frame(top_Dijsktra)
        bottom.pack()

        impressao = Listbox(bottom, width=40)
        impressao.pack(fill="x")

        botao_sair = Button(bottom, text="Voltar", command=lambda: top_Dijsktra.destroy()).pack()

    def toplevel_imprimir(self):

        def imprimirgrafo_resumida(grafo):

            impressao.delete(0, END)

            for i in range(grafo.nvert):
                impressao.insert(END, "Vértice = " + str(i))
                fk = grafo.verticies[i]
                fk2 = grafo.verticies[i].cabeca
                while fk2:
                    impressao.insert(END, "  " + str(fk2.vertice))
                    fk2 = fk2.prox
                impressao.insert(END, "  " + "TweetID: " + str(fk.tweetId))


        top_imprimir = Toplevel()
        top_imprimir.geometry("600x250")

        botao_imprimir = Button(top_imprimir, text="Imprimir", command=lambda: imprimirgrafo_resumida(self.grafo))
        botao_imprimir.pack()

        impressao = Listbox(top_imprimir)
        impressao.pack(fill="both")

        botao_sair = Button(top_imprimir, text="Voltar", command=lambda: top_imprimir.destroy()).pack()

if __name__ == '__main__':

    GuiGrafo()