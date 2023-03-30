import os

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
    marca = input('Marca R - F - C: ' )
    while not(marca in ['R','F','C']):
        marca = input('Marca  R - F - C: ' )
    if marca =='R':
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

def leerAutomoviles(automovil):
    print('Cargar Lista de Automoviles')
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

def  reservarAutomovil(automovil):
    print('Reservar Automovil')
    dominio = input('Ingrese Dominio: ')
    pos = buscarPorDominio(automovil,dominio)
    if (pos != -1) and ((automovil[pos][7] != 'R') or (automovil[pos][7]=='V')):
        automovil[pos][7] = 'R'
        print('Automovil Reservado')
    else:
        print('Automovil Inexistente o ya se encuentra Reservado o Vendido')

print('convierte un fichero en una lista')
automovil=[]
fichero = open('vehiculos.txt','r')
texto = fichero.readlines()#aca texto es una lista
fichero.close()
for linea in texto:
    auto = linea.split(";")
    auto[7] = auto[7].replace("\n", "")
    automovil.append([auto[0],auto[1],auto[2],int(auto[3]),int(auto[4]),int(auto[5]),
                      int(auto[6]), auto[7]])
print(automovil)
presionarTecla()

print('convierte un fichero de texto a diccionario previo lista')
diccionario={}
contador=0
for auto in automovil:
  diccionario[contador] = auto
  contador += 1
print(diccionario)
presionarTecla()

automovil=leerAutomoviles(automovil)
#print(automovil)
fichero = open('vehiculos.txt','a+')
for linea in automovil:
        print(linea)
        linea[3]=str(linea[3])
        linea[4]=str(linea[4])
        linea[5]=str(linea[5])
        linea[6]=str(linea[6])
        texto = ';'.join(linea)
        fichero.write(texto+'\n')
fichero.close()

reservarAutomovil(automovil)
print(automovil)