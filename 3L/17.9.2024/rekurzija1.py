def fakulteta(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakulteta(n - 1)

n=int(input("Vnesi stevilo n: "))
print(fakulteta(n))