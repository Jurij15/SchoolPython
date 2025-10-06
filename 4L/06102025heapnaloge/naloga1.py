import heapq

nums = [5,1,9,3]
heapq.heapify(nums)

while nums:
    print(heapq.heappop(nums))