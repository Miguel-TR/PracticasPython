from io import open
from operator import itemgetter, attrgetter

def validarDominio(automovil,dominio):
    valido = True
    for item in automovil:
        if dominio == item[0] or  not((len(dominio)>=6 and len(dominio)<=9)):
            valido = False
            break
    return valido  

def validarMarca(marca):
    valido = True
    if not(marca =='Renault' or marca =='Ford' or marca =='Citroen' or marca =='Fiat'):
        valido = False
    return valido

def validarTipo(tipo):
    valido = True
    if not(tipo == 'Automovil' or tipo == 'Utilitario'):  
        valido = False
    return valido

def validarModelo(modelo):
    valido = True
    if not(modelo>=2005 and modelo<=2020):
        valido = False
    return valido

def validarEstado(estado): # ■ Estado: (Vendido, Disponible, Reservado).
    valido = True
    #if not(estado == 'Vendido' or estado == 'Disponible' or estado == 'Reservado'):
    if not(estado=='D'):  #'D\n'
        valido = False
    return valido

def CargarLista():
    automovil=[]
# Ruta donde leeremos el fichero, r indica lectura (por defecto ya es r)
    fichero = open('vehiculos.txt','r')
# La función join convierte una lista en una cadena formada por los elementos de la lista 
# separados por comas. Por otro lado, split convierte una cadena de texto en una lista. 
# Por defecto, los elementos de dicha lista serán las palabras de la cadena

# Lectura completa
    texto = fichero.readlines()#aca tecto es una lista
    fichero.close()
   # print(texto)

    for linea in texto:
        auto = linea.split(";")
        print(auto)
    #x = linea.split(sep='\n')
        auto[7] = auto[7].replace("\n", "")
        if (validarDominio(automovil,auto[0]) and validarMarca(auto[1]) and validarTipo(auto[2]) and validarModelo(int(auto[3])) and validarEstado(auto[7])):
            automovil.append([auto[0],auto[1],auto[2],int(auto[3]),int(auto[4]),int(auto[5]),int(auto[6]), auto[7]])
            print('Agregado correctamente!!!')
    return automovil

def busquedaBinaria(lista, x):
   # [1,2,3,4,5,6,7,8]
    izq = 0 # izq guarda el índice inicio del segmento
    der = len(lista) -1 # der guarda el índice fin del segmento
    # un segmento es vacío cuando izq > der:
    while izq <= der:
        medio = (izq+der)//2
        if lista[medio][0] == x:
            return medio
        elif lista[medio][0]> x:
            der = medio-1
        else:
            izq = medio+1
    return -1

# Programa principal
marca='Ford'
nonFichero=marca+'.txt'
print(nonFichero)
input('presione una tecla para continuar ...')

automovil = CargarLista()
for item in automovil:
    print(item)
input('presione una tecla para continuar ...')    

dominio = input("¿Valor DOMINIO buscado?: ")
listaOrdenada = sorted(automovil,key=itemgetter(0))
print(listaOrdenada)
resultado = busquedaBinaria(listaOrdenada, dominio)
print(resultado)
print ("Resultado:", listaOrdenada[resultado])
input('presione una tecla para continuar ...')

marca = input("¿Valor de marca buscado?: ").upper()
print(marca)
for item in automovil:
    #cadena.upper()
    print(item[1].upper())
    posicion = (item[1].upper()).find(marca)
    print(posicion)
    if posicion != -1:
        print(item)
input('presione una tecla para continuar ...')
#obtengo la lista filtrada por marca
marca = input("¿Valor de marca buscado?: ")
listaMarca=[]
for auto in automovil:
    if auto[1] == marca:
        listaMarca.append([auto[0],auto[1],auto[2],str(auto[3]),str(auto[4]),str(auto[5]),str(auto[6]), auto[7]])
print(listaMarca)
input('presione una tecla para continuar ...')
#transformo la lista a texto
for linea in listaMarca:
        texto = ';'.join(linea)
        print(texto)

nomFichero=marca+'.txt'
print(nonFichero)


fichAuto = open(nomFichero,'a+')
for linea in listaMarca:
        texto = ';'.join(linea)
        fichAuto.write(texto+'\n')
        print(texto)
fichAuto.close()




