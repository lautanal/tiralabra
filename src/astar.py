import pygame
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

    # Alkuasetukset
    map.start.costsum = 0
    queue = []
    heappush(queue, (0, 0, map.start))
    count = 0

    # Prioriteettijono-looppi
    while queue:
        # Keskeytys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Seuraava solmu keosta
        node = heappop(queue)[2]

        # Maali löytyi
        if node == map.goal:
            return True, timer() - tstart

        # Käydään läpi naapurit
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
                heappush(queue,(newcostsum + neighbor.heuristic, count, neighbor))

        # Animaatio
        node.set_visited(animate)
        if animate:
            drawnode(node)

    # Reittiä ei löytynyt
    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, 0
