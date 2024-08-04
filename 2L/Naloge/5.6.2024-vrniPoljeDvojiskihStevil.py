import random

def toBinary(x):
    stevilo = ""
    y =x
    while y != 0:
        if y%2!=0:
            stevilo += "1"
        else:
            stevilo += "0"

        y = y//2

    stevilo = stevilo[::-1]

    return  stevilo

def vrniPoljeDvojiskihStevil(st = []):
    bin = []
    for i in st:
        bin.append(toBinary(i))
    return  bin

stevila = []
for i in range(100):
    stevila.append(random.randint(1,1024))

#print(vrniPoljeDvojiskihStevil(stevila))

counter = 0
while True:
    orig = random.randint(1,1024)
    num = toBinary(orig)
    with open("binary.txt", "a") as file:
        file.write(f"{orig} : {num}\n")
    counter += 1
    print(counter)