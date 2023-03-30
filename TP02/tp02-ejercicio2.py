from cgitb import reset
from math import e
import os

def continuar():
    print()
    input('presione una tecla para continuar ...')
    os.system('cls')

def menu():
    print('1) Cargar Agenda')
    print('2) Mostrar Agenda')
    print('3) Mostrar los contactos que contengan la subcadena')
    print('4) Mostrar los contactos que comienzan con...')
    print('5) Eliminar contacto')
    print('6) Salir')
    eleccion = int(input('Elija una opción: '))
    while not((eleccion >= 1) and (eleccion <= 6)):
        eleccion = int(input('Elija una opción: '))
    os.system('cls')
    return eleccion

def validaPositivo(x):
    valida = False
    if x < 0:
        valida = True
    return valida

def obligatorio():
    nombre=input('Nombre: ')
    while not len(nombre):    
        nombre=input('Nombre: ')
    return nombre   

def leerTelefono():
    telefono = int(input('Telefono: '))
    while validaPositivo(telefono):
        print('El Telefono no puede ser negativo!!!')
        telefono = int(input('Telefono: '))
    return telefono   

def mostrarAgenda(diccionario):
    print('Listado de Contactos')
    for clave, valor in diccionario.items():
        print(clave,valor)

def buscarNombre(agenda,nombre):
    codigo=-1
    for clave, valor in agenda.items():
        if valor[0]==nombre:
                codigo =clave
    return codigo

def leerAgenda(agenda, primero):
    print('Cargar Lista de Contactos')
    if primero:
        agenda = {  1:['Marcelo', 123456],
                    2:['Maria', 654123],
                    3:['Laura', 8796328],
                    4:['Raul', 6659630], 
                    5:['Rocio', 7656033],
                    6:['Ramon', 87963258]}
    continua ='s'
    while (continua == 's'):
        nombre = obligatorio()
        codigo=buscarNombre(agenda,nombre)
        if codigo!=-1:
            #modificar contacto
            print('Telefono del Contacto: ',agenda[codigo][1])
            respuesta = input('Desea modificar el telefono del Contacto s/n?:')
            if respuesta=='s':
                telefono = leerTelefono()
                agenda[codigo][1]=telefono
                print('El telefono del Contacto se modifico correctamente')
        else: 
            #añade contacto
            codigo = len(agenda)+1
            telefono = leerTelefono()
            agenda[codigo] = [nombre, telefono]
            print('Contacto agregado correctamente')
        continua = input('Desea añadir/modificar otros Contactos: s/n? ')    
    return agenda

def mostrarNombre(agenda): #si contiene la subcadena
    encontro=False
    #c=0
    nombre = input("Ingrese el Nombre del contacto: ").upper()
    #print(nombre)
    for clave, item in agenda.items():
        #cadena.upper()
        #print(item[0].upper())
        posicion = (item[0].upper()).find(nombre)
        #print(posicion)
        if posicion != -1:
            print(clave, item)
            #c+=1
            encontro=True
    if not encontro:
        print('No se encontro ninguna ocurrencia!!!') 
    #return c           

def mostrarNombreComienza(agenda):
    encontro=False
    nombre = input("Ingrese el Nombre del contacto: ").upper()
    for clave, item in agenda.items():
        if (item[0].upper()).startswith(nombre):
            print(item) 
            encontro=True
    if not encontro:
        print('No se encontro ninguna ocurrencia!!!')  

def eliminar(agenda):
    mostrarNombre(agenda)
    codigo=int(input('Ingrese el Codigo desea eliminar:'))
    #for item in list(agenda.keys()):
        #if agenda[item][2]==0:
    print('Esta por eliminar el contacto: ',agenda[codigo])    
    respuesta=input('Desea eliminar el contacto? s/n: ')
    if respuesta=='s':
        del agenda[codigo]
    
def salir():
    print('Fin del programa...')
    
#principal
opcion = 0
agenda = {}
os.system('cls')
primero=True
while (opcion != 6):
    opcion = menu()
    if opcion == 1:
        agenda = leerAgenda(agenda,primero)
        primero=False
    elif opcion == 2:
        mostrarAgenda(agenda)
    elif opcion == 3:
        mostrarNombre(agenda)
    elif opcion == 4:
        mostrarNombreComienza(agenda)
    elif opcion == 5:    
        eliminar(agenda)
    elif (opcion == 6):        
        salir()
    continuar()
