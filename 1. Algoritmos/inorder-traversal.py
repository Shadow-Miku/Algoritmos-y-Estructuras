class Node:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None    # Referencia al hijo izquierdo
        self.right = None   # Referencia al hijo derecho

class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol

    def inorder_traversal(self, node, result=None):
        """
        Realiza un recorrido en orden (inorder) en un árbol binario.

        Parámetros:
        node (Node): Nodo actual en el recorrido.
        result (list): Lista para almacenar los valores en el orden recorrido.

        Retorna:
        list: Lista de valores en orden.
        """
        if result is None:
            result = []

        if node:
            # Recorrer el subárbol izquierdo
            self.inorder_traversal(node.left, result)

            # Procesar el nodo actual
            result.append(node.value)

            # Recorrer el subárbol derecho
            self.inorder_traversal(node.right, result)

        return result

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un árbol binario
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Recorrido en orden (Inorder Traversal):")
    result = tree.inorder_traversal(tree.root)
    print(result)