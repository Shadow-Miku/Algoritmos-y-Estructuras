class Solution(object):
    def searchBST(self,root, val):   
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Otra solucion
""" class Solution(object):
    def searchBST(self, root, val):   
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None """

# Definición de un nodo del árbol 
class TreeNode(object): 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val 
        self.left = left 
        self.right = right 
        
# Ejemplo de creación de un BST 
root = TreeNode(4) 
root.left = TreeNode(2) 
root.right = TreeNode(7) 
root.left.left = TreeNode(1) 
root.left.right = TreeNode(3) 

# Crear una instancia de Solution y llamar al método
solution = Solution() 
result = solution.searchBST(root, 2) 
print(result.val if result else "Not found")