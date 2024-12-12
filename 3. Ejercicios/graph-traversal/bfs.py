def bfs(graph, start):
    visited = set()       # Conjunto para almacenar los nodos visitados
    queue = [start]       # Cola inicial con el nodo de inicio
    result = []           # Lista para almacenar el orden de los nodos visitados

    while queue:
        node = queue.pop(0)  # Extraer el primer nodo de la cola

        if node not in visited:
            visited.add(node)  # Marcar el nodo como visitado
            result.append(node)  # Agregar el nodo al resultado
            # Agregar los nodos vecinos a la cola solo si no han sido visitados
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])

    return result  # O retornar "visited" si quieres mantener el conjunto de nodos visitados

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
result = bfs(graph, start_node)
print(result)  # Debería imprimir ['A', 'B', 'C', 'D', 'E', 'F']
