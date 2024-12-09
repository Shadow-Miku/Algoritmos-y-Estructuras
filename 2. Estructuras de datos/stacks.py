class Stack:
    def __init__(self):
        self.stack = []  # Lista para almacenar los elementos del stack

    def push(self, value):
        # Agrega un elemento al tope del stack
        self.stack.append(value)

    def pop(self):
        # Elimina y retorna el elemento del tope del stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        # Retorna el elemento del tope del stack sin eliminarlo
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        # Verifica si el stack está vacío
        return len(self.stack) == 0

    def display(self):
        # Muestra los elementos del stack
        print("Stack content (top to bottom):", self.stack[::-1])

# Ejemplo de uso
if __name__ == "__main__":
    stack = Stack()

    # Agregar elementos al stack
    stack.push(10)
    stack.push(30)
    stack.push(40)
    stack.push(20)
    stack.push(50)
  

    print("\nContenido del stack después de apilar elementos:")
    stack.display()

    print("\nElemento al tope del stack (peek):")
    print(stack.peek())

    print("\nDesapilar elementos:")
    while not stack.is_empty():
        print("Pop:", stack.pop())

    print("\nIntentar desapilar de un stack vacío:")
    stack.pop()
