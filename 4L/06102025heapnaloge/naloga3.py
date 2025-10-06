import heapq


class MaxHeap:
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)
        heapq.heapify(self.data)

    def extractMax(self):
        return self.data[len(self.data)-1]

    def peek(self):
        return self.data