N = int(input("Vnesi st:"))
vsota = 0
"""
for i in range(N):
    ocena = int(input("Vnesi oceno:"))
    vsota = vsota + ocena
"""

counter = 0 
while(counter < N):
    ocena = int(input("Vnesi oceno:"))
    vsota = vsota + ocena
    counter = counter +1 

povprecje =  vsota/N
print(povprecje)