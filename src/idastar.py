import pygame
from math import sqrt
from timeit import default_timer as timer
from queue import PriorityQueue
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
    paths = PriorityQueue()
    paths.put((0, 1, [start]))
    while not paths.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        thrmin = float("inf")
        newpaths = PriorityQueue()
        while not paths.empty():
            costsum, plen, path  = paths.get()
            res = idastar_search(path, costsum, threshold, goal, newpaths, diagonal, animate, map.drawnode)
            if res < 0:
                tend = timer()
                print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
                ida_path(path, start, goal)
                npath = len(path) - 2
                costsum = goal.costsum
                if not diagonal:
                    costsum = costsum - goal.cost
                return True, npath, costsum, tend-tstart
            elif res < thrmin:
                thrmin = res
        threshold = thrmin
        paths = newpaths

    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, 0, 0, 0


# Syvyysetsintä-rutiini
def idastar_search(path, costsum, threshold, goal, paths, diagonal, animate, drawfunc):
    node = path[-1]
    node.set_visited(animate)
    if animate:
        drawfunc(node)

    if node == goal:
        return -1

    estimate = costsum + node.heuristic
    if estimate > threshold:
        paths.put((costsum, len(path), path.copy()))
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
                res = idastar_search(path, newcostsum, threshold, goal, paths, diagonal, animate, drawfunc)
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



# Polun track, IDA*
def ida_path(path, start, goal):
    for node in path:
        if node != start and node != goal:
            node.mark_path()
