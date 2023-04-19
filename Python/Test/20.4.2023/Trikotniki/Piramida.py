"""
    *
   * *
  * * *
 * * * *
* * * * * 
"""


visina = int(input("Vnesi visino: "))

RowCounter = 0

while RowCounter < visina:
    ColumnCounter = 0

    while ColumnCounter < visina:
        if ColumnCounter < visina - RowCounter - 1:
            print(" ", end="")
        else:
            print("* ", end="")
        ColumnCounter += 1

    print()
    RowCounter += 1