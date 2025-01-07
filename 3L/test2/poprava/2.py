"""""
def izracunaj(a,n):
    if n == 0:
        return 1
    else:
        return a * izracunaj(a,n-1)

print(izracunaj(2,5))
"""""
#sled
izracunaj(2,5)
2*izracunaj(2,4)
2*2*izracunaj(2,3)
2*2*2*izracunaj(2,2)
2*2*2*2*izracunaj(2,1)
2*2*2*2*2*izracunaj(2,0)
2*2*2*2*2*1=32