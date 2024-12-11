import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, source, destination, weight):
        """Agrega una arista dirigida con un peso al grafo."""
        if source not in self.edges:
            self.edges[source] = []
        self.edges[source].append((destination, weight))

    def dijkstra(self, start):
        """Implementa el algoritmo de Dijkstra para encontrar caminos mínimos."""
        min_heap = [(0, start)]  # (distancia, nodo actual)
        distances = {start: 0}
        visited = set()

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# Ejemplo de uso
if __name__ == "__main__":
    graph = Graph()

    # Agregar aristas al grafo
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 6)
    graph.add_edge("C", "D", 3)

    # Ejecutar Dijkstra desde el nodo de inicio 'A'
    start_node = "A"
    shortest_paths = graph.dijkstra(start_node)

    print(f"Caminos mínimos desde el nodo '{start_node}':")
    for node, distance in shortest_paths.items():
        print(f"Nodo {node}: {distance}")
