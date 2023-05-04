imput = int(input("Enter a number "))

counter = 0

while(counter <= imput):
    if(counter % 2 == 0): #stevilo JE sodo
        print("*"*counter)
    else:
        print(counter)
    counter += 1
    print()