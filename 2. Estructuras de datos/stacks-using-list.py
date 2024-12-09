class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0
    
    def push(self, item):
        """Añade un elemento al tope de la pila."""
        self.items.append(item)
    
    def pop(self):
        """Remueve y devuelve el elemento en el tope de la pila."""
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        """Devuelve el elemento en el tope sin removerlo."""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.items)
    
    def __str__(self):
        """Devuelve una representación en cadena de la pila."""
        return str(self.items)

# Ejemplo de uso:
stack = Stack()

print("Pila vacía:", stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print("Estado de la pila:", stack)
print("Elemento en el tope:", stack.peek())
print("Tamaño de la pila:", stack.size())
print("Eliminando el elemento del tope:", stack.pop())
print("Estado de la pila después de pop:", stack)
print("Elemento en el tope después de pop:", stack.peek())
