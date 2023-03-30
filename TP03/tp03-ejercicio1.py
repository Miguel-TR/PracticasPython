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
                 ['AC245EV', 'Ford', 'Utilitario', 2006, 80000, 150000, 175000,'D'],
                 ['AA110ED', 'Citroen', 'Automovil', 2019, 20000, 350000, 400000, 'D'],
                 ['AE205EV', 'Ford', 'Utilitario', 2006, 80000, 150000, 178000,'D'],
                 ['AB101ED', 'Renault', 'Automovil', 2019, 20000, 250000, 277000, 'D'],
                 ['AC100EV', 'Ford', 'Utilitario', 2006, 80000, 150000, 176000,'D'],
                 ['AA102ED', 'Citroen', 'Automovil', 2019, 20000, 350000, 401000, 'D'],
                 ['AE206EV', 'Ford', 'Utilitario', 2006, 80000, 150000, 172000,'D'],
                 ['AE300EV', 'Renault', 'Utilitario', 2006, 80000, 150000, 170000,'D'],
                 ['AE033EV', 'Citroen', 'Automovil', 2006, 80000, 150000, 140000,'D']
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

automovil=[]
automovil=leerAutomoviles(automovil)
bubbleSort(automovil)
print(automovil)
insertionSort(automovil)
print(automovil)
