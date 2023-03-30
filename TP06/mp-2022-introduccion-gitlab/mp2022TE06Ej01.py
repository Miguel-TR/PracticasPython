
def menu():
    print('1) Ingresar A y B')
    print('2) Sumar A con B')
    print('3) Opcion 3')
    print('9) Salir')
    eleccion = int(input('Elija una opción: '))
    while not((eleccion >= 1) and (eleccion <= 9)):
        eleccion = int(input('Elija una opción: '))
    return eleccion

def sumar(x, y):
    suma = x + y
    print('Suma:', suma)

#Módulo principal
opcion = 0
while opcion != 9:
    opcion = menu()
    if opcion == 1:
        a = float(input('A: '))
        b = float(input('B: '))
    elif opcion == 2:
        sumar(a, b)
    elif opcion == 3:
        print ('Opcion 3')
    elif (opcion == 9):        
        print('Fin del programa')
    else:
        print('Error: Opción inválida')
    input('Para continuar presione enter ...OK')
