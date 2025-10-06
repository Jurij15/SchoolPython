import heapq


def najvecjih_k(seznam, k):
    return heapq.nlargest(k, seznam)

print(najvecjih_k([1, 2, 3, 4, 5], 3))