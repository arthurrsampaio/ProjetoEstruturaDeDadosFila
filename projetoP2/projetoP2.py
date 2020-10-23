import csv
f=open("D:\\Documentos\\movies\\archive\\tmdb_5000_movies.csv")
leitor = csv.reader(f,delimiter =',')
i=0

for coluna in leitor:
        j=coluna

        print(j.pop())
        print(j.pop())
