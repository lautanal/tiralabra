import pygame
from math import sqrt
from queue import PriorityQueue
from heapq import heappush, heappop
from timeit import default_timer as timer

# A* -algoritmi
def astar(map, diagonal, animate):
    tstart = timer()

    # Naapurit ja heuristiikka
    if diagonal:
        map.neighbors_diag()
        map.heuristic_euclidian(map.goal)
    else:
        map.neighbors_xy()
        map.heuristic_manhattan(map.goal)

    # Alkuasetukset
    map.start.costsum = 0
    prqueue = []
    heappush(prqueue, (0, 0, map.start))
#    prqueue = PriorityQueue()
#    prqueue.put((0, 0, start))
    count = 0

    # Prioriteettijono-looppi
#    while not prqueue.empty():
    while prqueue:
        # Keskeytys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Seuraava solmu keosta
        node = heappop(prqueue)[2]
#        node = prqueue.get()[2]

        # Maali löytyi
        if node == map.goal:
            return True, timer() - tstart

        # Käydään läpi naapurit
        for neighbor in node.neighbors:
            deltacost = neighbor.cost
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2+(node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
            newcostsum = node.costsum + deltacost

            # Parempi reitti löytyi
            if not neighbor.visited and newcostsum < neighbor.costsum:
                count += 1
                neighbor.previous = node
                neighbor.costsum = newcostsum
                heappush(prqueue,(newcostsum + neighbor.heuristic, count, neighbor))

        # Animaatio
        node.set_visited(animate)
        if animate:
            map.drawnode(node)

    # Reittiä ei löytynyt
    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, 0
