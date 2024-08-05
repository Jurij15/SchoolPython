import random

nums = []
last = 0

for i in range(100):
    nums.append(random.randint(10, 100))

last = nums[len(nums)-1]

for i in nums:
    if i > last:
        print(i)