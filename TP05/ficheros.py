
from io import open

texto = "Una linea con texto\n\nOtra linea con texto"
#print(texto)
# Ruta donde crearemos el fichero, w indica
#escritura (puntero al principio)
fichero = open('leame.txt','w')
# Escribimos el texto
fichero.write(texto)
# Cerramos el fichero
fichero.close()

# Ruta donde leeremos el fichero, r
#indica lectura (por defecto ya es r)
fichero = open('leame.txt','r')
# Lectura completa
texto = fichero.read()
# Cerramos el fichero
fichero.close() 
print(texto)

fichero = open('vehiculos.txt','r')
# Leempos creando una lista de líneas
texto = fichero.readlines()
fichero.close()
print(texto)
print('texto[0]:',texto[0])#\n lo imprime como linea en blanco
print('texto[1]:',texto[1])

#Leer fichero con with
with open('leame.txt', 'r') as fichero:
    for linea in fichero:
        print(linea)
#Añadir datos al final de un fichero
fichero = open ("leame.txt", "a")
fichero.write("\notra linea agregada")    
fichero.close()
