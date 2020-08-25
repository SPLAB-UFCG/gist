#coding utf-8
#Codigo dedicado á execução de um simples BubbleSort  de uma lista em arquivo
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if(lista[j] > lista [j +1]):
                lista[j],lista[j+1] =  lista[j+1],lista[j]


path  =  input('Path do arquivo: ')
arquivo =  open( path , "r")
lista = arquivo.read().splitlines()
arquivo.close() 
bubble_sort(lista)
with open ('Result.txt', "w")as file:
    for word in lista:
        file.write("%s\n" % word)
