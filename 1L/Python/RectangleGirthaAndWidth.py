#Import the Math library (for Square root)
import math

#Get the variables
InputA = int(input("Enter Rectangle Grith"))
InputB = int(input("Enter Rectanle Width"))

#calculate girth by A*2+B*2
Girth = InputA*2 + InputB*2
#calculate width by A*B
Width = InputA*InputB
#calculate hypotenuse by using the sqare root function in the math class
Hypotenuse = math.sqrt(InputA*InputA+InputB*InputB)

#print all the calculated variables and exit
print("Obseg: ",Girth, ";")
print("Ploščina: ", Width, ";")
print("Hipotenuza: ", Hypotenuse, ";")