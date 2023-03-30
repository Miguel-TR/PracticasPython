import os
from random import randint

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
        x = randint(1,20)
        lista.append(x)
    return lista    

def mostrarLista(lista):
    for i in lista: 
        print(i)
    input('Presione una tecla para continuar...')    

def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print(lst)
    return lst

def insertionSort(lst):
    for step in range(1, len(lst)):
        key = lst[step]
        j = step - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key
        print(lst)
    return lst

def selectionSort(lst):
    n = len(lst)
    for step in range(n):
        j = step
        for i in range(step + 1, n):
            if lst[i] < lst[j]:
                j = i
        lst[step], lst[j] = lst[j], lst[step]
        print(lst)
    return lst    

os.system('cls')   
lista=leerLista()
listaIns=lista.copy()
listaSel=lista.copy()
mostrarLista(lista)
bubbleSort(lista)
mostrarLista(lista)
mostrarLista(listaIns)
insertionSort(listaIns)
mostrarLista(listaIns)
mostrarLista(listaSel)
selectionSort(listaSel)
mostrarLista(listaSel)

def shellSort(lst):
    n = len(lst)
    gap = n // 2 # … 112,48,21,7,5,1
    while gap > 0: #
        for i in range(gap, n):
            tmp = lst[i]
            j = i
            while j >= gap and lst[j - gap][0] > tmp[0]: # < desc > asc 
                lst[j] = lst[j - gap] #podria ir un print(list) para mostrar los cambios de la lista
                j -= gap
            lst[j] = tmp
        gap = gap // 2
    return lst

def quicksort(lst, start, stop): #https://www.youtube.com/watch?v=YzHDIvxOQcI
    if stop - start > 0:
        pivot, left, right = lst[start][3], start, stop
        while left <= right:
            while lst[left][3] < pivot: #estos dos se cambiaria para cambiar de orden descendente < asc   > desc
                left += 1
            while lst[right][3]> pivot: # este es el contrario al anterior
                right -= 1
            if left <= right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        quicksort(lst, start, right)
        quicksort(lst, left, stop)
    return lst

def mergeSortAuto(myList): #https://www.educative.io/answers/merge-sort-in-python
    if len(myList) > 1:
        mid = len(myList) // 2 #estas lineas se divide y luego ordena
        left = myList[:mid]
        right = myList[mid:]

        # Llamada recursiva en cada mitad
        mergeSortAuto(left)
        mergeSortAuto(right)

        # Dos iteradores para atravesar las dos mitades
        i = 0
        j = 0
        
        # Iterador para la lista principal
        k = 0
        #aqui comienza la mezcla merge
        while i < len(left) and j < len(right):
            if left[i][4] <= right[j][4]:# aqui se cambia para un valor descendente
              # Se ha utilizado el valor de la mitad izquierda.
              myList[k] = left[i]
              # Mover el iterador hacia adelante
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Mover a la siguiente elemento
            k += 1

        # Para todos los valores restantes
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

def mergeSort(myList): #https://www.educative.io/answers/merge-sort-in-python
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Llamada recursiva en cada mitad
        mergeSort(left)
        mergeSort(right)

        # Dos iteradores para atravesar las dos mitades
        i = 0
        j = 0
        
        # Iterador para la lista principal
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # Se ha utilizado el valor de la mitad izquierda.
              myList[k] = left[i]
              # Mover el iterador hacia adelante
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Mover a la siguiente elemento
            k += 1

        # Para todos los valores restantes
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

            
shellSort(automovil)#dominio
print(automovil)
quicksort(automovil, 0, len(automovil)-1)#modelo
print(automovil)
myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)