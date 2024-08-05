import random

nums = []
maximum = 0

for i in range(50):
    nums.append(random.randint(10, 1000))

for i in nums:
    if i > maximum:
        maximum = i

print(maximum)