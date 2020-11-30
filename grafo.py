import random
import pandas
import copy
arquivo=pandas.read_csv("Tweets.csv")

class Adj:
    def __init__(self,v,peso):
        self.vertice=v
        self.peso=peso
        self.prox=None

class Vertice:
    def __init__(self,arquivo,x,i):

        self.cabeca = None
        self.nvizinhos=0
        self.vertice=i
        self.tweetId=arquivo['tweet_id'][x]
        self.airline_sentiment=arquivo['airline_sentiment'][x]
        self.airline_sentiment_confidence=arquivo['airline_sentiment_confidence'][x]
        self.negativereason=arquivo['negativereason'][x]
        self.negativereason_confidence=arquivo['negativereason_confidence'][x]
        self.airline=arquivo['airline'][x]
        self.airline_sentiment_gold=arquivo['airline_sentiment_gold'][x]
        self.name=arquivo['name'][x]
        self.negativereason_gold=arquivo['negativereason_gold'][x]
        self.retweet_count=arquivo['retweet_count'][x]
        self.tweet_coord=arquivo['tweet_coord'][x]
        self.tweet_created=arquivo['tweet_created'][x]
        self.tweet_location=arquivo['tweet_location'][x]
        self.user_timezone=arquivo['user_timezone'][x]

class initD:
    def __init__(self,v):
        self.d=[]
        self.p=[]
        for i in range(100):
            self.p.append(-1)
            self.d.append(50000)
        self.d[v]=0
class Grafo:

    def __init__(self,nvert):
        self.nvert=nvert
        self.arestas=0
        self.verticies=[]

def criarvertice(grafo):
    for i in range(grafo.nvert):
        x=random.randint(0,len(arquivo))
        grafo.verticies.append(Vertice(arquivo,x,i))

def criararesta(vi,vf,grafo,peso):
    fk=grafo.verticies
    novo=Adj(vf,peso)
    grafo.verticies[vi].nvizinhos+=1
    novo.prox=grafo.verticies[vi].cabeca
    grafo.verticies[vi].cabeca=novo
    grafo.arestas+=1
def printargf(grafo):

    for i in range (grafo.nvert):
        print("vertice=",i)
        fk=grafo.verticies[i]
        fk2=grafo.verticies[i].cabeca
        
        print(fk.tweetId)
       


def relaxa(grafo,listas,u,v):
    ad=grafo.verticies[u].cabeca
    while (ad and ad.vertice!=v):
        ad=ad.prox
    if(ad):
        if(listas.d[v] > listas.d[u]+ ad.peso):
            listas.d[v] = listas.d[u]+ad.peso
            listas.p[v] = u

def dijsktra(grafo,vertice,final):
    aberto=[]
    listas=initD(vertice)
    for i in range(grafo.nvert):
        aberto.append(1)
    while(isopen(grafo,aberto)):
        u=smallerdist(grafo,aberto,listas)
        aberto[u]=0
        ad=grafo.verticies[u].cabeca
        while(ad):
            relaxa(grafo,listas,u,ad.vertice)
            ad=ad.prox
    print(listas.d[final])

def isopen(grafo,aberto):
    for i in range(grafo.nvert):
        if(aberto[i]==1):
            return 1
    return 0

def smallerdist(grafo,aberto,listas):

    for i in range(grafo.nvert):
        if(aberto[i]):
            break
    if(i==grafo.nvert):
        return -1
    menor=i
    j=menor +1
    for j in range(grafo.nvert):
        if(aberto[j] and listas.d[menor]>listas.d[i]):
            menor=i


    return menor

def buscar(grafo,id):
    for i in range(grafo.nvert):
        if(grafo.verticies[i].tweetId==int(id)):
            return i

grafo=Grafo(10)
criarvertice(grafo)
criararesta(0,1,grafo,2)
criararesta(1,4,grafo,2)
criararesta(1,3,grafo,2)
criararesta(2,3,grafo,2)
criararesta(3,4,grafo,2)
criararesta(4,5,grafo,2)
criararesta(5,6,grafo,2)
criararesta(6,7,grafo,2)
criararesta(7,8,grafo,2)
criararesta(8,2,grafo,2)
criararesta(8,9,grafo,2)
criararesta(9,8,grafo,2)
deleditar=input("1=print,2=djiktra,0=sair: ")

while(int(deleditar)!=0):
    if(int(deleditar)==1):
        printargf(grafo)
    if(int(deleditar)==2):

        dijsktra(grafo,buscar(grafo,input("coloque o id")),buscar(grafo,input("destino")))
    deleditar=input("1=print,2=djiktra,0=sair: ")

