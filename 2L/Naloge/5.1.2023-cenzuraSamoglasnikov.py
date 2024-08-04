import re

def CenzuraSamoglasnikov(X):
    return re.sub("[A,E,I,O,U]", "#", X)

print(CenzuraSamoglasnikov(input("vnesi string: ")))