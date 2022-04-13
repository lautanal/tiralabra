# Minimikeko

class Bheap:
    def __init__(self, size):
        self.heap = [None] * (size+1)
        self.size = 0
        self.maxsize = size + 1

    # Tarkistus, onko tyhjä keko
    def empty(self):
        return self.size == 0

    # Uuden alkion talletus kekoon
    def put(self, value):
        if self.size + 1 == self.maxsize:
            return
        self.heap[self.size + 1] = value
        self.size += 1
        self.heapify_put(self.size)

    # Pienin alkio ulos keosta
    def get(self):
        if self.size == 0:
            return None
        else:
            res = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.heap[self.size] = None
            self.size -= 1
            self.heapify_get(1)
            return res

    # Korjataan keon rakenne minimikeoksi (put)
    def heapify_put(self, index):
        parent = index // 2
        if index <= 1:
            return
        if self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
        self.heapify_put(parent)

    # Korjataan keon rakenne minimikeoksi (get)
    def heapify_get(self, index):
        left = index * 2
        right = index * 2 + 1
        swap = 0

        if self.size < left:
            return
        elif self.size == left:
            if self.heap[index] > self.heap[left]:
                self.swap(index, left)
            return

        else:
            if self.heap[left] < self.heap[right]:
                swap = left
            else:
                swap = right
            if self.heap[index] > self.heap[swap]:
                self.swap(index, swap)
        self.heapify_get(swap)

    # Solmujen paikan vaihto
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
