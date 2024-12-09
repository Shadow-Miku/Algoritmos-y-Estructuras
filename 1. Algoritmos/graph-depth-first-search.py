def depth_first_search(graph, start, visited=None):
    """
    Implementa el algoritmo de búsqueda en profundidad (DFS) de forma recursiva.

    Parámetros:
    graph (dict): Representación del grafo como lista de adyacencia.
    start: Nodo inicial para comenzar el recorrido.
    visited (set): Conjunto de nodos visitados.

    Retorna:
    list: Lista de nodos en el orden en que fueron visitados.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    dfs_order = [start]  # Lista para almacenar el orden de visita

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_order.extend(depth_first_search(graph, neighbor, visited))

    return dfs_order

# Ejemplo de uso
if __name__ == "__main__":
    # Grafo representado como una lista de adyacencia
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Grafo:", graph)
    start_node = 'A'

    print(f"\nRecorrido DFS comenzando desde el nodo '{start_node}':")
    dfs_result = depth_first_search(graph, start_node)
    print(dfs_result)