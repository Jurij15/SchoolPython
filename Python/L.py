lenght = int(input("Enter lenght: "))

RowCounter = 1
Counter2 = 1

while (RowCounter <= lenght):

    print("*")
    RowCounter += 1

    if (RowCounter == lenght):
        while (Counter2 <= lenght):
            print("* ", end="")
            Counter2 += 1

Counter2 = 1

while(Counter2 <= lenght):
    print("* ", end="")
    Counter2 += 1

RowCounter = 1

while(RowCounter <= lenght):
    print("* ")
    RowCounter += 1
