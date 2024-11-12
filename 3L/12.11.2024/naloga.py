with open("STEVILA.txt", "r") as file, open("pozitivna_stevila.txt", "w") as pozitivna_stevila:
    stevila = file.readlines()

    for i in stevila:
        if int(i)>0:
            pozitivna_stevila.write(i)
