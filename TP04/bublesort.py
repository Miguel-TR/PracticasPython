def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


lista = [3, 5, 4, 1]    
print(lista)
#listaOrdenada = bubbleSort(lista)
lista.sort()
print(lista)