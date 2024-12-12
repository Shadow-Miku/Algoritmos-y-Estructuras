class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def postorder_traversal(node, result):
    # Verificar si el nodo actual no es None
    if node:
        # Recursivamente realizar post-order traversal en el subárbol izquierdo
        postorder_traversal(node.left, result)
        # Recursivamente realizar post-order traversal en el subárbol derecho
        postorder_traversal(node.right, result)
        # Añadir el valor del nodo actual al resultado
        result.append(node.value)
    # Retornar el resultado con los valores en post-order
    return result


# Ejemplo de uso
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = []
postorder_result = postorder_traversal(root, result)
print(postorder_result)  # Debería imprimir [4, 5, 2, 3, 1]
