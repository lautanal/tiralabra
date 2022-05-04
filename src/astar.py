from math import sqrt
from heapq import heappush, heappop
from timeit import default_timer as timer


def astar(map, diagonal, animate, drawnode):
    """A* -algoritmi

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

    # Alkuasetukset
    map.start.costsum = 0
    queue = []
    heappush(queue, (0, 0, map.start))
    count = 0
    drawcount = 0

    # Prioriteettijono-looppi
    while queue:
        # Seuraava solmu keosta
        node = heappop(queue)[2]
        drawcount += 1

        # Maali löytyi
        if node == map.goal:
            return True, timer() - tstart

        # Käydään läpi naapurit
        for neighbor in node.neighbors:
            deltacost = neighbor.cost
            # Vino reitti
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2 + \
                    (node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
            newcostsum = node.costsum + deltacost

            # Parempi reitti löytyi
            if not neighbor.visited and newcostsum < neighbor.costsum:
                count += 1
                neighbor.previous = node
                neighbor.costsum = newcostsum
                heappush(queue,(newcostsum + neighbor.heuristic, count, neighbor))

        # Merkitään solmu käsitellyksi
        node.set_visited()

        # Animaatio
        if animate:
            if drawcount < 200:
                drawnode(node, False)
            else:
                drawnode(node, True)
                drawcount = 0

    # Reittiä ei löytynyt
    return False, timer() - tstart
