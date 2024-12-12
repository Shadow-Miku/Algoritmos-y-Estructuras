def binary_search(nums, target):
    # Supongamos que 'nums' ya está ordenado
    left = 0  # Índice inicial
    right = len(nums) - 1  # Índice final

    # Mientras no se crucen los índices
    while left <= right:
        mid = (left + right) // 2  # Punto medio

        # Si encontramos el objetivo, devolvemos el índice
        if nums[mid] == target:
            return mid
        # Si el objetivo es mayor, descartamos la mitad izquierda
        elif nums[mid] < target:
            left = mid + 1
        # Si el objetivo es menor, descartamos la mitad derecha
        else:
            right = mid - 1
    
    # Si no encontramos el objetivo, devolvemos -1
    return -1

# Ejemplo de uso
nums = [4, 2, 5, 1, 3]
nums.sort()  # Ordenar la lista antes de buscar
target = 3
index = binary_search(nums, target)
print(f"El índice del objetivo es: {index}")
