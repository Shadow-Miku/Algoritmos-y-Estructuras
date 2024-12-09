# Clase que representa un nodo de la lista enlazada
class Node:
    def __init__(self, value):
        self.value = value  # Valor almacenado en el nodo
        self.next = None    # Puntero al siguiente nodo, inicialmente None


# Clase que representa la lista enlazada
class LinkedList:
    def __init__(self):
        self.head = None  # Primer nodo de la lista
        self.tail = None  # Último nodo de la lista

    # Método para añadir un nodo al final de la lista
    def append(self, value):
        new_node = Node(value)  # Crear un nuevo nodo
        if not self.head:       # Si la lista está vacía
            self.head = new_node  # El nuevo nodo será el primer nodo
            self.tail = new_node  # Y también el último nodo
        else:
            self.tail.next = new_node  # Enlazar el último nodo actual con el nuevo nodo
            self.tail = new_node       # Actualizar el último nodo a ser el nuevo nodo

    # Método para añadir un nodo al inicio de la lista
    def prepend(self, value):
        new_node = Node(value)     # Crear un nuevo nodo
        new_node.next = self.head  # Enlazar el nuevo nodo con el primer nodo actual
        self.head = new_node       # Actualizar el primer nodo a ser el nuevo nodo
        if not self.tail:          # Si la lista estaba vacía, el nuevo nodo es también el último nodo
            self.tail = new_node

    # Método para eliminar un nodo con un valor específico
    def remove(self, value):
        if not self.head:  # Si la lista está vacía, no hay nada que eliminar
            return

        # Caso especial: si el nodo a eliminar es el primero
        if self.head.value == value:
            self.head = self.head.next  # Mover el primer nodo al siguiente
            if not self.head:          # Si ahora la lista está vacía, también actualizar la cola
                self.tail = None
            return

        # Buscar el nodo a eliminar
        iterator = self.head
        while iterator.next:
            if iterator.next.value == value:  # Si encontramos el nodo a eliminar
                iterator.next = iterator.next.next  # Saltar el nodo actual
                if not iterator.next:  # Si el nodo eliminado era el último, actualizar la cola
                    self.tail = iterator
                return
            iterator = iterator.next  # Pasar al siguiente nodo

    # Método para recorrer e imprimir los valores de la lista
    def iterate(self):
        iterator = self.head  # Iniciar desde el primer nodo
        while iterator:       # Mientras haya un nodo actual
            print(iterator.value + " ")  # Imprimir el valor del nodo
            iterator = iterator.next     # Avanzar al siguiente nodo


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una nueva lista enlazada
    ll = LinkedList()

    # Añadir nodos al final de la lista
    ll.append("A")
    ll.append("B")
    ll.append("C")

    # Añadir un nodo al inicio de la lista
    ll.prepend("Start")

    # Mostrar los elementos de la lista
    print("Lista inicial:")
    ll.iterate()

    # Eliminar un nodo
    ll.remove("B")

    # Mostrar los elementos de la lista después de eliminar
    print("\nLista después de eliminar 'B':")
    ll.iterate()
