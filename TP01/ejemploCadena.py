
cadena = input("ingrese una cadena: ")
contador = 0
for letra in cadena: 
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador += 1

print('Cantidad de vocales: ', contador)
