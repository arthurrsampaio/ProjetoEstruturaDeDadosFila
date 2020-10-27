import pandas
import random

arquivo = pandas.read_csv("tmdb_5000_movies.csv")


class No:
    def __init__(self, arquivo, x):
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


def editar(lista, numero, antigo, novo):
    listateste = lista.prox
    for i in range(numero):
        listateste = listateste.prox

    setattr(listateste, antigo, novo)


def inserir(dado, lista, x):
    novono = No(dado, x)
    if (lista.prox == None):
        lista.prox = novono
        return

    atual = lista.prox
    previous = None

    while (atual and atual.vote_average <= novono.vote_average):
        previous = atual
        atual = atual.prox
    if (previous == None):
        novono.prox = lista.prox
        lista.prox = novono
    else:

        novono.prox = previous.prox
        previous.prox = novono


# 1 5 8 9

def delete(lista, numero):
    listateste = lista.prox
    previous = None
    if (numero == 0):
        lista.prox = lista.prox.prox
        return
    for i in range(numero):
        previous = listateste
        listateste = listateste.prox
    previous.prox = listateste.prox
    listateste.prox = None


def imprimirlista(lista,x):
    imprimirlist = lista.prox
    for i in range(x):
        print("filme =", i + 1)
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
# print(arquivo.columns)
for i in range(100):
    x = random.randint(0, len(arquivo['budget']) - 1)
    inserir(arquivo, lista1, x)
deleditar = input("lanse a braba")
cont=0
if(int(deleditar) == 1):
    vrau = input("digite o numero")
    vrau2 = input("digite a categoria")
    vrau3 = input("digite o novo")
    editar(lista1, int(vrau), vrau2, vrau3)
if(int(deleditar) == 2):
    num = input("digita meu bom")
    delete(lista1, int(num))
    cont+=1



imprimirlista(lista1,100-cont)
