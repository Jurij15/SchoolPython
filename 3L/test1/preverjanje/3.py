import random

N= int(input("vnesi n: "))
A= int(input("vnesi a: "))
B= int(input("vnesi b: "))

seznam = []

for i in range(N):
    seznam.append(random.randint(A,B))

pozitivna = 0
negativna = 0
nicelne = 0

for i in seznam:
    if i >0:
        pozitivna+=1
    elif i < 0:
        negativna+=1
    else:
        nicelne+=1

print(pozitivna)
print(negativna)
print(nicelne)