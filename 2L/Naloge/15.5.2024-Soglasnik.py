import re

def Soglasnik(s):
    res = re.findall("[AEIOUaieou]", s)
    if  len(res) > 0:
        return False
    else:
        return True

print(Soglasnik(input("vnesi char: ")))