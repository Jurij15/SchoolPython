import random

def LihaST():
    t = []
    
    while len(t) != 10:
        ran = random.randint(1,100)
        
        if ran %2 != 0:
            t.append(ran)
            
LihaST()