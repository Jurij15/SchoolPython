side = 5
rowCounter = 0

SpecialColumnCounter = 0
while(SpecialColumnCounter < side):
    print(" X", end="")
    SpecialColumnCounter += 1
SpecialColumnCounter = 0

rowCounter += 1
while rowCounter < side:
    columnCounter = 0
    while columnCounter < side:
        if(rowCounter != 1):
            if(columnCounter == 0):
                print(" X", end="")
            elif(columnCounter == 4):
                print(" X", end="")
            else:
                print(" O", end="")
        columnCounter += 1
    rowCounter += 1
    print("")

while(SpecialColumnCounter < side):
    print(" X", end="")
    SpecialColumnCounter += 1
SpecialColumnCounter = 0