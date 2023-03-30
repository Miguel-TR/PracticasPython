import os
from random import randint

def validaDominio():
    d = input('Ingrese Dominio:')
    while not(len(d)>=6 and len(d)<=9):
        d = input('Ingrese Dominio:')
    return d         
def validaMarca():
    marca= input('Ingrese Marca:').upper
    while not(marca in ['F','R','C']):
        marca = input('Ingrese Marca:')
    if marca=='F':
        marca='Ford'
    elif marca=='R' :
        marca='Renault'      
    elif marca=='C' :
        marca='Citroen'       
    return marca

def validaEstado():
    estado= input('Ingrese estado:').upper
    while not(estado in ['V','R','D','']):
        estado = input('Ingrese estado:')
    if estado=='V':
        estado='Vendido'
    elif estado=='R' :
        estado='Reservado'      
    elif estado=='D' :
        estado='Disponible'     
    elif estado=='' :
        estado='Disponible'        
    return estado    

def leerAutomoviles(automovil):
    print('Cargar Lista de Automoviles')
    automovil = [['AB101ED', 'Renault', 'Automovil', 2019, 20000, 250000, 275000, 'D'],
                 ['AC245EV', 'Ford', 'Utilitario', 2021, 80000, 150000, 175000,'D'],
                 ['AA110ED', 'Citroen', 'Automovil', 2018, 10000, 350000, 400000, 'D'],
                 ['AE205EV', 'Ford', 'Utilitario', 2006, 70000, 150000, 178000,'D'],
                 ['AB102ED', 'Renault', 'Automovil', 2019, 24000, 250000, 277000, 'D'],
                 ['AC100EV', 'Ford', 'Utilitario', 2014, 82000, 150000, 176000,'D'],
                 ['AA102ED', 'Citroen', 'Automovil', 2017, 21000, 350000, 401000, 'D'],
                 ['AE206EV', 'Ford', 'Utilitario', 2010, 81000, 150000, 172000,'D'],
                 ['AE300EV', 'Renault', 'Utilitario', 2000, 87000, 150000, 170000,'D'],
                 ['AE033EV', 'Citroen', 'Automovil', 2017, 23000, 150000, 140000,'D']
                ]
    # continuar = 's'
    # while (continuar=='s')
    #     dominio=validaDominio()
    #     marca=validaMarca()
    #     estado=validaEstado()
    #     pve=pval*1.10
    #     automovil.append([dominio, marca, tipo, modelo, km, pva, pve,estado])
    return automovil    
   

def bubbleSort(automovil):
    n = len(automovil)
    for i in range(n):
        for j in range(0, n-1):
            if automovil[j][1] > automovil[j+1][1]: #comparan el criterio a ordenar
                automovil[j], automovil[j+1] = automovil[j+1], automovil[j]
    return automovil

def insertionSort(lst):
    for step in range(1, len(lst)):
        key = lst[step]
        j = step - 1
        while j >= 0 and key[6] < lst[j][6]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key
    return lst    

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
        mid = len(myList) // 2
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

def buscarPorDominio(automovil,dominio):
    pos = -1
    for i, item in enumerate(automovil):
        if(item[0] == dominio):
            pos = i
            break
    return pos 


def  reservarAutomovil(automovil):
    print('Reservar Automovil')
    dominio = input('Ingrese Dominio: ')
    pos = buscarPorDominio(automovil,dominio)
    if (pos != -1) and ((automovil[pos][7] != 'R') or (automovil[pos][7]=='V')):
        automovil[pos][7] = 'R'
        print('Automovil Reservado')
    else:
        print('Automovil Inexistente o ya se encuentra Reservado o Vendido')

automovil=[]
automovil=leerAutomoviles(automovil)
"""bubbleSort(automovil)
print(automovil)
insertionSort(automovil)
print(automovil)
shellSort(automovil)#dominio
print(automovil)
quicksort(automovil, 0, len(automovil)-1)#modelo
print(automovil)
myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)
mergeSortAuto(automovil)
print(automovil)"""
reservarAutomovil(automovil)
print(automovil)