class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(node, result):
    # Verificar si el nodo es None. Si lo es, retornamos el resultado actual.
    if node is None:
        return result
    
    # Recursivamente realizar in-order traversal en el subárbol izquierdo
    result = inorder_traversal(node.left, result)
    
    # Añadir el valor del nodo actual al resultado
    result.append(node.value)
    
    # Recursivamente realizar in-order traversal en el subárbol derecho
    result = inorder_traversal(node.right, result)
    
    # Retornar el resultado con los valores en orden
    return result

# Ejemplo de uso
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = []
inorder_result = inorder_traversal(root, result)
print(inorder_result)  # Debería imprimir [4, 2, 5, 1, 3]
