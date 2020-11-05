import pandas
import random

arquivo = pandas.read_csv("tmdb_5000_movies.csv")


class No:
    def __init__(self, arquivo, x):
        # criando um no
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


class queue:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0

def push(fila,arquivo,x):
    new_node= No(arquivo,x)
    if(fila.inicio == None):
        fila.inicio = new_node
        fila.final = new_node
        return 1
    filafalsa = fila.inicio
    while (filafalsa and filafalsa.id != new_node.id):
        filafalsa=filafalsa.prox
    if(filafalsa==None):
        fila.final.prox=new_node
        fila.final=new_node
        return 1
    else:
        return 0



def popid (fila):
    printqueue(fila,1)
    aux=fila.inicio
    fila.inicio = fila.inicio.prox
    aux.prox=None
    return aux

def printqueue(fila,x):
    printafila = fila.inicio
    for i in range(x):
        print("filme =", i + 1)
        print(printafila.budget)
        print(printafila.genres)
        print(printafila.homepage)
        print(printafila.id)
        print(printafila.keywords)
        print(printafila.original_language)
        print(printafila.original_title)
        print(printafila.overview)
        print(printafila.popularity)
        print(printafila.production_companies)
        print(printafila.production_countries)
        print(printafila.release_date)
        print(printafila.revenue)
        print(printafila.runtime)
        print(printafila.spoken_languages)
        print(printafila.status)
        print(printafila.tagline)
        print(printafila.title)
        print(printafila.vote_average)
        print(printafila.vote_count)
        print(' ')

        printafila = printafila.prox
fila = queue()
contfila = 0
while (fila.tamanho != 100):
    # inserir 100 filmes aleatorios
    x = random.randint(0, len(arquivo['budget']) - 1)
    if(push(fila,arquivo,x)):

        fila.tamanho+=1

def editar(fila, antigo, novo):
    # funcao que edita o topo da pilha
    setattr(fila.inicio, antigo, novo)


choice = input("pop=1  editar=2 imprimir=3 sair=0 ")
while (int(choice) != 0):
    if choice == '1':
        j=popid(fila)
    if choice == '2':
        antigo = input("digite o antigo")
        novo = input("digite o novo")
        editar(fila,antigo,novo)
    if choice == '3':
        printqueue(fila,100)

    choice = input("pop=1  editar=2 imprimir=3 sair=0 ")
