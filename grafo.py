import random
import pandas

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
    for i in range(100):
        x=random.randint(0,len(arquivo))
        grafo.verticies.append(Vertice(arquivo,x,i))

def criararesta(vi,vf,grafo,peso):
    novo=Adj(vf,peso)
    grafo.verticies[vi].nvizinhos+=1
    novo.prox=grafo.verticies[vi].cabeca
    grafo.verticies[vi].cabeca=novo
    grafo.arestas+=1
def printargf(grafo):

    for i in range (100):
        print("vertice=",i)
        j=i
        fk=grafo.verticies
        print(grafo.verticies[i].tweetId)

def relaxa(grafo,listas,u,v):
    ad=grafo.verticies[u].cabeca
    while (ad and ad.vertice!=v):
        ad=ad.prox
    if(ad):
        if(listas.d[v] > listas.d[u]+ ad.peso):
            listas.d[v] = listas.d[u]+ad.peso
            listas.p[v] = u

def dijsktra(grafo,vertice):
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
    for i in range(grafo.nvert):
        print(listas.d[i])
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


grafo=Grafo(10)
criarvertice(grafo)
for i in range(100000):
    peso=int(float(grafo.verticies[i%].airline_sentiment_confidence) * 10)
    conecta=str(grafo.verticies[i%10].tweetId)
    if(i!=9):
        j=i+1
    else:
        j=8
    criararesta(i%10,int(conecta[-2:]),grafo,peso)


dijsktra(grafo,0)
#printargf(grafo)
