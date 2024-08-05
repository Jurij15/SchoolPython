n = int(input("Vnesi stevilo: "))

for i in range(n):
    row = " "
    for y in range(n):
        if (i == y):
            row += "1 "
        else:
            row += "0 "
            
    print(row)