opcion = "si"
print("Hola mundo")
while opcion == "si":
    a = int(input("Ingrese un número entre 1 y 3: "))

    if (a>=1 and a<=3):
        if (a == 1):
            print("UNO")
        elif (a == 2):
            print("DOS")
        else:
            print("TRES")
    else:
        print("ERROR...")

    print("¿Desea continuar?")
    opcion = input("(si/no) : ")

print("PROGRAMA FINALIZADO")