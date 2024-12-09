class HashMap:
    def __init__(self, size=10):
        self.size = size  # Tamaño del array subyacente
        self.map = [None] * self.size  # Array para almacenar cadenas

    def _hash(self, key):
        # Genera un índice basado en la clave
        return hash(key) % self.size

    def insert(self, key, value):
        # Inserta un par clave-valor en el mapa hash
        index = self._hash(key)
        if self.map[index] is None:
            self.map[index] = []  # Inicializa una lista para manejar colisiones
        
        # Actualiza el valor si la clave ya existe
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Si no existe, agrega un nuevo par clave-valor
        self.map[index].append([key, value])

    def get(self, key):
        # Recupera el valor asociado a una clave
        index = self._hash(key)
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        # Elimina un par clave-valor
        index = self._hash(key)
        if self.map[index] is not None:
            for i, pair in enumerate(self.map[index]):
                if pair[0] == key:
                    self.map[index].pop(i)
                    return True
        return False

    def display(self):
        # Muestra el contenido del mapa hash
        for i, bucket in enumerate(self.map):
            if bucket:
                print(f"Index {i}: {bucket}")
            else:
                print(f"Index {i}: Empty")

# Ejemplo de uso
if __name__ == "__main__":
    hashmap = HashMap()

    # Insertar pares clave-valor
    hashmap.insert("name", "Alice")
    hashmap.insert("age", 25)
    hashmap.insert("city", "New York")
    hashmap.insert("job", "Engineer")

    print("\nMapa hash después de insertar elementos:")
    hashmap.display()

    # Recuperar valores
    print("\nRecuperar valores:")
    print("name:", hashmap.get("name"))
    print("age:", hashmap.get("age"))

    # Actualizar un valor
    print("\nActualizar valor de 'age':")
    hashmap.insert("age", 26)
    print("age:", hashmap.get("age"))

    # Eliminar un elemento
    print("\nEliminar elemento con clave 'city':")
    hashmap.delete("city")
    hashmap.display()

    # Intentar recuperar un elemento eliminado
    print("\nRecuperar clave eliminada 'city':")
    print("city:", hashmap.get("city"))
