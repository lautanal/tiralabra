import pygame
from math import sqrt
from queue import PriorityQueue
from timeit import default_timer as timer
from node import Node
from map import Map


# A* -algoritmi
def astar(map, start, goal, diagonal, animate):
    tstart = timer()
    if diagonal:
        map.neighbors_diag()
        map.heuristic_manhattan(goal)
    else:
        map.neighbors_xy()
        map.heuristic_euclidian(goal)
    start.costsum = 0
    prqueue = PriorityQueue()
    prqueue.put((0, 0, start))
    count = 0

    while not prqueue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        node = prqueue.get()[2]
        if node == goal:
            tend = timer()
            print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
            npath = track_path(start, goal)
            costsum = node.costsum
            if not diagonal:
                costsum = node.costsum - node.cost
            return True, npath, costsum, tend-tstart

        for neighbor in node.neighbors:
            deltacost = neighbor.cost
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2+(node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
            newcostsum = node.costsum + deltacost
            if not neighbor.visited and newcostsum < neighbor.costsum:
                count += 1
                neighbor.previous = node
                neighbor.costsum = newcostsum
                prqueue.put((newcostsum + neighbor.heuristic, count, neighbor))

        node.set_visited(animate)

        if animate:
            map.drawnode(node)

    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, 0, 0, 0


# Polun track
def track_path(start, goal):
    node = goal.previous
    count = 0
    while node != start:
        count += 1
        node.mark_path()
        node = node.previous
    return count
