number = int(input("Enter a number... "))

counter = 1

if(number % 2 == 0):
    number = number / 2
else:
    number = number * 2

while(counter <= number):
    print(counter)
    counter += 1