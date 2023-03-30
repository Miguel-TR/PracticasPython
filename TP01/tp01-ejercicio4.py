
#d. Ingrese un número entero denominado objetivo y determine la cantidad de pares de elementos
#del vector que tienen una diferencia igual al valor objetivo.

import os
from random import randint

def menu():
    os.system('cls')
    print('1) Cargar lista en forma aleatoria')
    print('2) Mostrar los valores generados')
    print('3) Modificar todos los números que sean múltiplos de 3')
    print('4) Mostrar pares de elementos que tienen una diferencia igual al valor objetivo')
    print('5) Fin')
    opcion = int(input('Ingrese una opción: '))
    while not(opcion >= 1 and opcion <= 5): 
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

def primo(k):
    primo=True #inicializacion de la variable logica, que me permitirá saber si el nro tiene divisibles 
    for i in range(2,(k//2+1)): #busca los multiplos de nro entre 2 y la mitad del nro ---While primo and n>=2 y n<=nro/2
        if (k%i==0):
            primo=False #actualizacion de la variable logica, cuando encuentra algun multiplo de nro osea resto 0
                        #print(i)# verificar el break
            break
    return primo

def leerLista():
    lista = []
    for i in range(30):
        #print(i)
        #input('tecla...')
        x = randint(1,50)
        while buscar(lista,x)!=-1 or primo(x):
            x = randint(1,50)
        lista.append(x)
    return lista    

def divisible(k):
    divisible=False #inicializacion de la variable logica, que me permitirá saber si el nro tiene divisibles 
    if (k%3==0):
        divisible=True 
    return divisible

def modificarDiv3(lista):
    for (i, item) in enumerate(lista):
        if divisible(item):
            #x = randint(1,50)
            #while divisible(x):
                #x = randint(1,50)
            lista[i]=lista[i]*lista[i]
    pulsarTecla()
    return(lista)        

def mostrarPosicion(lista):
    numero = int(input('Ingrese numero a buscar: '))
    posicion = buscar(lista,numero)
    if posicion != -1:
        print('El numero: ',numero, ' se encuentra en la posicion: ',posicion)
    else:
        print('El numero ingresado no se encuentra en la lista')    
    pulsarTecla()

def diferencia(lista):
    c=0
    numero = int(input('Ingrese numero objetivo: '))
    for i in range(len(lista)-1):
        if abs(lista[i]-lista[i+1])==numero:
            print(lista[i],' - ',lista[i+1])
            c+=1
    return(c)


#Principal
opcion = 0
#lista = []
while opcion != 5:
    opcion = menu()
    if opcion == 1: 
        lista = leerLista()
    elif opcion == 2: 
        print(lista) 
        pulsarTecla()    
    elif opcion == 3: 
        lista = modificarDiv3(lista)
    elif opcion == 4: 
        print('la cantidad de pares con diferencia objetivo: ',diferencia(lista))   
        pulsarTecla()   
    elif opcion == 5: 
        print('Fin del programa')    