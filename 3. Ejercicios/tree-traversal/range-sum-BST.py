class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def rangeSumBST(root, low, high):
    # Definición de la función interna 'inorder' para el recorrido en orden
    def inorder(node):
        if node:  # Si el nodo no es None
            inorder(node.left)  # Recorrer el subárbol izquierdo
            if low <= node.value <= high:  # Si el valor del nodo está dentro del rango
                nonlocal sum  # Permite modificar la variable 'sum' definida en el alcance superior
                sum += node.value  # Sumar el valor del nodo a la variable 'sum'
            inorder(node.right)  # Recorrer el subárbol derecho

    sum = 0  # Inicializar la suma en 0
    inorder(root)  # Iniciar el recorrido en orden desde la raíz
    return sum  # Devolver la suma total

# Creación del árbol BST de ventas
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Calcular la suma de las ventas en el rango [7, 15]
result = rangeSumBST(root, 7, 15)
print(result)  # Debería imprimir 32 (7 + 10 + 15)
