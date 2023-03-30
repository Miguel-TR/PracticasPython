import os
from cmath import sqrt
from math import factorial


def menu():
    print('a) Raiz de A ')
    print('b) Cociente A y B')
    print('c) Calcular R')
    print('d) Salir')
    opcion = input('Elija una opción: ')
    return opcion 

def raizCuadrada(x):
    if(x >= 0): 
        print("Raiz: ", sqrt(x))
    else: 
        print('Error radicando negativo...')

def cociente(a, b):
    if(b != 0): 
        print("cociente: ", a / b)
    else: 
        print('Error división por cero...')

def calcularR(A, B):
    if A == 0: 
        print('División por cero...')
    elif A < 0 or B < 0:
        print('Factorial negativo...')    
    else: 
        return (factorial(A) - factorial(B)) / A**5

#Programa Principal
A = int(input('Ingrese A: '))
B = int(input('Ingrese B: '))

opcion = '*'
while opcion != 'd':
    opcion = menu()
    if(opcion == 'a'):
        raizCuadrada(A)
    elif opcion == 'b':
        cociente(A,B)
    elif opcion == 'c':
        print('Valor R: ',calcularR(A,B))
    elif opcion == 'd':
        print('Fin...')
        

