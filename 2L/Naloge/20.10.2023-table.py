t = [-3,100,15,-14,-50,73,-100]

for i in range(0, len(t)):
    for y in range(0,len(t)):
        if(t[i] < t[y]):
            temp = t[i]
            t[i] = t[y]
            t[y] = temp

print(t)