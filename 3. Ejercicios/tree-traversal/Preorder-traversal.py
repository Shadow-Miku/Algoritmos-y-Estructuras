class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal(node, result):
    # Verificar si el nodo es None. Si lo es, retornamos el resultado actual.
    if node is None:
        return result
    
    # Añadir el valor del nodo actual al resultado
    result.append(node.value)
    
    # Recursivamente realizar pre-order traversal en el subárbol izquierdo
    preorder_traversal(node.left, result)
    
    # Recursivamente realizar pre-order traversal en el subárbol derecho
    preorder_traversal(node.right, result)
    
    # Retornar el resultado con los valores en pre-order
    return result

# Ejemplo de uso
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = []
preorder_result = preorder_traversal(root, result)
print(preorder_result)  # Debería imprimir [1, 2, 4, 5, 3]
