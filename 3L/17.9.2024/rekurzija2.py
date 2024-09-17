#fibonacijevo zaporedje
#0,1,1,2,3,5,8,12,21

def fibonacci(n):
    if n == 0 or n == 1:
        return n #ničli člen je 0, prvi člen je 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Vnesi stevilo N:"))
print(fibonacci(n))