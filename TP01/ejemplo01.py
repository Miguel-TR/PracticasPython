
def saludo():
    print("Hello world...")

def ingresoDatos():
    nombre = input("Ingrese su nombre: ")
    print ("hello ", nombre)
    edad = int(input("ingrese su edad: "))
    return nombre, edad
def esMayorDeEdad(edad):
    resultado = False
    if edad >= 18:
        resultado = True
    return resultado

# Programa Principal
saludo()
nombre, edad = ingresoDatos()
if esMayorDeEdad(edad):
    print("usted es mayor de edad")
else:
    print("usted es menor de edad")    
