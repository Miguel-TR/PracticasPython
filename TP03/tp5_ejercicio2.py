import os
from operator import itemgetter, attrgetter

def continuar():
    print()
    input('presione una tecla para continuar ...')
    os.system('cls')

def menu():
    print('Menu de Opciones')
    print('1) Cargar Automoviles')
    print('2) Mostrar lista de Automoviles')
    print('3) Reservar un automóvil')
    print('4) Buscar un automóvil por su dominio')
    print('5) Ordenar la lista de automóviles en forma ascendente o descendente por Marca')
    print('6) Ordenar la lista de automóviles en forma ascendente o descendente por Marca')
    print('7) Salir')
    print('Fin del menu')
    eleccion = int(input('Elija una opción: '))
    while not((eleccion >= 1) and (eleccion <= 7)):
        eleccion = int(input('Elija una opción: '))
    os.system('cls')
    return eleccion

def presionarTecla():
   input('Presione una tecla...') 
   
def validarDominio(automovil,dominio):
    valido = True
    for item in automovil:
        if dominio == item[0]:
            valido = False
            break
    return valido   

def leerDominio():
    dominio = input('Dominio: ')
    dominio.replace(" ", "")
    while not(len(dominio)>=6 and len(dominio)<=9):
        dominio = input('Dominio: ')
    return dominio

def leerMarca():
    marca = input('Marca R - F - C: ' )#aqui se valida que sean r f o c
    while not(marca in ['R','F','C']):
        marca = input('Marca  R - F - C: ' )
    if marca =='R': #aqui se transforman a valores completos
        marca = 'Renault'
    elif marca =='F':
        marca = 'Ford'  
    else:
        marca = 'Citroen'
    return marca

def leerTipo():
    tipo = input('Tipo A - U: ' )
    while not(tipo in ['A','U']):
        tipo = input('Tipo A - U: ' )
    if tipo =='A':
        tipo = 'Automovil'
    elif tipo =='U':
        tipo = 'Utilitario'   
    return tipo       

def leerModelo():
    modelo = int(input('Modelo [2005-2020]: '))
    while not(modelo>=2005 and modelo<=2020):
        modelo = int(input('Modelo [2005-2020]: '))
    return modelo

def leerKilometraje():
    kilometraje = int(input('Kilometraje: '))
    while not(kilometraje >= 0):
        kilometraje = int(input('kilometraje: '))
    return kilometraje

def leerPrecioV():
    precioValor = int(input('Precio Valuado: '))
    while not(precioValor >= 10000):
        precioValor = int(input('Precio Valuado: '))
    return precioValor

def mostrar(lista):
    print('Listado de Automoviles')
    for item in lista:
        print(item)

def  mostrarDisponibles(lista):
    print('Listado de Automoviles Disponibles')
    for item in lista:
        if item[7] =='D':
            print(item)        

def leerAutomoviles(automovil):
    print('Cargar Lista de Automoviles')
    automovil = [['AB101ED', 'Renault', 'Automovil', 2019, 20000, 250000, 275000, 'D'],
                 ['AC245EV', 'Ford', 'Utilitario', 2006, 80000, 150000, 175000,'D'],
                 ['AA110ED', 'Citroen', 'Automovil', 2019, 20000, 350000, 400000, 'D'],
                 ['AE205EV', 'Ford', 'Utilitario', 2006, 80000, 150000, 175000,'D'],
                 ['AB101ED', 'Renault', 'Automovil', 2019, 20000, 250000, 275000, 'D'],
                 ['AC100EV', 'Ford', 'Utilitario', 2006, 80000, 150000, 175000,'D'],
                 ['AA102ED', 'Citroen', 'Automovil', 2019, 20000, 350000, 400000, 'D'],
                 ['AE206EV', 'Ford', 'Utilitario', 2006, 80000, 150000, 175000,'D'],
                 ['AE300EV', 'Renault', 'Utilitario', 2006, 80000, 150000, 175000,'D'],
                 ['AE033EV', 'Citroen', 'Automovil', 2006, 80000, 150000, 175000,'D']
                ]
    continuar = 's'
    while (continuar=='s'):
        dominio = leerDominio()
        if validarDominio(automovil,dominio):   
            marca = leerMarca() 
            tipo = leerTipo()
            modelo = leerModelo()
            kilometraje = leerKilometraje()
            precioValor = leerPrecioV()
            precioVta = int(precioValor *1.1)
            estado = 'D'
            automovil.append([dominio,marca,tipo,modelo,kilometraje,precioValor,precioVta, estado])
            print('Agregado correctamente!!!')
        else:
            print('El Dominio Ingresado ya existe!!!')
        continuar = input('Continua Cargando Automovil? s/n: ')    
    return automovil

def buscarPorDominio(automovil,dominio):
    pos = -1
    for i, item in enumerate(automovil):
        if(item[0] == dominio):
            pos = i
            break
    return pos   

def buscarAutomovil(automovil):
    print('Busqueda de Automovil')
    dominio = input('Ingrese Dominio: ')
    pos = buscarPorDominio(automovil,dominio)
    if (pos != -1):
        print(automovil[pos])
    else:
        print('Automovil Inexistente')

def  reservarAutomovil(automovil):
    print('Reservar Automovil')
    dominio = input('Ingrese Dominio: ')
    pos = buscarPorDominio(automovil,dominio)
    if (pos != -1) and ((automovil[pos][7] != 'R') or (automovil[pos][7]=='V')):
        automovil[pos][7] = 'R'
        print('Automovil Reservado')
    else:
        print('Automovil Inexistente o ya se encuentra Reservado o Vendido')

def salir():
    print('Fin del programa...')

#principal
opcion = 0
os.system('cls')
automovil=[]
while (opcion != 7):
    opcion = menu()
    if opcion == 1:
        automovil = leerAutomoviles(automovil)
    elif opcion == 2:
        mostrar(automovil)
    elif opcion == 3:
        reservarAutomovil(automovil)
    elif opcion == 4:
        buscarAutomovil(automovil)
    elif opcion == 5:
        listaOrdenada = sorted(automovil,key=itemgetter(1))
        mostrar(listaOrdenada)
        continuar()
        listaOrdenada = sorted(automovil,key=itemgetter(1), reverse=True)
        mostrar(listaOrdenada)
        continuar()
    elif opcion == 6:
        listaOrdenada = sorted(automovil,key=itemgetter(6))
        mostrarDisponibles(listaOrdenada)
        continuar()
        listaOrdenada = sorted(automovil,key=itemgetter(6), reverse=True)
        mostrarDisponibles(listaOrdenada)
        continuar()
    elif (opcion == 7):        
        salir()
    continuar()
