import os
#from operator import itemgetter, attrgetter
alumnos = { 1:['Jorge','388-4896369'],
            2:['Anastasia','388-4896368'],
            3:['Mariela','388-4896367'],
            4:['Mariana','388-4896366'],
            5:['Analia','388-4896365'],
            6:['Fabiana','388-4896364'],
            7:['Claudia','388-4896363'],
            8:['Claudio','388-4896362'],
            9:['Jorgelina','388-4896361']}
nombre = input("¿NOmbre buscado?: ").upper()
print(nombre)
for clave, item in alumnos.items():
    #cadena.upper()
    print(item[0].upper())
    posicion = (item[0].upper()).find(nombre)#lo hace en mayuscula para ver la calidad y este unificada
    print(posicion)
    if posicion != -1:
        print(item)
input('presione una tecla para continuar ...')