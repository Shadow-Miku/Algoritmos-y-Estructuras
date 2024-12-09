def selection_sort(arr):
    """
    Implementa el algoritmo Selection Sort para ordenar una lista.

    Parámetros:
    arr (list): Lista de elementos a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    n = len(arr)

    for i in range(n):
        # Encontrar el índice del elemento mínimo en el resto de la lista
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambiar el elemento mínimo encontrado con el primer elemento no ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    unsorted_list = [64, 25, 12, 22, 11]
    print("Lista desordenada:", unsorted_list)

    sorted_list = selection_sort(unsorted_list)
    print("Lista ordenada:", sorted_list)
