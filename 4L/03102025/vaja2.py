#napiši funkcijo sortiraj_kopico, ki vrne seznam, urejen z uporabo kopice

import heapq

def sortiraj_kopico(seznam):
    heapq.heapify(seznam)
    return seznam

print(sortiraj_kopico([5,3,8,1]))