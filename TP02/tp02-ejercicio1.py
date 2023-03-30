import os

def continuar():
    print()
    input('presione una tecla para continuar ...')
    os.system('cls')

def menu():
    print('1) Cargar Productos')
    print('2) Mostrar Productos')
    print('3) Mostrar Productos con stock [desde-hasta]')
    print('4) Buscar el precio más alto de la lista de productos')
    print('5) Modifica Stock con X cantidad para stock menor al valor Y')
    print('6) Eliminar Productos con stock 0 ')
    print('7) Salir')
    eleccion = int(input('Elija una opción: '))
    while not((eleccion >= 1) and (eleccion <= 7)):
        eleccion = int(input('Elija una opción: '))
    os.system('cls')
    return eleccion

def validaPositivo(x):
    valida = False
    if x < 0:
        valida = True
    return valida

def obligatorio():
    descripcion=input('Descripcion: ')
    while not len(descripcion):    #?len(descripcion) si es distinto de 0
        descripcion=input('Descripcion: ')
    return descripcion   

def leerPrecio():
    precio = float(input('Precio: '))
    while validaPositivo(precio):
        print('El Precio no puede ser negativo!!!')
        precio = float(input('Precio: '))
    return precio  

def leerStock():
    stock = int(input('Stock: '))
    while validaPositivo(stock):
        print('El Stock no puede ser negativo!!!')
        stock = int(input('Stock: '))
    return stock   

def mostrarProductos(diccionario):
    print('Listado de Productos')
    for clave, valor in diccionario.items():#me devuelve la clave y el valor(lista)
        print(clave,valor)

def leerProductos():
    print('Cargar Lista de Productos')
    productos = {   25:['Lapiz', 35.0, 80],
                    15:['Goma', 21.0, 0],
                    36:['Lapicera', 86.5, 0],
                    12:['Regla 20cm', 66.5, 30], 
                    13:['Regla 30cm', 76.5, 60],
                    14:['Regla 50cm', 86.5, 70]}
    continua ='s'
    while (continua == 's'):
        codigo = int(input('Ingrese Codigo: '))
        if codigo not in productos: 
            descripcion = obligatorio()
            precio = leerPrecio()
            stock = leerStock()
            productos[codigo] = [descripcion, precio, stock]
            print('Producto agregado correctamente')
        else:
            print('el producto ya existe')
        continua = input('Desea cargar otros Productos: s/n?')    
    return productos

def leerDesdeHasta():
    print('Stock desde:')
    stockdesde = leerStock()
    print('Stock Hasta:')
    stockHasta = leerStock()
    while stockHasta < stockdesde:
        print('Debe ingresar un Stock mayor a: ',stockdesde)
        stockHasta = leerStock()
    return stockdesde, stockHasta


def mostrarStock(productos, desde, hasta):
    print('Lista de Productos con stock entre [',desde, '-',hasta,']')
    for codigo, datos in productos.items():
        if (datos[2] >= desde and datos[2]<= hasta): 
            print(codigo, datos)

def mostrarStockDesdeHasta(productos):
        desde,hasta= leerDesdeHasta()
        mostrarStock(productos, desde, hasta)
        
def buscarMayorPrecio(productos):
    bmay=True
    for clave, valor in productos.items():
        if bmay:
            mayorPrecio=valor[1]# guarda el primer elemento
            bmay =False
        else:
            if valor[1]>mayorPrecio:
                mayorPrecio=valor[1]
    return mayorPrecio

def mostrarMayorPrecio(productos):
    print('Lista de Productos con mayor precio')
    mayorPrecio=buscarMayorPrecio(productos)
    for codigo, datos in productos.items():
        if (datos[1] == mayorPrecio): 
            print(codigo, datos)

def modificarStock(productos):
    print('Modificar Stock de Productos')
    print('Ingrese Stock X:')
    x = leerStock()
    print('Ingrese Stock Y:')
    y = leerStock()
    #llamar a otra funcion
    for codigo, datos in productos.items():
        if (datos[2] < y): 
            datos[2] +=x #para probar??????????????????
            #stock = datos[2]+x
            #productos[codigo] = [datos[0],datos[1],stock]
            print('Modificado correctamente')
            print('Antes')
            print(codigo, datos)
            print('Despues')
            print(productos[codigo])
            print(productos.items())
  
def eliminar1(productos):##listas
    auxiliarProducto= productos.copy()
    #print(auxiliarProducto)
    print('Elimina los prodcutos con Stock 0')
    for codigo, datos in productos.items():
        if (datos[2] == 0): 
            print('Se va a eliminar: ', productos[codigo])
            del auxiliarProducto[codigo]
            print ('Eliminado ...')
    #print(auxiliarProducto)        
    productos=auxiliarProducto    
    return (productos)

def eliminar2(productos):#diccionario
    print('Elimina los prodcutos con Stock 0')
    i = 1
    while i <= len(productos):
        for codigo, datos in productos.items():
            if (datos[2] == 0): 
                print('Se va a eliminar: ', productos[codigo])
                del productos[codigo]
                print ('Eliminado ...')
                break
        i+=1    
    return (productos)

def eliminar3(productos):
    for item in list(productos.keys()):# lo transforma en lista y utiliza una clave
        if productos[item][2]==0:
            del productos[item]

    
def salir():
    print('Fin del programa...')

#principal
opcion = 0
productos = {}
os.system('cls')
while (opcion != 7):
    opcion = menu()
    if opcion == 1:
        productos = leerProductos()
    elif opcion == 2:
        mostrarProductos(productos)
    elif opcion == 3:
        mostrarStockDesdeHasta(productos)
    elif opcion == 4:
        mostrarMayorPrecio(productos)
    elif opcion == 5:    
        modificarStock(productos)
    elif opcion == 6:
        eliminar2(productos)
    elif (opcion == 7):        
        salir()
    continuar()
