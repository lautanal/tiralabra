import pygame
from math import sqrt
from queue import PriorityQueue
from timeit import default_timer as timer
from node import Node
from map import Map
from bheap import Bheap

# Dijkstran algoritmi
def dijkstra(map, start, goal, diagonal, animate):
    tstart = timer()

    # Naapurit
    if diagonal:
        map.neighbors_diag()
    else:
        map.neighbors_xy()

    # Alkuasetukset
    start.costsum = 0
    bheap = Bheap(map.nrows*map.ncols)
    bheap.put((0, 0, start))
    count = 0

    # Binäärikeko-looppi
    while not bheap.empty():
        # Keskeytys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Seuraava solmu keosta
        node = bheap.get()[2]

        # Maali löytyi
        if node == goal:
            return True, timer() - tstart

        # Käydään läpi naapurit
        for neighbor in node.neighbors:
            deltacost = neighbor.cost
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2 + (node.col - neighbor.col)**2) * (node.cost + neighbor.cost) / 2
            newcostsum = node.costsum + deltacost

            # Löytyi parempi reitti
            if not neighbor.visited and newcostsum < neighbor.costsum:
                count += 1
                neighbor.previous = node
                neighbor.costsum = newcostsum
                bheap.put((newcostsum, count, neighbor))

        # Animaatio
        node.set_visited(animate)
        if animate:
            map.drawnode(node)

    # Polkua ei löytynyt
    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, 0
