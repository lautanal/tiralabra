from math import sqrt
from timeit import default_timer as timer
from bheap import Bheap


def dijkstra(map, diagonal, animate, drawnode):
    """Dijkstran algoritmi

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

    # Naapurit
    if diagonal:
        map.neighbors_diag()
    else:
        map.neighbors_xy()

    # Alkuasetukset
    map.start.costsum = 0
    bheap = Bheap(map.nrows*map.ncols)
    bheap.put((0, 0, map.start))
    count = 0
    drawcount = 0

    # Binäärikeko-looppi
    while not bheap.empty():
        # Seuraava solmu keosta
        node = bheap.get()[2]

        # Maali löytyi
        if node == map.goal:
            return True, timer() - tstart

        # Käydään läpi naapurit
        for neighbor in node.neighbors:
            deltacost = neighbor.cost
            # Vino reitti
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2 + \
                    (node.col - neighbor.col)**2) * (node.cost + neighbor.cost) / 2
            newcostsum = node.costsum + deltacost

            # Löytyi parempi reitti
            if not neighbor.visited and newcostsum < neighbor.costsum:
                count += 1
                neighbor.previous = node
                neighbor.costsum = newcostsum
                bheap.put((newcostsum, count, neighbor))

        # Merkitään solmu käsitellyksi
        node.set_visited()

        # Animaatio
        if animate:
            if drawcount < 200:
                drawcount += 1
                drawnode(node, False)
            else:
                drawnode(node, True)
                drawcount = 0

    # Polkua ei löytynyt
    return False, timer() - tstart
