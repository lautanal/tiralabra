import pygame
from math import sqrt
from timeit import default_timer as timer
from node import Node
from map import Map


# IDA* -algoritmi
def idastar(map, start, goal, diagonal, animate):
    tstart = timer()
    if diagonal:
        map.neighbors_diag()
        map.heuristic_manhattan(goal)
    else:
        map.neighbors_xy()
        map.heuristic_euclidian(goal)

    threshold = start.heuristic
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        map.init_costsums()
        start.costsum = 0
        path = [start]
        costsum = idastar_search(map, goal, path, threshold, diagonal, animate)

        if costsum == float("inf"):
            return False, 0, 0, 0
        elif costsum < 0:
            tend = timer()
            print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
            ida_path(path, start, goal)
            npath = len(path) - 2
            costsum = -costsum
            if not diagonal:
                costsum = costsum - goal.cost
            return True, npath, costsum, tend-tstart
        else:
            threshold = costsum


# Etsintä-rutiini
def idastar_search(map, goal, path, threshold, diagonal, animate):
    node = path[-1]
    costsum = node.costsum
    node.set_visited(animate)
    if animate:
        map.drawnode(node)

    if node == goal:
        return -costsum

    estimate = costsum + node.heuristic
    if estimate > threshold:
        return estimate

    tmin = float("inf")
    for neighbor in node.neighbors:
        if neighbor not in path:
            deltacost = neighbor.cost
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2+(node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
            newcostsum = costsum + deltacost

            if newcostsum < neighbor.costsum:
                neighbor.costsum = newcostsum
                path.append(neighbor)
                res = idastar_search(map, goal, path, threshold, diagonal, animate)
                if res < 0:
                    return res
                elif res < tmin:
                    tmin = res
                path.pop()

    return tmin


# Polun track, IDA*
def ida_path(path, start, goal):
    for node in path:
        if node != start and node != goal:
            node.mark_path()
