from random import randint
import os
#funciones
def menu():
    os.system('cls')
    print('1) Generar lista Aleatoria')
    print('2) Generar lista Completa')
    print('3) Salir')
    opc = int(input('Ingrese opcion correcta del 1 al 3: '))
    while not(opc >= 1 and opc <= 3):
        opc = int(input('Ingrese opcion correcta del 1 al 3: '))
    return opc

def pulsarTecla():
    input('Pulse una tecla...')

#GENERA Nº ALEATORIOS
def generarLista():
    lista = []
    n = int(input('Ingrese el valor N: '))
    for i in range(n):
        x = randint(1,20)
        lista.append(x)
    return lista

#METODO DE INSERCION
def insercionSort(lista):
    #metodo de ordenamiento insercion
    for stop in range(1, len(lista)):
        key=lista[stop]
        j=stop-1
        while (j>0) and (key < lista[j]):
            lista[j+1]-lista[j]
            j =j-1
        lista[j+1]=key
    return lista

#METODO MERGE SORT
'''def mergeSort(lista_3):
    #metodo de ordenacion merge sort
    if(len(lista_3) <= 1):
        return lista_3
    else:
        medio = len(lista_3) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista_3[i])
        derecha =[]
        for i in range(medio, len(lista_3)):
            derecha.append(lista_3[i])
        izquierda=mergeSort(izquierda)
        derecha=mergeSort(derecha)
        if (izquierda[medio-1] <= derecha[0]):
            izquierda += derecha
            return izquierda
        resultado = merge(izquierda,derecha)
        return resultado'''

def merge(izquierda, derecha):
    #mezcla las listas
    lista_mezclada = []
    while(len(izquierda)>0) and (len(derecha)>0):
        if (izquierda[0]<derecha[0]):
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if(len(izquierda)>0):
        lista_mezclada += izquierda
    if(len(derecha)>0):
        lista_mezclada += derecha
    return lista_mezclada


opc = 0
while opc != 3:
    opc = menu()
    if(opc == 1):
        print('Generar lista 1: ')
        lista_1 = generarLista()
        print('La lista 1 es: ',insercionSort(lista_1))
        print('Generar lista 2: ')
        lista_2 = generarLista()
        print('La lista 2 es: ',insercionSort(lista_2))
        pulsarTecla
    elif (opc == 2): 
        print(lista_1)
        print(lista_2)  
        print('La lista completa es: ', merge(lista_1, lista_2))
        pulsarTecla()
    elif (opc ==3):
        print('Fin del programa...')
