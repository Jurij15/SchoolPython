import random

N = int(input("vnesi stevilo metov: "))
meti = []

for i in range(N):
    kocka1 = random.randint(1,6)
    kocka2 = random.randint(1,6)
    vsota = kocka1 + kocka2
    meti.append(vsota)

st7=0
for i in meti:
    if i>= 7:
        st7 += 1
print(st7)
print(meti)