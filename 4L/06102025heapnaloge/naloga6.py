import heapq


def k_najmanjsih(seznam, k):
    smallest = heapq.nsmallest(k, seznam)
    return smallest[k-1]

print(k_najmanjsih([7,10,4,3,20,15], 3))