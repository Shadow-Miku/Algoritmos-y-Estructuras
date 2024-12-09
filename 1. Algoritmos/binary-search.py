def binary_search(arr, target):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Parámetros:
    arr (list): Lista ordenada de elementos.
    target: Elemento a buscar en la lista.

    Retorna:
    int: Índice del elemento buscado o -1 si no se encuentra.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Encuentra el punto medio

        # Caso: el elemento se encuentra
        if arr[mid] == target:
            return mid

        # Ajustar los límites de búsqueda
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Elemento no encontrado

# Ejemplo de uso
if __name__ == "__main__":
    # Lista ordenada para realizar la búsqueda
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print("Lista ordenada:", sorted_list)

    # Elementos a buscar
    targets = [7, 14, 19, 1]

    for target in targets:
        result = binary_search(sorted_list, target)
        if result != -1:
            print(f"El elemento {target} se encuentra en el índice {result}.")
        else:
            print(f"El elemento {target} no está en la lista.")
