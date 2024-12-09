class Node:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.next = None  # Referencia al siguiente nodo

class Queue:
    def __init__(self):
        self.front = None  # Nodo al frente de la cola
        self.back = None   # Nodo al final de la cola
        self.size = 0      # Tamaño de la cola

    def is_empty(self):
        # Verifica si la cola está vacía
        return self.size == 0

    def enqueue(self, value):
        # Agrega un nuevo elemento al final de la cola
        new_node = Node(value)
        if self.is_empty():
            self.front = self.back = new_node  # Ambos apuntan al nuevo nodo
        else:
            self.back.next = new_node  # El nodo actual en `back` apunta al nuevo nodo
            self.back = new_node       # Actualiza `back` al nuevo nodo
        self.size += 1

    def dequeue(self):
        # Elimina y retorna el elemento al frente de la cola
        if not self.is_empty():
            removed_item = self.front.value  # Guardar el valor a eliminar
            self.front = self.front.next     # Mover el frente al siguiente nodo
            self.size -= 1
            if self.is_empty():
                self.back = None  # Si la cola queda vacía, actualiza `back`
            return removed_item
        else:
            print("Queue is empty")
            return None

    def peek(self):
        # Retorna el elemento al frente de la cola sin eliminarlo
        if not self.is_empty():
            return self.front.value
        else:
            print("Queue is empty")
            return None

    def display(self):
        # Muestra los elementos de la cola
        current = self.front
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Queue contents:", " -> ".join(elements))

# Ejemplo de uso
if __name__ == "__main__":
    print_queue = Queue()

    # Agregar documentos a la cola
    print_queue.enqueue("Document1.pdf")
    print_queue.enqueue("Document2.pdf")
    print_queue.enqueue("Document3.pdf")

    print("\nContenido de la cola después de encolar:")
    print_queue.display()

    print("\nElemento al frente de la cola:")
    print(print_queue.peek())

    print("\nProcesando la cola:")
    while not print_queue.is_empty():
        document = print_queue.dequeue()
        print("Printing:", document)

    print("\nContenido de la cola después de vaciarla:")
    print_queue.display()
