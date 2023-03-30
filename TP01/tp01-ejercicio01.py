import os


os.system('cls')

respuesta = 's'
while respuesta == 's':
    nro= int(input('Ingrese un numero entre 1 y 3: '))
    if(nro == 1):
        print('UNO')
    elif (nro == 2):
        print('DOS')
    elif (nro == 3):
        print('TRES')
    else:
        print('INGRESE UN VALOR DEL 1 AL 3')
    respuesta = input('Desea continuar? s/n: ')