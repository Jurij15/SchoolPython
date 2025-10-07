import heapq


def combine(lists):
    combined = []
    heapq.heapify(combined)
    for array in lists:
        heapq.heapify(array)
        combined = heapq.merge(combined, array)

    return list(combined)

print(combine([[1,4,7], [2,5,8], [3,6,9]]))