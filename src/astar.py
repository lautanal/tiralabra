import pygame
from math import sqrt
from queue import PriorityQueue
from timeit import default_timer as timer
from node import Node
from map import Map

# A* -algoritmi
def astar(map, start, goal, diagonal, animate):
    tstart = timer()

    # Naapurit ja heuristiikka
    if diagonal:
        map.neighbors_diag()
        map.heuristic_euclidian(goal)
    else:
        map.neighbors_xy()
        map.heuristic_manhattan(goal)

    # Alkuasetukset
    start.costsum = 0
    prqueue = PriorityQueue()
    prqueue.put((0, 0, start))
    count = 0

    # Prioriteettijono-looppi
    while not prqueue.empty():
        # Keskeytys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Seuraava solmu keosta
        node = prqueue.get()[2]

        # Maali löytyi
        if node == goal:
            return True, timer() - tstart

        # Naapurit
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
                prqueue.put((newcostsum + neighbor.heuristic, count, neighbor))

        # Animaatio
        node.set_visited(animate)
        if animate:
            map.drawnode(node)

    # Reittiä ei löytynyt
    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, 0, 0, 0
