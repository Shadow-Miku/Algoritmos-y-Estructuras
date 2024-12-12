class UndirectedGraph:
    def __init__(self):
        # Implement the class constructor
        self.adjacency_list = {}
        self.edge_count = 0

    def add_node(self, node):
        # Implement this function
        self.adjacency_list[node] = []
        self.edge_count = 0

    def add_edge(self, node1, node2):
        # Implement this function
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
        self.edge_count += 1

    def has_edge(self, node1, node2):
        # Implement this function
        return node1 in self.adjacency_list and node2 in self.adjacency_list[node1]