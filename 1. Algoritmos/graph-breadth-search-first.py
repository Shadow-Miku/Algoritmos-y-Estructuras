from collections import deque

def breadth_first_search(graph, start):
    """
    Implementa el algoritmo de búsqueda en anchura (BFS) para recorrer un grafo.

    Parámetros:
    graph (dict): Representación del grafo como lista de adyacencia.
    start: Nodo inicial para comenzar el recorrido.

    Retorna:
    list: Lista de nodos en el orden en que fueron visitados.
    """
    visited = set()  # Conjunto para rastrear nodos visitados
    queue = deque([start])  # Cola para gestionar el orden de recorrido
    bfs_order = []  # Lista para almacenar el orden de visita

    while queue:
        current = queue.popleft()  # Extraer el primer nodo de la cola

        if current not in visited:
            visited.add(current)  # Marcar el nodo como visitado
            bfs_order.append(current)  # Almacenar el nodo visitado

            # Agregar a la cola los vecinos no visitados
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

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

    print(f"\nRecorrido BFS comenzando desde el nodo '{start_node}':")
    bfs_result = breadth_first_search(graph, start_node)
    print(bfs_result)