# Clase que representa un nodo en una lista doblemente enlazada
class Node:
    def __init__(self, data):
        self.data = data  # Valor almacenado en el nodo
        self.prev = None  # Puntero al nodo anterior (inicia como None)
        self.next = None  # Puntero al nodo siguiente (inicia como None)


# Clase que implementa una lista doblemente enlazada
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Primer nodo de la lista
        self.tail = None  # Último nodo de la lista

    # Método para añadir un nodo al final de la lista
    def append(self, data):
        new_node = Node(data)  # Crear un nuevo nodo
        if self.tail is None:  # Si la lista está vacía
            self.head = new_node  # El nuevo nodo será el primero
            self.tail = new_node  # Y también el último
            return
        self.tail.next = new_node  # Enlazar el último nodo con el nuevo nodo
        new_node.prev = self.tail  # El nuevo nodo apunta al anterior como su predecesor
        self.tail = new_node       # Actualizar la cola al nuevo nodo

    # Método para añadir un nodo al inicio de la lista
    def prepend(self, data):
        new_node = Node(data)  # Crear un nuevo nodo
        if self.head is None:  # Si la lista está vacía
            self.head = new_node  # El nuevo nodo será el primero
            self.tail = new_node  # Y también el último
            return
        self.head.prev = new_node  # El nodo actual apunta al nuevo nodo como su predecesor
        new_node.next = self.head  # El nuevo nodo apunta al nodo actual como su sucesor
        self.head = new_node       # Actualizar la cabeza al nuevo nodo

    # Método para eliminar un nodo con un valor específico
    def delete(self, key):
        current_node = self.head  # Comenzar desde el primer nodo
        while current_node:
            if current_node.data == key:  # Si el valor del nodo coincide con el buscado
                if current_node.prev:  # Si no es el primer nodo
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next  # Actualizar la cabeza si es el primer nodo
                if current_node.next:  # Si no es el último nodo
                    current_node.next.prev = current_node.prev
                if current_node == self.tail:  # Si es el último nodo
                    self.tail = current_node.prev  # Actualizar la cola
                return
            current_node = current_node.next  # Avanzar al siguiente nodo

    # Método para imprimir la lista de izquierda a derecha
    def print_list(self):
        current_node = self.head  # Comenzar desde la cabeza
        while current_node:
            print(current_node.data, end=" ")  # Imprimir el valor del nodo
            current_node = current_node.next  # Avanzar al siguiente nodo
        print()


# Clase derivada que añade funcionalidad de un cursor a la lista
class CursorDLL(DoublyLinkedList):
    def __init__(self):
        super().__init__()  # Inicializar la lista base
        self.cursor = self.head  # Inicializar el cursor en la cabeza

    # Mover el cursor al nodo siguiente
    def move_cursor_forward(self):
        if self.cursor is None or self.cursor.next is None:  # Verificar límites
            return
        self.cursor = self.cursor.next

    # Mover el cursor al nodo anterior
    def move_cursor_backward(self):
        if self.cursor is None or self.cursor.prev is None:  # Verificar límites
            return
        self.cursor = self.cursor.prev

    # Imprimir la lista, destacando el nodo donde está el cursor
    def print_list_with_cursor(self):
        current_node = self.head  # Comenzar desde la cabeza
        while current_node:
            if current_node == self.cursor:  # Si el nodo actual es el del cursor
                print("[{}]".format(current_node.data), end=" ")  # Destacar el nodo
            else:
                print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    # Sobrescribir el método para añadir un nodo al final e inicializar el cursor si es necesario
    def append(self, data):
        super().append(data)  # Usar el método de la clase base
        if self.cursor is None:  # Si el cursor no está inicializado
            self.cursor = self.tail

    # Sobrescribir el método para añadir un nodo al inicio e inicializar el cursor si es necesario
    def prepend(self, data):
        super().prepend(data)  # Usar el método de la clase base
        if self.cursor is None:  # Si el cursor no está inicializado
            self.cursor = self.head


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una lista doblemente enlazada con cursor
    dll = CursorDLL()

    # Añadir nodos
    dll.append("A")
    dll.append("B")
    dll.append("C")

    # Imprimir la lista con el cursor
    print("Lista inicial con cursor:")
    dll.print_list_with_cursor()

    # Mover el cursor y mostrar la lista
    dll.move_cursor_forward()
    print("\nCursor movido adelante:")
    dll.print_list_with_cursor()

    # Mover el cursor hacia atrás y mostrar la lista
    dll.move_cursor_backward()
    print("\nCursor movido atrás:")
    dll.print_list_with_cursor()

    # Eliminar un nodo y mostrar la lista
    dll.delete("B")
    print("\nLista después de eliminar 'B':")
    dll.print_list_with_cursor()
