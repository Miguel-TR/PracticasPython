
def registrar(lista):
    while(True):
        codigo=validarCodigo(lista)
        descripcion=validarContenido("Ingrese la descripcion: ")
        precio=validarNumero("Ingrese el precio: ")
        stock =validarNumero("Ingrese el stock: ")
        lista.append([codigo,descripcion,precio,stock])
        opcion=(input("Desea agregar otro Producto?: (S/N)")).upper()
        if opcion == "N":
            break
    return lista

def validarCodigo(lista):
    codigo=input("Ingrese el codigo: ")
    while codigo in lista[0] or codigo.isspace() or codigo == "":
        if codigo.isspace() or codigo == "":
            print("El codigo no es valido")
        else:
            print("El codigo ya existe ingrese otro codigo")
        codigo=input("Ingrese el codigo: ")
    print("El codigo es valido")
    return codigo

def validarNumero(mensaje):
    while True:
        try :
            numero= int(input((mensaje)))
            if numero >= 0:
                break
            else:
                print("Ingrese un numero mayor o igual 0")
        except ValueError:
            print("Ingrese un numero entero")
    return numero

def validarContenido(mensaje):
    informacion=input(mensaje)
    while(informacion.isspace() or informacion == ""):
        print("Informacion invalida")
        informacion=input(mensaje)
    return informacion


def menu():
    print("a. Registar producto")
    print("b. Mostrar el listado de productos")
    print("c. Mostrar los productos cuyo stock se encuentre en el intervalo [desde,hasta]")
    print("d. Diseñar un proceso que le sume X al stock de todos los productos cuyo valor actual de stock sea menor al valor Y")
    print("e. Eliminar todos los productos cuyo stock sea igual a cero.")
    print("f. Salir")
    opcion=(input("Que operacion desea realizar:")).lower()
    while opcion not in ["a","b","c","d","e","f"]:
        print("Ingreso invalido")
        opcion=input("Que operacion desea realizar:")
    return opcion
def mostrarProducto(lista):
    print("Productos Registrados")
    for i in lista:
        print(i)
    


lista=[
    ["123","uno",150,0],
    ["321","dos",300,10],
    ["012","tres",120,200],
    ["452","cuatro",100,0]
]
opcion=menu()
while opcion != "f":
    if opcion == "a":
        registrar(lista)
    elif opcion == "b":
        print()
    elif opcion == "c":
        print()
    elif opcion == "d":
        print()
    elif opcion == "e":
        print()
    opcion=menu()
print("Fin del programa")