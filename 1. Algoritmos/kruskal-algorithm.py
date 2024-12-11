class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Compresión de caminos
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph, num_vertices):
    # Ordenar las aristas por peso
    edges = sorted(graph, key=lambda x: x[2])
    union_find = UnionFind(num_vertices)
    mst = []  # Almacenará las aristas del MST
    total_weight = 0

    for edge in edges:
        u, v, weight = edge
        if union_find.find(u) != union_find.find(v):  # Verificar si forman ciclo
            union_find.union(u, v)
            mst.append(edge)
            total_weight += weight

    return mst, total_weight


# Ejemplo de uso
if __name__ == "__main__":
    # Grafo representado como lista de aristas (u, v, peso)
    graph = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    num_vertices = 4
    mst, total_weight = kruskal(graph, num_vertices)

    print("Árbol de Expansión Mínima (MST):")
    for u, v, weight in mst:
        print(f"Arista ({u}, {v}) con peso {weight}")
    print(f"Peso total del MST: {total_weight}")
