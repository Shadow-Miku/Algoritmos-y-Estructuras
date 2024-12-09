def merge_sort(arr):
    """
    Implementa el algoritmo Merge Sort para ordenar una lista.

    Parámetros:
    arr (list): Lista de elementos a ordenar.

    Retorna:
    list: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr

    # Dividir la lista en mitades
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Combinar las mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    """
    Combina dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    left (list): Primera mitad ordenada.
    right (list): Segunda mitad ordenada.

    Retorna:
    list: Lista combinada y ordenada.
    """
    sorted_list = []
    i = j = 0

    # Comparar elementos de ambas mitades y combinarlos
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Agregar los elementos restantes
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Ejemplo de uso
if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    print("Lista desordenada:", unsorted_list)

    sorted_list = merge_sort(unsorted_list)
    print("Lista ordenada:", sorted_list)
