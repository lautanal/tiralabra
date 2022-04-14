import pygame
from math import sqrt
from timeit import default_timer as timer
from queue import PriorityQueue


# IDA* -algoritmi
def idastar(map, diagonal, animate):
    tstart = timer()

    # Naapurit ja heuristiikka
    if diagonal:
        map.neighbors_diag()
        map.heuristic_euclidian(map.goal)
    else:
        map.neighbors_xy()
        map.heuristic_manhattan(map.goal)

    # Alustukset
    map.init_costsums()
    map.start.costsum = 0
    threshold = map.start.heuristic
    paths = PriorityQueue()
    paths.put((0, [map.start]))

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
            res = idastar_search(path, threshold, map.goal, newpaths, diagonal, animate, map.drawnode)

            # Maali löytyi
            if res < 0:
                return True, timer() - tstart

            # Uusi hakukynnys
            elif res < tmin:
                tmin = res

        # Uudet hakupolut ja uusi kynnys
        paths = newpaths
        threshold = tmin


    # Reittiä ei löytynyt
    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, 0


# Syvyysetsintä-rutiini
def idastar_search(path, threshold, goal, paths, diagonal, animate, drawfunc):
    node = path[-1]
    costsum = node.costsum

    # Animaatio
    if animate:
        node.set_visited(animate)
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
