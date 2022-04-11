import pygame
from math import sqrt
from timeit import default_timer as timer
from queue import PriorityQueue
from node import Node
from map import Map


# IDA* -algoritmi
def idastar(map, start, goal, diagonal, animate):
    tstart = timer()

    # Naapurit ja heuristiikka
    if diagonal:
        map.neighbors_diag()
        map.heuristic_euclidian(goal)
    else:
        map.neighbors_xy()
        map.heuristic_manhattan(goal)

    # Alustukset
    map.init_costsums()
    start.costsum = 0
    threshold = start.heuristic
    paths = PriorityQueue()
    paths.put((0, [start]))

    while not paths.empty():
        # Keskeytys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Edetään polkuja kunnes kynnys ylittyy
        tmin = float("inf")
        newpaths = PriorityQueue()
        while not paths.empty():
            est, path = paths.get()
            res = idastar_search(path, threshold, goal, newpaths, diagonal, animate, map.drawnode)
            # Maali löytyi
            if res < 0:
                tend = timer()
                print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
                npath = track_path(start, goal)
                costsum = goal.costsum
                if not diagonal:
                    costsum = costsum - goal.cost
                return True, npath, costsum, tend-tstart
            # Uusi hakukynnys
            elif res < tmin:
                tmin = res
        threshold = tmin
        # Uudet polut
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

    # Maali
    if node == goal:
        return -1

    # Hakukynnys ylittyi
    estimate = costsum + node.heuristic
    if estimate > threshold:
        paths.put((estimate, path.copy()))
        return estimate

    # Käydään läpi naapurit
    tmin = float("inf")
    for neighbor in node.neighbors:
        if neighbor not in path:
            deltacost = neighbor.cost
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2+(node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
            newcostsum = costsum + deltacost

            # Jatketaan syvyyshakua
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


# Polun track, IDA*
def ida_path(path, start, goal):
    for node in path:
        if node != start and node != goal:
            node.mark_path()
