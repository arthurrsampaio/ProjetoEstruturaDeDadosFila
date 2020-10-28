import pandas
import random

arquivo = pandas.read_csv("tmdb_5000_movies.csv")


class No:
    def __init__(self, arquivo, x):
        #criando no definindo suas variaveis 
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
    #funcao que edita um no recebendo sua posicao e o atributo antigo e novo
    listateste = lista.prox
    for i in range(numero):
        listateste = listateste.prox

    setattr(listateste, antigo, novo)


def inserir(dado, lista, x):
    #funcao que insere o no de maneira ordenada baseado na media de votos
    novono = No(dado, x)
    if lista.prox is None:
        lista.prox = novono
        return

    atual = lista.prox
    previous = None

    while atual and atual.vote_average <= novono.vote_average:
        previous = atual
        atual = atual.prox
    if previous is None:
        novono.prox = lista.prox
        lista.prox = novono
    else:

        novono.prox = previous.prox
        previous.prox = novono



def delete(lista, numero):
    #funcao para deletar um no da lista que recebe sua posição
    listateste = lista.prox
    previous = None
    if(numero == 0):
        lista.prox = lista.prox.prox
        return
    for i in range(numero):
        previous = listateste
        listateste = listateste.prox
    previous.prox = listateste.prox
    listateste.prox = None


def imprimirlista(lista,x):
    #funcaoqueimprimealista
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

for i in range(100):
    #inserir 100 filmes aleatorios
    x = random.randint(0, len(arquivo['budget']) - 1)
    inserir(arquivo, lista1, x)
    
deleditar = input("Digite sua opção(0 = Imprimir, 1 = Editar, 2 = Deletar) ")
cont = 0
while int(deleditar) != 0:
    if int(deleditar) == 1:
        num = input("Digite o número: ")
        cat = input("Digite a Categoria: ")
        new = input("Digite o Novo: ")
        editar(lista1, int(num), cat, new)
        deleditar = input("Digite sua opção(0 = Imprimir, 1 = Editar, 2 = Deletar) ")
        
    if int(deleditar) == 2:
        num = input("Digite o número que deseja deletar: ")
        delete(lista1, int(num))
        cont += 1
        deleditar = input("Digite sua opção(0 = Imprimir, 1 = Editar, 2 = Deletar) ")


imprimirlista(lista1, 100-cont)
