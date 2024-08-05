import random


def nakljucnaLihaSt():
    nums = []
    while len(nums) != 10:
        rand = random.randint(1, 100)
        if rand % 2 != 0:
            nums.append(rand)

    return nums


def nakljucnaLihaStMat():
    nums = []
    for i in range(10):
        rand = random.randint(1, 50)
        lihost = rand * 2 - 1
        nums.append(lihost)

    return nums


print(nakljucnaLihaSt())
print(nakljucnaLihaStMat())
