tabela = [-6,10,17,12,-5,20,50,10,12,20]

print(tabela[4]) #[-5]
print(tabela[5:8]) #20,50,10
print(tabela[2:]) # 17,12,-5,20,50,10,12,20
print(tabela[:3]) # -6,10,17
print(tabela[4:4]) # []
print(len(tabela)) #10
print(tabela[-5:-1]) # [20, 50, 10, 12]
print(tabela[-1:-5]) # []
print(len(tabela[3:4])) #4
tabela.insert(4, 20)
print(tabela) #[-6, 10, 17, 12, 20, -5, 20, 50, 10, 12, 20]
tabela.remove(10)
print(tabela) #[-6, 17, 12, 20, -5, 20, 50, 10, 12, 20]