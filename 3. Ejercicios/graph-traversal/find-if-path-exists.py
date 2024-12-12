def validPath(n, edges, source, destination):
    # Crear una lista de adyacencia para representar el grafo
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()  # Conjunto para rastrear nodos visitados
    stack = [source]  # Pila para DFS, comenzando desde el nodo de origen

    while stack:
        node = stack.pop()  # Extraer un nodo de la pila

        # Si encontramos el nodo de destino, devolver True
        if node == destination:
            return True

        visited.add(node)  # Marcar el nodo como visitado

        # Agregar los vecinos no visitados del nodo actual a la pila
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    # Si no encontramos el destino, devolver False
    return False

n = 6
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]]
source = 0
destination = 5

result = validPath(n, edges, source, destination)
print(result)  # Debería imprimir True, porque hay un camino 0 -> 2 -> 3 -> 4 -> 5

