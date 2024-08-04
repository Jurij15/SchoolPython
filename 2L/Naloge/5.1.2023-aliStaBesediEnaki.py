import re

def AliStaBesediEnaki(X, Y):
    if(len(X) != len(Y) | len(Y) != len(X)):
        return False
    
    for i in range(len(X)):
        if X[i] == Y[i]:
            continue
        else:
            return False
        
    return True

print(AliStaBesediEnaki(input("Vnesi prvi string: "), input("Vnesi drugi string: ")))        