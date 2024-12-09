class MaxHeap:
    def __init__(self):
        self.heap = []  # Lista para almacenar los elementos del heap

    def insert(self, value):
        # Insertar un nuevo valor en el heap
        self.heap.append(value)  # Agregar al final
        self._heapify_up(len(self.heap) - 1)  # Restaurar la propiedad del heap

    def extract_max(self):
        # Eliminar y retornar el valor máximo (raíz)
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Mover el último elemento a la raíz
        self._heapify_down(0)  # Restaurar la propiedad del heap
        return max_value

    def _heapify_up(self, index):
        # Restaurar la propiedad del heap hacia arriba
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            # Intercambiar si el nodo actual es mayor que su padre
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        # Restaurar la propiedad del heap hacia abajo
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            # Intercambiar y continuar hacia abajo
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def peek(self):
        # Retorna el valor máximo sin eliminarlo
        return self.heap[0] if self.heap else None

    def display(self):
        # Muestra los elementos del heap
        print("Heap content:", self.heap)

# Ejemplo de uso
if __name__ == "__main__":
    max_heap = MaxHeap()

    # Insertar elementos
    max_heap.insert(20)
    max_heap.insert(15)
    max_heap.insert(30)
    max_heap.insert(10)
    max_heap.insert(40)

    print("\nContenido del heap después de insertar elementos:")
    max_heap.display()

    print("\nElemento máximo (peek):")
    print(max_heap.peek())

    print("\nExtraer el máximo:")
    print(max_heap.extract_max())
    max_heap.display()

    print("\nExtraer el máximo nuevamente:")
    print(max_heap.extract_max())
    max_heap.display()
