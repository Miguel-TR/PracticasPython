"""Ordenar la lista 6, 0, 3, 2, 5, 7, 4, 1 usando el método quicksort. Mostrar el árbol de recursividad
explicando las llamadas que se hacen en cada paso, y el orden en el que se realizan. Utilice lápiz y papel
para resolver el ejercicio"""

from multiprocessing.resource_sharer import stop
from tracemalloc import start


def quicksort(lst, start, stop): #https://www.youtube.com/watch?v=YzHDIvxOQcI
    if stop - start > 0:
        pivot, left, right = lst[start], start, stop
        while left <= right:
            while lst[left] < pivot: #estos dos se cambiaria para cambiar de orden descendente < asc   > desc
                left += 1
            while lst[right] > pivot: # este es el contrario al anterior
                right -= 1
            if left <= right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        quicksort(lst, start, right)
        quicksort(lst, left, stop)
    return lst

lista = [6, 0, 3, 2, 5, 7, 4, 1]
print(lista)
(quicksort(lista, 0, len(lista)-1))
print (lista)


