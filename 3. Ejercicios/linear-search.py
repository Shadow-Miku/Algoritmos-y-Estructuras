"""Searches for a target value in an array using linear search.

Iterates through each element in the array and compares it with the target value.

If the target is found, returns the index of the target; otherwise, returns -1.
"""

def linear_search(arr, target):
    # Iteramos a través de cada índice en el arreglo 'arr'
    for i in range(len(arr)):
        # Comparamos el elemento en la posición actual con el 'target'
        if arr[i] == target:
            # Si encontramos el 'target', retornamos el índice 'i'
            return i
    # Si no encontramos el 'target' en el arreglo, retornamos -1
    return -1
