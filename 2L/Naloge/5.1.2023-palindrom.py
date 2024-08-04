#ANA
import re

def ObrniNiz(s):
    returnvalue = ""
    counter = len(s)
    while (counter > 0):
        returnvalue += s[counter-1]
        counter -=1
    return returnvalue

def aliJePalindrom(s):
    obrni = ObrniNiz(s)
    
    if(obrni == s):
        return True
    
    return False

print(aliJePalindrom(input("vnesi string: ")))