side = 8
rowCounter = 0

while rowCounter < side:
    columnCounter = 0
    while columnCounter < side:
        if (rowCounter + columnCounter) % 2 == 0:
            print(" * ", end="")
        else:
            print(" 0 ", end="")
        columnCounter += 1
    rowCounter += 1
    print("")
