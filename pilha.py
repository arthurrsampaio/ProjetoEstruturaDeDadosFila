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


class top:
    def __init__(self):
        self.prox = None


def editar(pilha, antigo, novo):

    setattr(pilha.prox, antigo, novo)


def push(dado, pilha, x):
    novono = No(dado, x)
    novono.prox = pilha.prox
    pilha.prox = novono


# 1 5 8 9

def pop(pilha):
    imprimirpilha(pilha, 1)
    aux=pilha.prox
    pilha.prox=aux.prox
    aux.prox=None


def peek(pilha):
    imprimirpilha(pilha,1)

def imprimirpilha(pilha,x):
    imprimirpilha = pilha.prox
    for i in range(x):
        print("filme =", i + 1)
        print(imprimirpilha.budget)
        print(imprimirpilha.genres)
        print(imprimirpilha.homepage)
        print(imprimirpilha.id)
        print(imprimirpilha.keywords)
        print(imprimirpilha.original_language)
        print(imprimirpilha.original_title)
        print(imprimirpilha.overview)
        print(imprimirpilha.popularity)
        print(imprimirpilha.production_companies)
        print(imprimirpilha.production_countries)
        print(imprimirpilha.release_date)
        print(imprimirpilha.revenue)
        print(imprimirpilha.runtime)
        print(imprimirpilha.spoken_languages)
        print(imprimirpilha.status)
        print(imprimirpilha.tagline)
        print(imprimirpilha.title)
        print(imprimirpilha.vote_average)
        print(imprimirpilha.vote_count)
        print(' ')

        imprimirpilha = imprimirpilha.prox


pilha = top()

for i in range(100):
    x = random.randint(0, len(arquivo['budget']) - 1)
    push(arquivo, pilha, x)
choice=input("pop=1  peek=2 editar=3 imprimir=01 ")
if choice=='1':
    print(pop(pilha))
if choice == '2':
    print(peek(pilha))
if choice == '3':
    antigo=input("digite o antigo")
    novo=input("digite o antigo")
    editar(pilha,antigo,novo)

if choice == '0':
    imprimirpilha(pilha, 100)

