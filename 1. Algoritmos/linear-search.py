def linear_search(arr, target):
    """
    Implementa el algoritmo de búsqueda lineal para encontrar un elemento en una lista.

    Parámetros:
    arr (list): Lista de elementos donde buscar.
    target: Elemento a buscar en la lista.

    Retorna:
    int: Índice del elemento encontrado o -1 si no se encuentra.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index  # Retorna el índice si se encuentra el elemento
    return -1  # Retorna -1 si el elemento no está en la lista

# Ejemplo de uso
if __name__ == "__main__":
    elements = [10, 20, 30, 40, 50]
    print("Lista de elementos:", elements)

    # Elementos a buscar
    targets = [30, 60, 10]

    for target in targets:
        result = linear_search(elements, target)
        if result != -1:
            print(f"El elemento {target} se encuentra en el índice {result}.")
        else:
            print(f"El elemento {target} no está en la lista.")