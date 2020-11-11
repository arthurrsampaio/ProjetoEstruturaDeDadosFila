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

        self.left = None
        self.right = None


def deletar(arvore,id):
    previous=buscarprev(arvore,id)

def editar(arvore, antigo, novo,id):
    nozinho=(buscar(arvore,id))
    setattr(nozinho, antigo, novo)

def editar2(arvore2, antigo, novo,popularity):
    nozinho=(buscar2(arvore2,popularity))
    setattr(nozinho, antigo, novo)


def editar3(arvore3, antigo, novo,vote):
    nozinho=(buscar3(arvore3,vote))
    setattr(nozinho, antigo, novo)

def buscar(arvore,id):

    while(arvore):
        if int(arvore.id)==int(id):

            return arvore
        if int(arvore.id)>int(id) and arvore.id!=id:
            prev=arvore
            arvore=arvore.left
        elif int(arvore.id)!=id:
            prev=arvore
            arvore=arvore.right
def buscarprev(arvore,id,prev):

    while(arvore):
        if int(arvore.id)==int(id):

            return prev
        if int(arvore.id)>int(id) and arvore.id!=id:
            prev=arvore
            arvore=arvore.left
        elif int(arvore.id)!=id:
            prev=arvore
            arvore=arvore.right

def buscar2(arvore2,popularity):

    while(arvore2):
        if float(arvore2.popularity)==float(popularity):

            return arvore2
        if float(arvore2.popularity)>float(popularity) and arvore2.popularity!=popularity:
            arvore2=arvore2.left
        elif float(arvore2.popularity)!=popularity:

            arvore2=arvore2.right

def buscar3(arvore3,vote):

    while(arvore3):
        if int(arvore3.vote_count)==int(vote):

            return arvore3
        if int(arvore3.vote_count)>int(vote) and arvore3.vote_count!=vote:
            arvore3=arvore3.left
        elif int(arvore3.vote_count)!=vote:

            arvore3=arvore3.right
def printarvore(arvore):

    if(arvore!=None):
        printarvore(arvore.left)
        """  print(arvore.budget)
        print(arvore.genres)
        print(arvore.homepage)"""
        print("id=")
        print(arvore.id)
        """ print(arvore.keywords)
        print(arvore.original_language)
        print(arvore.original_title)
        print(arvore.overview)"""
        print("popularity=")
        print(arvore.popularity)
        """
        print(arvore.production_companies)
        print(arvore.production_countries)
        print(arvore.release_date)
        print(arvore.revenue)
        print(arvore.runtime)
        print(arvore.spoken_languages)
        print(arvore.status)
        print(arvore.tagline)
        print(arvore.title)
        print(arvore.vote_average)"""
        print("vote count=")
        print(arvore.vote_count)
        print(' ')

        printarvore(arvore.right)
def contarno(arvore):
    if(arvore==None):
        return 0
    else:
        conte = contarno(arvore.left);
        contd = contarno(arvore.right);
    return conte + contd + 1;
def inserir(arvore, arquivo, x):

    novono = No(arquivo, x)

    if(arvore==None):
        return novono
    if(novono.id<arvore.id and arvore.id != novono.id):
        arvore.left=inserir(arvore.left,arquivo,x)
    elif arvore.id != novono.id :
        arvore.right = inserir(arvore.right, arquivo, x)

    return (arvore)


def inserir2(arvore2, arquivo, x):

    novono = No(arquivo, x)
    if(arvore2==None):
        return novono
    if(novono.popularity<arvore2.popularity and arvore2.popularity != novono.popularity):
        arvore2.left=inserir2(arvore2.left,arquivo,x)
    elif arvore2.id != novono.id and arvore2.popularity!=novono.popularity:
        arvore2.right = inserir2(arvore2.right, arquivo, x)
    return (arvore2)

def inserir3(arvore3, arquivo, x):
    novono = No(arquivo, x)
    if (arvore3 == None):
        return novono
    if (novono.vote_count < arvore3.vote_count and arvore3.vote_count != novono.vote_count):
        arvore3.left = inserir3(arvore3.left, arquivo, x)
    elif arvore3.id != novono.id and arvore3.vote_count != novono.vote_count:
        arvore3.right = inserir3(arvore3.right, arquivo, x)
    return (arvore3)

def removeno (arvore,id):
    pai=None
    p=None
    atual=arvore
    q=None
    while(atual and int(atual.id) != int(id)):
        pai=atual
        if(int(atual.id)>int(id)):
            atual=atual.left
        else:
            atual = atual.right
    ata=atual.id
    if (atual == None):
        return arvore

    if(atual.left ==None or atual.right==None):
        print ("caiu")
        if(not atual.left):
            q=atual.right
        else:
            q=atual.left



    else:
        p=atual
        q=atual.left
        while(q.right):
            p=q
            q=q.right


        if(p!=atual):
            p.right = q.left
            q.left = atual.left
        q=atual.right

    if (not pai):
        atual.right=None
        atual.left=None
        return (q)

    if(int(id) < int(pai.id)):
        pai.left=q
    else:
        pai.right=q

    atual.right=None
    atual.left=None
    return arvore
def removeno2 (arvore,popularity):
    pai=None
    p=None
    atual=arvore
    q=None
    while(atual and float(atual.popularity) != float(popularity)):
        pai=atual
        if(float(atual.popularity)>float(popularity)):
            atual=atual.left
        else:
            atual = atual.right

    if (atual == None):
        return arvore

    if(atual.left ==None or atual.right==None):
        print ("caiu")
        if(not atual.left):
            q=atual.right
        else:
            q=atual.left



    else:
        p=atual
        q=atual.left
        while(q.right):
            p=q
            q=q.right


        if(p!=atual):
            p.right = q.left
            q.left = atual.left
        q=atual.right

    if (not pai):
        atual.right=None
        atual.left=None
        return (q)

    if(float(popularity) < float(pai.popularity)):
        pai.left=q
    else:
        pai.right=q

    atual.right=None
    atual.left=None
    return arvore

def removeno3 (arvore,vote_count):
    pai=None
    p=None
    atual=arvore
    q=None
    while(atual and int(atual.vote_count) != int(vote_count)):
        pai=atual
        if(int(atual.vote_count)>int(vote_count)):
            atual=atual.left
        else:
            atual = atual.right

    if (atual == None):
        return arvore

    if(atual.left ==None or atual.right==None):
        
        if(not atual.left):
            q=atual.right
        else:
            q=atual.left



    else:
        p=atual
        q=atual.left
        while(q.right):
            p=q
            q=q.right


        if(p!=atual):
            p.right = q.left
            q.left = atual.left
        q=atual.right

    if (not pai):
        atual.right=None
        atual.left=None
        return (q)

    if(int(vote_count) < int(pai.vote_count)):
        pai.left=q
    else:
        pai.right=q

    atual.right=None
    atual.left=None
    return arvore
arvore = None
arvore2 = None
arvore3 = None

while (contarno(arvore)!=100):
    # inserir 100 filmes aleatorios
    x = random.randint(0, len(arquivo['budget']) - 1)
    arvore = inserir(arvore,arquivo, x)

while (contarno(arvore2)!=100):
    x = random.randint(0, len(arquivo['budget']) - 1)
    arvore2 = inserir2(arvore2, arquivo, x)

while (contarno(arvore3)!=100):
    x = random.randint(0, len(arquivo['budget']) - 1)
    arvore3 = inserir3(arvore3, arquivo, x)

choice = input("escolha a arvore")
if(choice=='1'):

    choice = input("imprimir=1  editar=2  sair=0 ")
    while (int(choice) != 0):
        if choice == '1':
            printarvore(arvore)
        if choice == '2':
            categoria = input("digite o categoria")
            novo = input("digite a nova informação")
            ide=input("digite a ser substituido")
            editar(arvore,categoria,novo,ide)
        if choice == '3':
            removeno(arvore,input("digite o id"))
        if choice == '4':
            pass

        choice = input("pop=1  peek=2 editar=3 imprimir=4 sair=0 ")

if(choice=='2'):
    choice = input("imprimir=1  editar=2 editar=3 imprimir=4 sair=0 ")
    while (int(choice) != 0):
        if choice == '1':
            printarvore(arvore2)
        if choice == '2':
            categoria = input("digite o categoria")
            novo = input("digite a nova informação")
            budget = input("digite a ser substituido")
            editar2(arvore2, categoria, novo, budget)
        if choice == '3':
            print("foi")
            removeno2(arvore2,input("digite o populairty"))
        if choice == '4':
            pass

        choice = input("pop=1  peek=2 editar=3 imprimir=4 sair=0 ")

if(choice=='3'):
    choice = input("imprimir=1  editar=2 editar=3 imprimir=4 sair=0 ")
    while (int(choice) != 0):
        if choice == '1':
            printarvore(arvore3)
        if choice == '2':
            categoria = input("digite o categoria")
            novo = input("digite a nova informação")
            ide = input("digite a ser substituido")
            editar3(arvore3, categoria, novo, ide)
        if choice == '3':
            removeno3(arvore3,input("digite o vote_count"))
        if choice == '4':
            pass

        choice = input("pop=1  peek=2 editar=3 imprimir=4 sair=0 ")
