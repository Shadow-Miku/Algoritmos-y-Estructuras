def dfs(graph, start, visited=None):
    # Inicializar el conjunto de nodos visitados si es la primera llamada
    if visited is None:
        visited = set()

    visited.add(start)  # Marcar el nodo inicial como visitado
    dfs_order = [start]  # Lista para almacenar el orden de visita

    # Iterar sobre los vecinos del nodo actual
    for neighbor in graph.get(start, []):
        if neighbor not in visited:  # Si el vecino no ha sido visitado
            # Llamada recursiva para el vecino no visitado y extender dfs_order
            dfs_order.extend(dfs(graph, neighbor, visited))

    return dfs_order  # Retornar la lista con el orden de visita

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
dfs_result = dfs(graph, start_node)
print(dfs_result)  # Debería imprimir ['A', 'B', 'D', 'E', 'F', 'C']
