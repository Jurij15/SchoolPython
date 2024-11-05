#napisi podprogram, ki ustvari datoteko stavki.txt
#in omogoča vnos besedila
#ter izpiše vsebino datoteke

##################################
#To je prvi stavek. TO je drugi  #
#stavek. To je tretji stavek. To #
#je četrti stavek                #
##################################

ime_dat = "stavki.txt"
#besedilo = input("vnesi besedilo: ")

with open(ime_dat, "w") as file:
    file.write("To je prvi stavek. TO je drugi \nstavek. To je tretji stavek. To \nje cetrti stavek \n")

with open(ime_dat, "a") as file:
    file.write(input("vnesi besedilo: "))

with open(ime_dat, "r") as file:
    print(file.read())