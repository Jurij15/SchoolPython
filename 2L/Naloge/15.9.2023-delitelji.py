for n in range(1,100):
    d = 1
    for delitelj in range(1, n):
        if n % delitelj == 0:
            d += 1
    print(str(n)+" ima "+ str(d) + " deliteljev")