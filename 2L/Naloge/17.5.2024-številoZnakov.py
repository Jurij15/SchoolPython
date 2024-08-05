import re
print(len(re.sub("[abcdefghijklmnoprstuvz]", "", input("vnesi stevilo: ").lower())))

n = int(input("vnesi stevilo: "))
stevec = 0
while n>0:
    stevec += 1
    n=n//10
print(stevec)