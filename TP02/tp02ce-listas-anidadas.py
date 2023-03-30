import os

def presionarTecla():
   input('Presione una tecla...')

def menu():
    os.system('cls')
    print('1) Leer alumnos')
    print('2) Mostrar alumnos')
    print('3) Buscar por DNI')
    print('4) Modificar un alumno')
    print('5) Eliminar por DNI')
    print('6) Mostrar promedio')
    print('7) salir ')
    opcion = int(input('Seleccione una opción: '))
    return opcion
    
def leerNota():
    nota = float(input('Nota: '))
    while not(nota >= 0 and nota <= 10):
        print('Nota no válida...')
        nota = float(input('Nota: '))
    return nota    

def leerAlumnos():
    lista = []
    dni = 999
    while dni != 0:
        dni = int(input('DNI: '))
        if dni != 0:
            nombre = input('Nombre: ')
            nota = leerNota()
            lista.append([dni, nombre, nota])
    return lista

def buscarPorDni(alumnos, dni):
    pos = -1
    for i, item in enumerate(alumnos):
        if(item[0] == dni):
            pos = i
            break
    return pos    

def buscar(alumnos): 
    dni = int(input('DNI: '))
    pos = buscarPorDni(alumnos, dni)
    if(pos == -1): 
        print('No existe el dni ingresado...')
    else:
        print(alumnos[pos])    
    presionarTecla()    

def eliminar(alumnos):
    dni = int(input('DNI: '))
    pos = buscarPorDni(alumnos, dni)
    if(pos == -1): 
        print('No existe el dni ingresado...')
    else:
        alumnos.pop(pos)
        print('El alumno fue elimnado...')
    presionarTecla()    

def modificar(alumnos):
    dni = int(input('DNI: '))
    pos = buscarPorDni(alumnos, dni)
    if(pos == -1): 
        print('No existe el dni ingresado...')
    else:
        nombre = input('Nuevo nombre: ')
        nota = leerNota()
        alumnos[pos][1] = nombre
        alumnos[pos][2] = nota
        print('El alumno fue modificado...')
    presionarTecla()  

def suma(alumnos):
    suma = 0.
    for item in alumnos:
        suma += item[2]
    return suma

def promedio(alumnos):
    return suma(alumnos) / len(alumnos)

def mostrarAlumnos(lista):
    for posicion, alumno in enumerate(lista):
        print(posicion, alumno)
    return

#Principal
opcion = 0
alumnos = []
while opcion != 7: 
    opcion = menu()
    if opcion == 1:
        alumnos = leerAlumnos()
    elif opcion == 2:
        mostrarAlumnos(alumnos)
        presionarTecla()
    elif opcion == 3: 
        buscar(alumnos)    
    elif opcion == 4:     
        modificar(alumnos)    
    elif opcion == 5: 
        eliminar(alumnos)    
    elif opcion == 6:
        if(len(alumnos) > 0):
            print('Promedio: ', promedio(alumnos))
        else:
            print('La lista no posee alumnos...')
        presionarTecla()
    elif opcion == 7:
        print('Fin del programa...')    
        presionarTecla()


