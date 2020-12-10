import random
import pandas
import copy

arquivo = pandas.read_csv("Tweets.csv")


class Adj:
    def __init__(self, v, peso):
        self.vertice = v
        self.peso = peso
        self.prox = None


class Vertice:
    def __init__(self, arquivo, x, i):
        self.cabeca = None
        self.nvizinhos = 0
        self.vertice = i
        self.tweetId = arquivo['tweet_id'][x]
        self.airline_sentiment = arquivo['airline_sentiment'][x]
        self.airline_sentiment_confidence = arquivo['airline_sentiment_confidence'][x]
        self.negativereason = arquivo['negativereason'][x]
        self.negativereason_confidence = arquivo['negativereason_confidence'][x]
        self.airline = arquivo['airline'][x]
        self.airline_sentiment_gold = arquivo['airline_sentiment_gold'][x]
        self.name = arquivo['name'][x]
        self.negativereason_gold = arquivo['negativereason_gold'][x]
        self.retweet_count = arquivo['retweet_count'][x]
        self.tweet_coord = arquivo['tweet_coord'][x]
        self.tweet_created = arquivo['tweet_created'][x]
        self.tweet_location = arquivo['tweet_location'][x]
        self.user_timezone = arquivo['user_timezone'][x]


class initD:
    def __init__(self, v):
        self.d = []
        self.p = []
        for i in range(100):
            self.p.append(-1)
            self.d.append(50000)
        self.d[v] = 0


class Grafo:

    def __init__(self, nvert):
        self.nvert = nvert
        self.arestas = 0
        self.verticies = []


def criarvertice(grafo):
    for i in range(grafo.nvert):
        x = random.randint(0, len(arquivo))
        grafo.verticies.append(Vertice(arquivo, x, i))


def criararesta(vi, vf, grafo, peso):
    fk = grafo.verticies
    novo = Adj(vf, peso)
    grafo.verticies[vi].nvizinhos += 1
    novo.prox = grafo.verticies[vi].cabeca
    grafo.verticies[vi].cabeca = novo
    grafo.arestas += 1


def printargf(grafo):
    for i in range(grafo.nvert):
        print("vertice=", i)
        fk = grafo.verticies[i]
        fk2 = grafo.verticies[i].cabeca
        while(fk2):
            print(fk2.vertice)
            fk2=fk2.prox
        print(fk.tweetId)


def relaxa(grafo, listas, u, v):
    ad = grafo.verticies[u].cabeca
    while (ad and ad.vertice != v):
        ad = ad.prox
    if (ad):
        if (listas.d[v] > listas.d[u] + ad.peso):
            listas.d[v] = listas.d[u] + ad.peso
            listas.p[v] = u


def caminho(grafo, inicial, final, listas):
    newlist = []
    i = final
    j=0
    while (i != inicial and j<10):
        j+=1
        newlist.append(i)
        i = listas.p[i]
    if(j<10):

        newlist.append(inicial)
        newlist.reverse()

        print(newlist)


def dijsktra(grafo, vertice, final):
    aberto = []
    listas = initD(vertice)
    for i in range(grafo.nvert):
        aberto.append(1)
    while (isopen(grafo, aberto)):
        u = smallerdist(grafo, aberto, listas)
        aberto[u] = 0
        ad = grafo.verticies[u].cabeca
        while (ad):
            relaxa(grafo, listas, u, ad.vertice)
            ad = ad.prox
    if(int(listas.d[final])!=50000):
        print(listas.d[final])
        caminho(grafo, vertice, final, listas)
    else:
       print("nao tem")



def isopen(grafo, aberto):
    for i in range(grafo.nvert):
        if (aberto[i] == 1):
            return 1
    return 0


def smallerdist(grafo, aberto, listas):
    for i in range(grafo.nvert):
        if (aberto[i]):
            break
    if (i == grafo.nvert):
        return -1
    menor = i
    j = menor + 1
    for j in range(grafo.nvert):
        if (aberto[j] and listas.d[menor] > listas.d[j]):
            menor = j

    return menor


def buscar(grafo, id):
    for i in range(grafo.nvert):
        if (grafo.verticies[i].tweetId == int(id)):
            return i


grafo = Grafo(10)
criarvertice(grafo)

for i in range(10):
    x=random.randint(0, 3)
    y= random.randint(4, 6)
    z=random.randint(7, 9)
    while(x==i or y==i or z==i):
        x = random.randint(0, 3)
        y = random.randint(4, 6)
        z = random.randint(7, 9)
    criararesta(i, x, grafo, int(grafo.verticies[i].airline_sentiment_confidence *10))
    criararesta(i, y, grafo, int(grafo.verticies[i].airline_sentiment_confidence*10))
    criararesta(i, z, grafo, int(grafo.verticies[i].airline_sentiment_confidence*10))

deleditar = input("1=print,2=djiktra,0=sair: ")

while (int(deleditar) != 0):
    if (int(deleditar) == 1):
        printargf(grafo)
    if (int(deleditar) == 2):
        dijsktra(grafo, buscar(grafo, input("coloque o id: ")), buscar(grafo, input("destino: ")))
    deleditar = input("1=print,2=djiktra,0=sair: ")
