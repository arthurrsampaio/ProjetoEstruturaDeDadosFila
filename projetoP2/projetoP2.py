import pandas
import random
arquivo = pandas.read_csv("tmdb_5000_movies.csv")
class No:
    def __init__(self, arquivo,x, prox=None):
        self.budget = arquivo['budget'][x]
        self.genres = arquivo['genres'][x]
        self.homepage = arquivo['homepage'][x]
        self.id = arquivo['id'][x]
        self.keywords=arquivo['keywords'][x]
        self.original_language=arquivo['original_language'][x]
        self.original_title=arquivo['original_title'][x]
        self.overview=arquivo['overview'][x]
        self.popularity=arquivo['popularity'][x]
        self.production_companies=arquivo['production_companies'][x]
        self.production_countries=arquivo['production_countries'][x]
        self.release_date=arquivo['release_date'][x]
        self.revenue=arquivo['revenue'][x]
        self.runtime=arquivo['runtime'][x]
        self.spoken_languages=arquivo['spoken_languages'][x]
        self.status = arquivo['status'][x]
        self.tagline = arquivo['tagline'][x]
        self.title = arquivo['title'][x]
        self.vote_average = arquivo['vote_average'][x]
        self.vote_count = arquivo['vote_count'][x]

        self.prox = prox


class Cabeca:
    def __init__(self):
        self.prox = None


def inserir(dado, lista,x):
    novono = No(dado,x)
    novono.prox = lista.prox
    lista.prox = novono


def imprimirlista(lista):
    imprimirlist = lista.prox
    for i in range(10):
        print("filme =",i)
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
        print(' ')

        imprimirlist=imprimirlist.prox

lista1=Cabeca()
#print(arquivo.columns)
for i in range(10):

    x=random.randint(0,len(arquivo['id'])-1)
    inserir(arquivo,lista1,x)

imprimirlista(lista1)






