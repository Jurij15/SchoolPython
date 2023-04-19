# Program, ki izrise pravokotni trikotnik iz zvezdic, na podlagi visine, ki jo vpise uporabnik

visina = int(input("Vnesi visino trikotnika: "))

RowCounter = 1

while RowCounter <= visina:

    ColumnCounter = 1
    while ColumnCounter <= RowCounter:
        print("* ", end="")
        ColumnCounter = ColumnCounter + 1

    print()
    RowCounter = RowCounter + 1
