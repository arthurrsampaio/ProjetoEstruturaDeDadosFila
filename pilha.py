import pandas
import random

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

class top:
    def __init__(self):
        self.prox = None

def editar(pilha, antigo, novo):
    # funcao que edita o topo da pilha
    setattr(pilha.prox, antigo, novo)

def push_pilha(dado, pilha, x):
    # funcao que insere no topo da pilha
    novono = No(dado, x)
    pilhateste = pilha.prox
    if(pilha.prox!=None):
        while(pilhateste and pilhateste.id != novono.id):
            pilhateste=pilhateste.prox
    if(pilhateste and pilhateste.id==novono.id):
        return 1
    novono.prox = pilha.prox
    pilha.prox = novono

# 1 5 8 9

def pop(pilha):
    # funcao que imprime, retorna e deleta o primeiro no
    imprimirpilha(pilha, 1)
    x = pilha.prox
    aux = pilha.prox
    pilha.prox = aux.prox
    aux.prox = None
    return x

def peek(pilha):
    # funcao para visualizar o topo da pilha e retornar o primeiro elemento
    imprimirpilha(pilha, 1)
    return pilha.prox

def imprimirpilha(pilha, x):
    # funcao que imprime a pilha
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

def inicializa_pilha():
    arquivo = pandas.read_csv("tmdb_5000_movies.csv")

    pilha = top()
    contpilha = 0
    while (contpilha != 100):
        # inserir 100 filmes aleatorios
        x = random.randint(0, len(arquivo['budget']) - 1)
        if push_pilha(arquivo, pilha, x) != 1:
            contpilha += 1

    return pilha

if __name__ == "__main__":

    pilha = inicializa_pilha()

    cont = 0

    choice = input("pop=1  peek=2 editar=3 imprimir=4 sair=0 ")
    while (int(choice) != 0):
        if choice == '1':
            x = (pop(pilha))
            cont += 1
        elif choice == '2':
            y = (peek(pilha))
        elif choice == '3':
            antigo = input("digite o antigo")
            novo = input("digite o novo")
            editar(pilha, antigo, novo)
        elif choice == '4':
            imprimirpilha(pilha, 100 - cont)

        choice = input("pop=1  peek=2 editar=3 imprimir=4 sair=0 ")