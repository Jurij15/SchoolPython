a = int(input("vnesi a: "))
polovica = a/2

for i in range(0,a+1):
    if i != 0:
        if (a % i == 0) and (i < polovica):
            print(i)
