#napiši funkcijo k_najmanjših(seznam, k), ki s pomočjo kopice poišče k najmajnjših števil
import heapq


def k_najmanjsih(seznam, k):
    return heapq.nsmallest(k, seznam)

print(k_najmanjsih([10,2,5,8,1,9], 3))