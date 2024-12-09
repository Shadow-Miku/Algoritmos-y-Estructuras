class Graph:
    def __init__(self):
        # Inicializa un diccionario vacío para almacenar la lista de adyacencia.
        self.adjacency_list = {}

    def add_node(self, node):
        # Agrega un nuevo nodo al grafo.
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        else:
            print(f"El nodo '{node}' ya existe en el grafo.")

    def add_edge(self, node1, node2):
        # Agrega una arista no dirigida entre node1 y node2.
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            if node2 not in self.adjacency_list[node1]:
                self.adjacency_list[node1].append(node2)
                self.adjacency_list[node2].append(node1)
            else:
                print(f"La arista entre '{node1}' y '{node2}' ya existe.")
        else:
            print(f"Uno o ambos nodos ('{node1}', '{node2}') no existen en el grafo.")

    def remove_edge(self, node1, node2):
        # Elimina una arista no dirigida entre node1 y node2.
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            if node2 in self.adjacency_list[node1]:
                self.adjacency_list[node1].remove(node2)
                self.adjacency_list[node2].remove(node1)
            else:
                print(f"La arista entre '{node1}' y '{node2}' no existe.")
        else:
            print(f"Uno o ambos nodos ('{node1}', '{node2}') no existen en el grafo.")

    def remove_node(self, node):
        # Elimina un nodo y todas sus aristas asociadas.
        if node in self.adjacency_list:
            for neighbor in self.adjacency_list[node]:
                self.adjacency_list[neighbor].remove(node)
            del self.adjacency_list[node]
        else:
            print(f"El nodo '{node}' no existe en el grafo.")

    def display(self):
        # Muestra la representación del grafo como una lista de adyacencia.
        for node, neighbors in self.adjacency_list.items():
            print(f"{node}: {neighbors}")

    def dfs(self, start_node, visited=None):
        # Realiza un recorrido en profundidad (DFS) desde un nodo inicial.
        if visited is None:
            visited = set()

        if start_node not in self.adjacency_list:
            print(f"El nodo '{start_node}' no existe en el grafo.")
            return

        visited.add(start_node)
        print(start_node, end=" ")

        for neighbor in self.adjacency_list[start_node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Ejemplo de uso
graph = Graph()

# Agregar nodos
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

# Agregar aristas
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")

# Mostrar el grafo
graph.display()

print("\nRecorrido en profundidad (DFS) desde el nodo 'A':")
graph.dfs("A")

# Eliminar un nodo y una arista
print("\n\nEliminando la arista entre 'A' y 'B':")
graph.remove_edge("A", "B")
graph.display()

print("\nEliminando el nodo 'D':")
graph.remove_node("D")
graph.display()
