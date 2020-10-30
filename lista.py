import pandas
import random

arquivo = pandas.read_csv("tmdb_5000_movies.csv")


class No:
    def __init__(self, arquivo, x):
        # criando no definindo suas variaveis
        self.budget = arquivo['budget'][x]
        self.genres = arquivo['genres'][x]
        self.homepage = arquivo['homepage'][x]
        self.id = arquivo['id'][x]
        self.keywords = arquivo['keywords'][x]
        self.original_language = arquivo['original_language'][x]
        self.original_title = arquivo['original_title'][x]
        self.overview = arquivo['overview'][x]
        self.popularity = arquivo['popularity'][x]
        self.production_companies = arquivo['production_companies'][x]
        self.production_countries = arquivo['production_countries'][x]
        self.release_date = arquivo['release_date'][x]
        self.revenue = arquivo['revenue'][x]
        self.runtime = arquivo['runtime'][x]
        self.spoken_languages = arquivo['spoken_languages'][x]
        self.status = arquivo['status'][x]
        self.tagline = arquivo['tagline'][x]
        self.title = arquivo['title'][x]
        self.vote_average = arquivo['vote_average'][x]
        self.vote_count = arquivo['vote_count'][x]

        self.prox = None




class Cabeca:
    def __init__(self):
        self.prox = None


def editar(lista, id, antigo, novo):
    # funcao que edita um no recebendo sua posicao e o atributo antigo e novo
    listateste = lista.prox
    while (listateste and id != listateste.id):
        listateste = listateste.prox

    setattr(listateste, antigo, novo)
    #listates.antigo = novo
def busca (id,lista):

    listanova = lista.prox
    while  (listanova and listanova.id != id):
        listanova=listanova.prox

    if(listanova and listanova.id==id):
        return 1
    return 0
def inserir(dado, lista, x):

    # funcao que insere o no de maneira ordenada baseado na media de votos
    novono = No(dado, x)
    if lista.prox != None:
        if busca(novono.id,lista) == 1:
            return 1
    if lista.prox is None:
        lista.prox = novono
        return
    # cabeca 4 5 6

    atual = lista.prox
    previous = None

    while atual and atual.vote_average <= novono.vote_average:
        previous = atual
        atual = atual.prox

    if previous is None:
        # é menor que o primeiro entao insere na cabeca
        novono.prox = lista.prox
        lista.prox = novono
    else:

        novono.prox = previous.prox
        previous.prox = novono


def delete(lista, id):
    # funcao para deletar um no da lista que recebe sua posição
    listateste = lista.prox
    previous = lista.prox
    cont=0

    while( listateste and id != listateste.id ):
        previous = listateste
        listateste = listateste.prox
        cont+=1
    if cont!=0:
        previous.prox = listateste.prox
        listateste.prox = None
    else:
        lista.prox=lista.prox.prox


def imprimirlista(lista, x):
    # funcaoqueimprimealista
    imprimirlist = lista.prox
    for i in range(x):
        print("Filme =", i)
        print(imprimirlist.budget)
        print(imprimirlist.genres)
        print(imprimirlist.homepage)
        print(imprimirlist.id)
        print(imprimirlist.keywords)
        print(imprimirlist.original_language)
        print(imprimirlist.original_title)
        print(imprimirlist.overview)
        print(imprimirlist.popularity)
        print(imprimirlist.production_companies)
        print(imprimirlist.production_countries)
        print(imprimirlist.release_date)
        print(imprimirlist.revenue)
        print(imprimirlist.runtime)
        print(imprimirlist.spoken_languages)
        print(imprimirlist.status)
        print(imprimirlist.tagline)
        print(imprimirlist.title)
        print(imprimirlist.vote_average)
        print(imprimirlist.vote_count)
        print(' ')

        imprimirlist = imprimirlist.prox


lista1 = Cabeca()
cont = 0
contlista=0
while contlista!=100:
    # inserir 100 filmes aleatorios
    x = random.randint(0,len(arquivo['budget']))
    if inserir(arquivo, lista1, x) != 1:
        contlista +=1

deleditar = input("Digite sua opção(0=sair, 1 = Editar, 2 = Deletar,3 = Imprimir) ")

while int(deleditar) != 0:
    if int(deleditar) == 1:
        id = input("Digite o id: ")
        cat = input("Digite a Categoria: ")
        new = input("Digite o Novo: ")
        editar(lista1, int(id), cat, new)

    elif int(deleditar) == 2:
        id = input("Digite o id que deseja deletar: ")
        delete(lista1, int(id))
        cont += 1


    elif int(deleditar) == 3:
        imprimirlista(lista1, 100 - cont)

    deleditar = input("Digite sua opção(0=sair, 1 = Editar, 2 = Deletar,3 = Imprimir) ")