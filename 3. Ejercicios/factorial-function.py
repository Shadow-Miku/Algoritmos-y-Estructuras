def factorial(n):
    # Caso base: si n es 0, el factorial es 1
    if n == 0:
        return 1
    else:
        # Caso recursivo: multiplicar n por el factorial de (n - 1)
        return n * factorial(n - 1)

# Ejemplo de uso
n = 5
print(factorial(n))
# Complejidad temporal: O(n)
# Complejidad espacial: O(n)

print("\n")

# Version iterativa
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Ejemplo de uso
n = 5
print(factorial(n))

# Complejidad temporal: O(n)
# Complejidad espacial: O(1)