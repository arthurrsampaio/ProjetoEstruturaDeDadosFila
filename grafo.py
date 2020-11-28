from copy import copy
class vizinhos:
    def __init__(self):
        self.dado=None
        self.peso=None
        self.prox=None
class Vertice:
    def __init__(self,vert):
        self.vert=vert
        self.vizinhos=None
        self.prox=None
class Grafo:
    def __init__(self):
        self.listavert=None

def addvert(grafo,vert):
    if(grafo.listavert==None):
        grafo.listavert=Vertice(vert)
    else:
        fk=grafo.listavert
        ant=fk
        while(fk):
            ant=fk
            fk=fk.prox
        ant.prox=Vertice(vert)

def printgf(grafo):
    fake=grafo
    while(fake.listavert):
        print(fake.listavert.vert)
        fake.listavert=fake.listavert.prox

grafo=Grafo()
addvert(grafo,1)
addvert(grafo,2)
addvert(grafo,3)
addvert(grafo,4)
printgf(grafo)
