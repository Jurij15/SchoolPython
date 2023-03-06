side = int(input("Enter a number..."))
counter = 0

while counter < side:
    columnCounter = 0
    while columnCounter < side:
        print("*", end="")
        columnCounter += 1
    counter += 1
    print("")
