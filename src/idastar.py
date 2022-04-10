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

    map.init_costsums()
    start.costsum = 0
    threshold = start.heuristic
    paths = [[start]]
    while paths:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        thrmin = float("inf")
        newpaths = []
        for path in paths:
            thrnew = idastar_search(path, threshold, goal, newpaths, diagonal, animate, map.drawnode)
            if thrnew < 0:
                tend = timer()
                print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
                npath = track_path(start, goal)
                costsum = goal.costsum
                if not diagonal:
                    costsum = costsum - goal.cost
                return True, npath, costsum, tend-tstart
            elif thrnew < thrmin:
                thrmin = thrnew
        threshold = thrmin
        paths = newpaths

    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, 0, 0, 0


# Syvyysetsintä-rutiini
def idastar_search(path, threshold, goal, paths, diagonal, animate, drawfunc):
    node = path[-1]
    costsum = node.costsum
    node.set_visited(animate)
    if animate:
        drawfunc(node)

    if node == goal:
        return -1

    estimate = costsum + node.heuristic
    if estimate > threshold:
        paths.append(path.copy())
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
                neighbor.previous = node
                path.append(neighbor)
                res = idastar_search(path, threshold, goal, paths, diagonal, animate, drawfunc)
                if res < 0:
                    return res
                elif res < tmin:
                    tmin = res
                path.pop()

    return tmin


# Polun track
def track_path(start, goal):
    node = goal.previous
    count = 0
    while node != start:
        count += 1
        node.mark_path()
        node = node.previous
    return count
