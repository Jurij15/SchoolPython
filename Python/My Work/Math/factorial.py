userNumber = int(input("Enter a number:"))
factorial = 1

while userNumber > 1:
    factorial *= userNumber
    userNumber -=1

print("Factorial:  ", factorial)