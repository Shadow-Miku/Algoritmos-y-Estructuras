class MaxHeap:
    def __init__(self):
        self.heap = []

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    @staticmethod
    def _get_left_child_index(index):
        return (index * 2) + 1

    @staticmethod
    def _get_right_child_index(index):
        return (index * 2) + 2

    @staticmethod
    def _get_parent_index(index):
        return (index - 1) // 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0 and self.heap[index] > self.heap[self._get_parent_index(index)]:
            self._swap(index, self._get_parent_index(index))
            index = self._get_parent_index(index)