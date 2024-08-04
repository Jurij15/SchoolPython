import re

def OdstraniSodeZnake(X):
    ToReturn = X
    for i in range(0, len(X)):
        if(i%2 != 0):
            ToReturn = ToReturn.replace(X[i], "")
    
    return ToReturn

print(OdstraniSodeZnake(input("vnesi string: ")))