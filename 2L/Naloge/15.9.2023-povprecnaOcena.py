TotalScores = int(input("Vnesi število ocen: "))
scores = 0

for i in range(TotalScores):
    scores += int(input("Vnesi število: "))
    
print(scores/TotalScores)