#vsota prvih n naravnih stevil
#n=7 ... 1+2+3+4+5+6+7 ... ?

def izracun(n):
    if  n == 1:
        return 1
    else:
        return n+izracun(n-1)

n = int(input("vnesi stevilo N:"))
print(izracun(n))