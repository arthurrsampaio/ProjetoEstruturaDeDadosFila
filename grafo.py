class Adj:
    def __init__(self,v,peso):
        self.vertice=v
        self.peso=peso
        self.prox=None

class Vertice:
    def __init__(self):
        self.cabeca = None
        self.nvizinhos=0
        self.dado=None

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
        grafo.verticies.append(Vertice())

def criararesta(vi,vf,grafo,peso):
    novo=Adj(vf,peso)
    grafo.verticies[vi].nvizinhos+=1
    novo.prox=grafo.verticies[vi].cabeca
    grafo.verticies[vi].cabeca=novo
    grafo.arestas+=1
def printargf(grafo):

    for i in range (5):
        print("vertice=",i)
        j=i
        fk=grafo.verticies
        for i in range(fk[j].nvizinhos):
            print(fk[j].cabeca.vertice)
            fk[j].cabeca=fk[j].cabeca.prox
def relaxa(grafo,u,v):
    listas=initD(u)
    ad=grafo.verticies[u].cabeca
    while (ad and ad.vertice!=v):
        ad=ad.prox
    if(ad):
        if(listas.d[v] > listas.d[u]+ ad.peso):
            listas.d[v] = listas.d[u]+ad.peso
            listas.p[v] = u

def dijsktra(grafo,s):
    aberto=[]
    for i in range


grafo=Grafo(100)
criarvertice(grafo)
criararesta(0,1,grafo,1)
criararesta(0,2,grafo,1)
criararesta(0,3,grafo,1)
criararesta(1,4,grafo,1)
criararesta(1,5,grafo,1)
criararesta(1,6,grafo,1)
criararesta(2,7,grafo,1)
relaxa(grafo,0,1)
