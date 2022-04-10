
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
        heuristic = euclidian
    else:
        map.neighbors_xy()
        heuristic = euclidian

    threshold = heuristic(start.get_pos(), goal.get_pos())
    while True:
        path = [start]		
        costsum = idastar_search(map, goal, path, 0, threshold, heuristic, diagonal, animate)

        if costsum == float("inf"):
            return False, 0, 0, 0
        elif costsum < 0:
            tend = timer()
            print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
            ida_path(path, start, goal)
            npath = len(path) - 2
            costsum = -costsum
            if not diagonal:
                costsum = costsum - goal.cost
            return True, npath, costsum, tend-tstart
        else:
            threshold = costsum

# Etsintä-rutiini
def idastar_search(map, goal, path, costsum, threshold, heuristic, diagonal, animate):
    node = path[-1]
    node.set_visited(animate)
    if animate:
        map.drawnode(node)

    if node == goal:
        return -costsum

    estimate = costsum + heuristic(node.get_pos(), goal.get_pos())
    if estimate > threshold:
        return estimate

    tmin = float("inf")
    for neighbor in node.neighbors:
        if neighbor not in path:
            deltacost = neighbor.cost
            if diagonal:
                deltacost = sqrt((node.row - neighbor.row)**2+(node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
            newcostsum = costsum + deltacost
            
            path.append(neighbor)
            res = idastar_search(map, goal, path, newcostsum, threshold, heuristic, diagonal, animate)
            if res < 0:
                return res
            elif res < tmin:
                tmin = res
            path.pop()

    return tmin

# Manhattan-heuristiikka
def manhattan(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Euklidiininen heuristiikka
def euclidian(p1,p2):
    y1, x1 = p1
    y2, x2 = p2
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Polun track, IDA*
def ida_path(path, start, goal):
    for node in path:
        if node != start and node != goal:
            node.mark_path()

