file = open("primer.txt", "w")
file.write("To je nasa prva datoteka. Danes je torek. \n")

file = open("primer.txt", "a")
file.write("Nase drugo besedilo.")



file = open("primer.txt", "r")
print(file.read())
#file.seek(0)

file = open("primer.txt", "r")
print(file.readline())
#file.seek(0)

file = open("primer.txt", "r")
print(file.readlines())

file.close()