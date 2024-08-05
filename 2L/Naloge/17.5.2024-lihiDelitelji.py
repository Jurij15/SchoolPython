a = int(input("vnesi a: "))

for i in range(0,a+1):
    if i != 0:
        if (a % i == 0) and (i % 2 != 0):
            print(i)
