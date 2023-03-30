import os
from random import randint


def menu():
    os.system('cls')
    print('1) Cargar lista en forma aleatoria')
    print('2) Mostrar los valores generados')
    print('3) Mostrar los primeros M valores de la lista')
    print('4) Mostrar los valores pares y la suma de estos')
    print('5) Buscar un número dado y mostrar su posición')
    print('6) Verificar si la lista se encuentra ordenado en forma descendente')        
    print('7) Fin')
    opcion = int(input('Ingrese una opción: '))
    while not(opcion >= 1 and opcion <= 7): 
        opcion = int(input('Ingrese una opción: '))
    return opcion    

def pulsarTecla():
    input('Pulse un tecla...')    

def buscar(lista, k):
    pos = -1 # al inico, supongo que no existe
    for (i,item) in enumerate(lista):
        if(item == k):
            pos = i+1
            break  # rompe la iteración de for 
    return pos        

def leerLista():
    lista = []
    n = int(input('Ingrese N: '))
    for i in range(n):  # range(a, b+1)
        x = randint(1,10)#me permite generar numeros del 1 al 10
        lista.append(x)
    return lista    

def mostrarMValores(lista):
    m = int(input('Ingrese los primeros M valores:'))
    if m <= len(lista):
        for i in range(m):
            print(lista[i])
    else:
        print('La Poscicion: ',m ,' no existe!!!')        
    pulsarTecla()

def MostrarPares(lista):
    sumaPar = 0
    for (i, item) in enumerate(lista):
        if(item%2 == 0):
            print(item)
            sumaPar += item
            pulsarTecla()
    return  sumaPar     

def mostrarPosicion(lista):
    numero = int(input('Ingrese numero a buscar: '))
    posicion = buscar(lista,numero)
    if posicion != -1:
        print('El numero: ',numero, ' se encuentra en la posicion: ',posicion)
    else:
        print('El numero ingresado no se encuentra en la lista')    
    pulsarTecla()

def ordenDescendente(lista):
    orden=True
    for i in range(len(lista)-1):
        if lista[i]<lista[i+1]:
            orden = False
            break        
    return(orden)

def informarOrden(lista):
    if ordenDescendente(lista):
        print('La Lista esta ordenada en forma descendente')
        print (lista)  
    else:
        print('La Lista no esta ordenada en forma descendente')     

#Principal
opcion = 0
#lista = []
while opcion != 7:
    opcion = menu()
    if opcion == 1: 
        lista = leerLista()
    elif opcion == 2: 
        print(lista) 
        pulsarTecla()    
    elif opcion == 3: 
        mostrarMValores(lista)
    elif opcion == 4: 
        print('Suma de valores Pares:',MostrarPares(lista))       
        pulsarTecla() 
    elif opcion == 5: 
        mostrarPosicion(lista)   
    elif opcion == 6: 
        informarOrden(lista)
        pulsarTecla()
    elif opcion == 7: 
        print('Fin del programa')