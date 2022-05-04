from math import sqrt
from timeit import default_timer as timer
from heapq import heappush, heappop


def idastar(map, diagonal, animate, drawnode):
    """IDA* -algoritmi

    Attributes:
        map: Karttaruudukko
        diagonal: Polun tyyppi (diagonal / xy)
        animate: Animaatio päällä
        drawnode: Karttaruudun piirtofunktio

    Returns:
        True: Palauttaa arvon True, jos reitti löytyi
        time: laskentaan kulunut aika
    """
    tstart = timer()

    # Naapurit ja heuristiikka
    if diagonal:
        map.neighbors_diag()
        map.heuristic_euclidian(map.goal)
#       map.heuristic_chebyshev(map.goal)
    else:
        map.neighbors_xy()
        map.heuristic_manhattan(map.goal)

    # Alustukset
    map.start.costsum = 0
    threshold = map.start.heuristic
    paths = []
    heappush(paths, (0, [map.start]))
    drawcount = 0
    update = False

    # Hakulooppi
    while paths:
        # Edetään polkuja kunnes kynnys ylittyy
        tmin = float("inf")
        newpaths = []
        while paths:
            path = heappop(paths)[1]
            if drawcount < 50:
                update = False
                drawcount += 1
            else:
                update = True
                drawcount = 0

            # Syvyyshaku kynnykseen asti
            res = idastar_search(path, threshold, map.goal, newpaths, diagonal, animate, drawnode, update)

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
    return False, timer() - tstart


def idastar_search(path, threshold, goal, paths, diagonal, animate, drawnode, update):
    """IDA* -syvyyshakurutiini

    Attributes:
        path: Polku ruutuun
        threshold: Etsintäkynnys
        goal: Maaliruutu
        paths: Etsintäpolut
        diagonal: Polun tyyppi (diagonal / xy)
        animate: Animaatio päällä
        drawnode: Karttaruudun piirtofunktio

    Returns:
        tmin: Uusi kynnysarvo etsinnälle
    """
    node = path[-1]
    costsum = node.costsum

    # Maali löytyi
    if node == goal:
        return -1

    # Animaatio
    node.set_visited()
    if animate:
        drawnode(node, update)

    # Hakukynnys ylittyi
    estimate = costsum + node.heuristic
    if estimate > threshold:
        heappush(paths, (estimate, path.copy()))
        return estimate

    # Käydään läpi naapurit
    tmin = float("inf")
    for neighbor in node.neighbors:
        if neighbor not in path:
            deltacost = neighbor.cost
            # Viisto polku
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2 + \
                    (node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
            newcostsum = costsum + deltacost

            # Jatketaan syvyyshakua
            if newcostsum < neighbor.costsum:
                neighbor.costsum = newcostsum
                neighbor.previous = node
                path.append(neighbor)
                res = idastar_search(path, threshold, goal, paths, diagonal, animate, drawnode, update)
                if res < 0:
                    return res
                elif res < tmin:
                    tmin = res
                path.pop()

    return tmin
