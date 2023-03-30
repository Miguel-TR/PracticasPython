cadena='marcelo$$'
print(cadena.isalnum()) ##caractres especiales
print(cadena.isalpha())
#isdigit()
#isnumeric() 


sentence = "i am learning PYTHON."

# capitalize the first character 
capitalized_string = sentence.capitalize()

# the sentence string is not modified 
print('Before capitalize():', sentence)

print('After capitalize():', capitalized_string)


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)


message = 'Python is fun'
# check if the message ends with fun
print(message.endswith('fun'))


def leerDni():
    dni = input('Ingrese Dni: ')
    while (len(dni)!=8) and (dni.isdigit()):
        print('El DNI debe tener 8 digitos!!!')
        dni = input('Ingrese Dni: ')

def validaMayuscula(x):
    mayuscula = False
    for caracter in x:
        if caracter.isupper():
            mayuscula = True
            break
    return mayuscula

def validaClave(clave):
    valida = False
    if (len(clave) >= 6) and (clave.isalnum()) and (validaMayuscula(clave)):
        valida = True
    return valida

def leerClave():
    clave = input('Ingrese Clave: ')
    while not validaClave(clave):
        clave = input('Ingrese Clave: ')

def validaNombre(nombre):
    valida = False
    if (len(nombre) >= 3) and not(nombre.isalnum()):
        valida = True
    return valida

def leerNombre():
    nombre = input('Ingrese el Nombre: ')
    while validaNombre(nombre):      
        print('El Nombre debe tener 3 o mas caracteres y sin dìgitos!!!')

def leerAlumnos():
    print('Cargar Alumnos')
    alumnos = {   25:['Lapiz', 35.0, 80],
                    15:['Goma', 21.0, 0],
                    36:['Lapicera', 45.5, 0],
                    12:['Regla 20cm', 66.5, 30]}
    continua ='s'
    while (continua == 's'):
        dni = leerDni()
        if dni not in alumnos: 
            stock = leerStock()
            productos[codigo] = [descripcion, precio, stock]
            print('Producto agregado correctamente')
        else:
            print('el producto ya existe')
        continua = input('Desea cargar otros Productos: s/n?')    
    return productos


def convertirADiccionario(listaExterna):
    diccionario = {}
    indice = 1
    for mov in listaExterna: 
        movimiento = mov.split(",")
        print(movimiento)
        importeString = movimiento[2]
        print(importeString)
        importe = float(importeString[:-2] + "." + importeString[-2:])
        movimiento[2] = importe
        diccionario[indice] = movimiento ## Agrego el movimiento al diccionario
        indice += 1 
    return diccionario    

def mostrarMovimientos(diccionarioCuentas):
    for indice, mov in diccionarioCuentas.items(): 
        print(indice, mov)

def mostrarDepositos(diccionarioCuentas):
    print("Lista de Depósitos Realizados")
    suma = 0.
    for indice, mov in diccionarioCuentas.items(): 
        if mov[4] == 'D':
            print(indice, mov)
            suma += mov[2]
    print("Total Acumulado: ", suma)        

def mostrarMovimientosDeUnaCuenta(diccionarioCuentas):
    numeroCuenta = input('Ingrese Nro de Cuenta: ')

    for indice, mov in diccionarioCuentas.items(): 
        if mov[0] == numeroCuenta: 
            print(indice, mov)    

listaExterna = ["27200123456,MARIA FERNANDEZ,0000500056,30-05-2021,E",
                "27200321654,CARLOS TORRES,0000400045,31-05-2021,D",
                "27200987125,LAURA AQUINO,0000230000,30-05-2021,D",
                "27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E",
                "27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E",
                "27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D"]

diccionarioCuentas = convertirADiccionario(listaExterna)
mostrarMovimientos(diccionarioCuentas)
mostrarDepositos(diccionarioCuentas)
mostrarMovimientosDeUnaCuenta(diccionarioCuentas)
