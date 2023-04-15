# Program, ki izracuna ploscino kroga z uporabo math lib

import math

radius = float(input("Vnesi polmer kroga: "))

ploscina = math.pi * math.pow(radius, 2)

print("Ploscina danega kroga je:", ploscina)