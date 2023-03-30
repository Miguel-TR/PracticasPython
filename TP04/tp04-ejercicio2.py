"""Mostrar los pasos del ordenamiento de la lista: 6, 0, 3, 2, 5, 7, 4, 1 con los métodos de inserción y con
merge sort. ¿Cuáles son las principales diferencias entre los métodos? ¿Cuál usarías en qué casos?.
Utilice lápiz y papel para resolver el ejercicio."""

def presionarTecla():
   input('Presione una tecla...')

def merge(lista1, lista2):
    i=0 #lista1
    j=0 #lista2
    #k=-1 #lista
    lista=[]
    while i<len(lista1) and j<len(lista2):
        if lista1[i] < lista2[j]:
            #k+=1
            lista.append(lista1[i])
            i+=1
        else:
            lista.append(lista2[j])
            j+=1
    if i<len(lista1):
        for k in range(i,len(lista1)):
           lista.append(lista1[k]) 
    if j<len(lista2):
        for k in range(j,len(lista2)):
           lista.append(lista2[k]) 
    return lista

lista = [6, 0, 3, 2, 5, 7, 4, 1]
