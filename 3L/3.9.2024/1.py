# napisi podprogram lihaSt, ki bo vstavil 10 celih števil v polje in ga napolnil zgolj z lihimi števili od 1 do 100
# program naj nastalo polje izpiše

import random


def randomLihoStevilo():
    x = random.randint(1, 100)
    while x % 2 == 0:
        x = random.randint(1, 100)

    return x


def lihaSt(y = []):
    for i in range(0, 10):
        y.append(randomLihoStevilo())

    return y;


x = lihaSt()

print(x)
