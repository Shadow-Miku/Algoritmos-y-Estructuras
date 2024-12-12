def insertion_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de Insertion Sort.

    :param arr: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    # Recorremos cada elemento de la lista, comenzando desde el segundo
    for i in range(1, len(arr)):
        # Guardamos el valor actual como clave
        key = arr[i]
        # Inicializamos una variable para rastrear la posición previa
        j = i - 1

        # Movemos los elementos de arr[0..i-1] que son mayores que la clave
        # una posición adelante de su posición actual
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insertamos la clave en su posición correcta
        arr[j + 1] = key

    return arr

# Ejemplo de uso
def main():
    # Lista de ejemplo
    numbers = [12, 11, 13, 5, 6]
    print("Lista original:", numbers)

    # Aplicar Insertion Sort
    sorted_numbers = insertion_sort(numbers)
    print("Lista ordenada:", sorted_numbers)

if __name__ == "__main__":
    main()