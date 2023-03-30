from operator import truediv
import os


os.system('cls')
a = int(input('Ingrese un nro A: '))
b = int(input('Ingrese un nro B: '))
while (a!=0 and b!=0):
    if (a > 0 and b > 0): 
        if a < b:
            for nro in range(a, b+1):
                primo = True
                for i in range(2, (nro//2+1)):
                    if (nro%i==0):
                        primo = False
                        print(i)
                        break
                if primo:
                    print('EL NRO', nro, 'ES PRIMO')
                else:
                    print('EL NRO', nro, 'NO ES PRIMO')
        else:
            print('Intervalo erroneo!!!')
    a = int(input('Ingrese un nro A: '))
    b = int(input('Ingrese un nro B: '))   
