class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Inserta un nuevo nodo en el árbol
        if not self.root:
            self.root = Node(value)
            return

        temp = self.root
        while temp:
            if value < temp.value:
                if temp.left is None:
                    temp.left = Node(value)
                    return
                else:
                    temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = Node(value)
                    return
                else:
                    temp = temp.right
            else:
                return

    def search(self, value):
        # Busca un nodo con un valor específico
        temp = self.root
        while temp:
            if value == temp.value:
                return temp
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return None

    def inorder_traversal(self, node, result=None):
        # Recorrido en orden (inorder): izquierda, raíz, derecha
        if result is None:
            result = []

        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def find_min(self):
        # Encuentra el valor mínimo en el árbol
        if not self.root:
            return None
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.value

    def find_max(self):
        # Encuentra el valor máximo en el árbol
        if not self.root:
            return None
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp.value

    def delete(self, value):
        # Elimina un nodo con el valor especificado
        def _delete_recursive(node, value):
            if not node:
                return node

            if value < node.value:
                node.left = _delete_recursive(node.left, value)
            elif value > node.value:
                node.right = _delete_recursive(node.right, value)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                min_larger_node = self._find_min_node(node.right)
                node.value = min_larger_node.value
                node.right = _delete_recursive(node.right, min_larger_node.value)

            return node

        self.root = _delete_recursive(self.root, value)

    def _find_min_node(self, node):
        # Encuentra el nodo con el valor mínimo a partir de un nodo dado
        while node.left:
            node = node.left
        return node


# Ejemplo de uso
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insertar valores
    bst.insert(45)
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.insert(10)
    bst.insert(35)
    bst.insert(55)
    bst.insert(75)
    bst.insert(85)


    print("\nRecorrido en orden (Inorder):")
    print(bst.inorder_traversal(bst.root))

    print("\nBuscar valor 40:")
    node = bst.search(40)
    print(f"Encontrado: {node.value}" if node else "No encontrado")

    print("\nValor mínimo en el árbol:")
    print(bst.find_min())

    print("\nValor máximo en el árbol:")
    print(bst.find_max())

    print("\nEliminar nodo con valor 70:")
    bst.delete(70)
    print(bst.inorder_traversal(bst.root))
