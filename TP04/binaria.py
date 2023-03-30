def busquedaBinaria(lista, x):
    """Búsqueda binaria
    Precondición: lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """

    izq = 0 # izq guarda el índice inicio del segmento
    der = len(lista) -1 # der guarda el índice fin del segmento

    # un segmento es vacío cuando izq > der:
    while izq <= der:
        medio = (izq+der)//2

        print ("DEBUG:", "izq:", izq, "der:", der, "medio:", medio)

        if lista[medio] == x:
            return medio
        elif lista[medio] > x:
            der = medio-1
        else:
            izq = medio+1
    return -1


def main():
    #lista = [1, 3, 5, 12, 30, 31, 35, 60, 61, 63, 68,70,90]
    lista = range(100000)
    x = int(input("¿Valor buscado?: "))
    resultado = busquedaBinaria(lista, x)
    print ("Resultado:", resultado)

# Programa principal
main()
