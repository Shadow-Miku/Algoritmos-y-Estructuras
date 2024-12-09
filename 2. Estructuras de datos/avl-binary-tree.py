import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Altura del nodo para balanceo

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if not node:
            return AVLNode(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        else:
            return node  # Valor duplicado no permitido

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balance = self.get_balance(node)

        # Rotaciones
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def inorder_traversal(self, node):
        if not node:
            return []
        return self.inorder_traversal(node.left) + [node.value] + self.inorder_traversal(node.right)

    def display(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(-10, 10)
        ax.set_ylim(0, 10)
        
        def plot_node(node, x, y, dx):
            if not node:
                return

            ax.text(x, y, str(node.value), fontsize=12, ha='center', va='center', 
                    bbox=dict(boxstyle='circle', edgecolor='black', facecolor='white'))

            if node.left:
                ax.plot([x, x - dx], [y - 1, y - 2], 'k-')
                plot_node(node.left, x - dx, y - 2, dx / 2)

            if node.right:
                ax.plot([x, x + dx], [y - 1, y - 2], 'k-')
                plot_node(node.right, x + dx, y - 2, dx / 2)

        plot_node(self.root, 0, 10, 5)
        plt.axis('off')
        plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 32, 28, 24, 26, 5, 7, 8]

    for value in values:
        avl.root = avl.insert(avl.root, value)

    print("Recorrido en orden (Inorder):")
    print(avl.inorder_traversal(avl.root))

    print("\nÁrbol AVL mostrado gráficamente:")
    avl.display()
