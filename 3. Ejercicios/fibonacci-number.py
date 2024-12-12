def fib(n):
    #Version iterativa optimizada
    # Caso base para n = 0
    if n == 0:
        return 0
    # Caso base para n = 1
    elif n == 1:
        return 1
    
    # Variables para almacenar los últimos dos valores de Fibonacci
    a, b = 0, 1
    # Calcular Fibonacci desde 2 hasta n
    for i in range(2, n + 1):
        a, b = b, a + b
    
    # Devolver el valor de Fibonacci para n
    return b

# Ejemplo de uso
n = 10
print(fib(n))   # Debería imprimir 55

# Complejidad temporal: O(n)
# Complejidad espacial: O(1)


# Version iterativa
"""
def fib(n):
# Caso base para n = 0 
 if n == 0: 
    return 0 
# Caso base para n = 1 
elif n == 1: 
    return 1 
# Lista para almacenar los valores de Fibonacci 
fibs = [0, 1] 
# Calcular Fibonacci desde 2 hasta n 
for i in range(2, n + 1): 
    fibs.append(fibs[i - 1] + fibs[i - 2]) 
# Devolver el valor de Fibonacci para n 
return fibs[n]
"""

# Version con memorizacion
"""
def fib(n, memo={}):
    # Caso base: si el valor ya está en memo, se devuelve
    if n in memo:
        return memo[n]
    
    # Caso base para n = 0
    if n == 0:
        return 0
    # Caso base para n = 1
    elif n == 1:
        return 1
    else:
        # Almacenar el resultado en memo y devolverlo
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]
"""
