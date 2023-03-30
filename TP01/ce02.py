import random


def generarLista():
    lista = []
    n = int(input('Ingrese n: '))
    for i in range(n):
        lista.append(random.randint(0,1000))
    return lista
def numerosEnIntervalo(lista):
    a = int(input('Ingrese a: '))
    b = int(input('Ingrese b: '))
    for valor in lista:
        if valor >= a and valor <= b:
            print(valor)

#principal
lista = generarLista()
print(lista)
numerosEnIntervalo(lista)
