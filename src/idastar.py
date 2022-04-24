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
        True, time (Tuple): Palauttaa arvon True, jos reitti löytyi ja laskentaan kuluneen ajan
    """
    tstart = timer()

    # Naapurit ja heuristiikka
    if diagonal:
        map.neighbors_diag()
        map.heuristic_euclidian(map.goal)
    else:
        map.neighbors_xy()
        map.heuristic_manhattan(map.goal)

    # Alustukset
    map.start.costsum = 0
    threshold = map.start.heuristic
    paths = []
    heappush(paths, (0, [map.start]))

    while paths:
        # Edetään polkuja kunnes kynnys ylittyy
        tmin = float("inf")
        newpaths = []
        while paths:
            est, path = heappop(paths)
            res = idastar_search(path, threshold, map.goal, newpaths, diagonal, animate, drawnode)

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


def idastar_search(path, threshold, goal, paths, diagonal, animate, drawnode):
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

    # Animaatio
    if animate:
        node.set_visited(animate)
        drawnode(node)

    # Maali löytyi
    if node == goal:
        return -1

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
            # Vino reitti
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2 + \
                    (node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
            newcostsum = costsum + deltacost

            # Jatketaan syvyyshakua
            if newcostsum < neighbor.costsum:
                neighbor.costsum = newcostsum
                neighbor.previous = node
                path.append(neighbor)
                res = idastar_search(path, threshold, goal, paths, diagonal, animate, drawnode)
                if res < 0:
                    return res
                elif res < tmin:
                    tmin = res
                path.pop()

    return tmin
