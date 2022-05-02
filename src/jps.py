from math import sqrt
from heapq import heappush, heappop
from timeit import default_timer as timer


def jps(map, animate, drawnode):
    """JPS -algoritmi

    Attributes:
        map: Karttaruudukko
        animate: Animaatio päällä
        drawnode: Karttaruudun piirtofunktio

    Returns:
        True: Palauttaa arvon True, jos reitti löytyi
        time: Laskentaan kulunut aika
        nn: Polun solmujen lukumäärä
        dist: Polun pituus
        path: Polun jump point pisteet
    """
    tstart = timer()

    # Heuristiikka
    map.heuristic_euclidian(map.goal)
#        map.heuristic_chebyshev(map.goal)

    # Alkuasetukset
    queue = []
    heappush(queue, (0, map.start, (1,0), 0, 0, [map.start]))
    heappush(queue, (0, map.start, (1,1), 0, 0, [map.start]))
    heappush(queue, (0, map.start, (0,1), 0, 0, [map.start]))
    heappush(queue, (0, map.start, (-1,1), 0, 0, [map.start]))
    heappush(queue, (0, map.start, (-1,0), 0, 0, [map.start]))
    heappush(queue, (0, map.start, (-1,-1), 0, 0, [map.start]))
    heappush(queue, (0, map.start, (0,-1), 0, 0, [map.start]))
    heappush(queue, (0, map.start, (1,-1), 0, 0, [map.start]))

    # Prioriteettijono-looppi
    while queue:
        # Seuraava solmu keosta
        est, node, dir, nn, dist, path = heappop(queue)
#        print(f'ROW: {node.row} COL: {node.col} NN: {nn} DIST:{dist}')

        # Maali löytyi
        if node == map.goal:
            return True, timer() - tstart, nn, dist, path

        # Reitti on jo käyty
        if node.check_visited_jps(dir):
            continue

        # Eri suuntien skannaukset
        if dir == (1,0) or dir == (-1,0):
            search_horizontal(map, node, dir[0], nn, dist, path, queue)
        elif dir == (0,1) or dir == (0,-1):  
            search_vertical(map, node, dir[1], nn, dist, path, queue)
        else:
            search_diagonal(map, node, dir, nn, dist, path, queue)

        # Animaatio
        node.set_visited_jps(dir, animate)
        if animate:
            drawnode(node)

    # Reittiä ei löytynyt
    tend = timer()
    print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

    return False, timer() - tstart, 0, 0, 0


def search_horizontal(map, node0, hor_dir, nn, dist, path, queue): 
    """ Horisontaalietsintä
    """ 

    row0 = node0.row
    col0 = node0.col

    # Skannauslooppi
    while True: 
        col1 = col0 + hor_dir
        # Ulkona kartalta
        if not map.on_map(row0, col1):
            return False

        # Este        
        node1 = map.nodes[row0][col1]
        if node1.blocked: 
            return False

        # Lisätään käsiteltävä solmu reitille
        path = path.copy()
        path.append(node1)

        # Maali
        if node1 == map.goal:
            heappush(queue, (dist+1, node1, (hor_dir, 0), nn, dist+1, path))
            return True 

        # Skannataan eteenpäin
        nn += 1        
        dist += 1
        col2 = col1 + hor_dir 
        jumppoint = False

        # Tarkistetaan, onko jump point        
        if map.on_map(row0-1, col2) and not map.nodes[row0-1][col2].blocked and map.nodes[row0-1][col1].blocked:
            jumppoint = True
#            node1.visited = True
            heappush(queue, (dist+node1.heuristic, node1, (hor_dir, -1), nn, dist, path))
        
        if map.on_map(row0+1, col2) and not map.nodes[row0+1][col2].blocked and map.nodes[row0+1][col1].blocked:
            jumppoint = True
#           node1.visited = True
            heappush(queue, (dist+node1.heuristic, node1, (hor_dir, 1), nn, dist, path))
        
        if jumppoint:
            heappush(queue, (dist+node1.heuristic, node1, (hor_dir, 0), nn, dist, path))
            return True

        # Seuraava ruutu            
        col0 = col1


def search_vertical(map, node0, vert_dir, nn, dist, path, queue): 
    """ Vertikaalietsintä
    """ 

    row0 = node0.row
    col0 = node0.col

    # Skannauslooppi
    while True: 
        row1 = row0 + vert_dir

        # Ulkona kartalta
        if not map.on_map(row1, col0):
            return False
        
        node1 = map.nodes[row1][col0]

        # Este
        if node1.blocked: 
            return False

        # Lisätään käsiteltävä solmu reitille
        path = path.copy()
        path.append(node1)

        # Maali
        if node1 == map.goal:
            heappush(queue, (dist+1, node1, (vert_dir, 0), nn, dist+1, path))
            return True 

        # Skannataan eteenpäin
        nn += 1        
        dist += 1
        row2 = row1 + vert_dir 
        jumppoint = False

        # Tarkistetaan, onko jump point        
        if map.on_map(row2, col0-1) and not map.nodes[row2][col0-1].blocked and map.nodes[row1][col0-1].blocked:
            jumppoint = True
#            node1.visited = True
            heappush(queue, (dist+node1.heuristic, node1, (-1, vert_dir), nn, dist, path))
        
        if map.on_map(row2, col0+1) and not map.nodes[row2][col0+1].blocked and map.nodes[row1][col0+1].blocked:
            jumppoint = True
#            node1.visited = True
            heappush(queue, (dist+node1.heuristic, node1, (1, vert_dir), nn, dist, path))
        
        if jumppoint:
            heappush(queue, (dist+node1.heuristic, node1, (0, vert_dir), nn, dist, path))
            return True

        # Seuraava ruutu            
        row0 = row1


def search_diagonal(map, node0, dir, nn, dist, path, queue): 
    """ Diagonaalietsintä.
    """ 

    row0 = node0.row
    col0 = node0.col
    hor_dir = dir[0]
    vert_dir = dir[1]

    # Skannauslooppi
    while True: 
        row1 = row0 + vert_dir 
        col1 = col0 + hor_dir

        # Ulkona kartalta       
        if not map.on_map(row1, col1):
            return False 

        node1 = map.nodes[row1][col1]

        # Este        
        if node1.blocked: 
            return False 

        # Lisätään käsiteltävä solmu reitille
        path = path.copy()
        path.append(node1)

        # Maali
        if node1 == map.goal:
            heappush(queue, (dist+sqrt(2), node1, (hor_dir, 0), nn, dist+sqrt(2), path))
            return True

        # Skannataan eteenpäin
        nn += 1        
        dist += sqrt(2)
        col2 = col1 + hor_dir
        row2 = row1 + vert_dir 

        # Pakotetut naapurit        
        if map.on_map(row2, col0) and not map.nodes[row2][col0].blocked and map.nodes[row1][col0].blocked:
            heappush(queue, (dist+node1.heuristic, node1, (-hor_dir, vert_dir), nn, dist, path))
        
        if map.on_map(row0, col2) and not map.nodes[row0][col2].blocked and map.nodes[row0][col1].blocked:
            heappush(queue, (dist+node1.heuristic, node1, (hor_dir, -vert_dir), nn, dist, path))

        # Horisontaali- ja vertikaaliskannaus        
        hsearch = search_horizontal(map, node1, hor_dir, nn, dist, path, queue)
        vsearch = search_vertical(map, node1, vert_dir, nn, dist, path, queue)

        # Jump point löytyi
        if hsearch or vsearch:
#            node1.visited = True
            heappush(queue, (dist+node1.heuristic, node1, (hor_dir, vert_dir), nn, dist, path))
            return True

        # Seuraava ruutu
        row0 = row1
        col0 = col1
