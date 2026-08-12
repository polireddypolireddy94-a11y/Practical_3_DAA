class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] < self.heap[i]:
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                i = p
            else:
                break

    def delete(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        n = len(self.heap)

        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def peek(self):
        return self.heap[0] if self.heap else None

    def display(self):
        print(self.heap)


h = MaxHeap()

h.insert(10)
h.insert(40)
h.insert(15)
h.insert(50)
h.insert(100)
h.insert(20)

h.display()
print(h.peek())
print(h.delete())
h.display()
