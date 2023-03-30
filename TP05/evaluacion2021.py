
import os
from turtle import pos
  
def menu():
    print('Menu de Opciones')
    print('1) Cargar Empleados')
    print('2) Mostrar Productos')
    print('3) Eliminar productos')
    print('4) Orden ascendente')
    print('5) Salir')
    print('Fin del menu')
    eleccion = int(input('Elija una opción: '))
    while not((eleccion >= 1) and (eleccion <= 7)):
        eleccion = int(input('Elija una opción: '))
    os.system('cls')
    return eleccion

def eliminar1(lista):##listas
    auxempleado= lista.copy()
    #print(auxiliarProducto)
    id =input('Ingrese el id a eliminar')
    for clave, valor in lista.items():
        if (clave == 0): 
            print('Se va a eliminar: ', lista[clave])
            del auxempleado[clave]
            print ('Eliminado ...')
    #print(auxiliarProducto)        
    lista = auxempleado
    return (lista)

def obligatorio():
    nombre = input('Ingrese un nombre: ')
    while not (len(nombre)):
        nombre = input('ingrese de nuevo el nombre: ')
    return nombre

def obligatorioDni():
    email = input('Ingrese un email:')
    while not (len(email)):
        email = input('Ingrese de nuevo un email:')
    return email

def cargarEmail():
    email = obligatorioDni()
    for letra in email:
        if letra == '@':
            print('cargado correctamente')
        return email  
        
def cargarDpto():
    marca = input('Marca 1:gerencia - 2:ventas - 3:compras ' )
    while not(marca in ['1','2','3']):
        marca = input('Departamento  1 - 2 - 3: ' )
    if marca =='1':
        marca = 'gerencia'
    elif marca =='2':
        marca = 'ventas'  
    elif marca =='3':
        marca == 'compras'
    else:
        marca = input('error - Marca 1:gerencia - 2:ventas - 3:compras ' )
    return marca

def mostrarEmpleados(lista):
    print('Listado de empleados')
    for clave, valor in lista.items():#me devuelve la clave y el valor(lista)
        print(clave,valor)

def selectionSort(lst):
    n = len(lst)
    for step in range(n):
        j = step
        for i in range(step + 1, n):
            if lst[i][0] < lst[j][0]:
                j = i
        lst[step], lst[j] = lst[j], lst[step]
        print(lst)
    return lst    

def cargarEmpleados(lista):
    empleados = {83:['Juan', 'pepito@...',1],
                 84:['Jose', 'beto@...',3],
                 85:['Maria', 'mari@...',2]}
    continuar = 's'
    while continuar == 's':
        id = int(input('ingrese id'))
        if id not in empleados:
            nombre = obligatorio()
            email = cargarEmail()
            departamento = cargarDpto()
            empleados [id] = (nombre, email, departamento)
        else:
            print('el id ingresado ya existe')
        continuar = input('Desea seguir? s/n')
        
def salir():
    print('Fin del programa...')

def continuar():
    print()
    input('presione una tecla para continuar ...')
    os.system('cls')

        
#PRINCIPAL
opc = 1
lista =[]
while (opc !=5 ):
    opc = menu()
    if opc == 1:
        cargarEmpleados(lista)
    elif (opc == 2):
        mostrarEmpleados(lista)
    elif (opc == 3):
        eliminar1(lista)
    elif(opc == 4):
        selectionSort(lista)
    elif (opc == 5):
        salir()
    continuar()
    