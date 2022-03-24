from tokenize import Hexnumber
import numpy as np
from queue import PriorityQueue
from math import sqrt
from timeit import default_timer as timer
from path import get_path

# A* XY-SUUNNAT

def astar_xy(map,istart,jstart,iend,jend,heuristic):
    tstart = timer()
    ysize = map.shape[0]
    xsize = map.shape[1]
# Taulukkojen alustus
    cost = [[999999999]*xsize for _ in range(ysize)]                                # Etäisyydet
    cost[istart][jstart] = map[istart,jstart]
    previous = [[(0,0)]*xsize for _ in range(ysize)]                                # Edelliset paikat
    visited = [[False]*xsize for _ in range(ysize)]                                 # Vierailut
    paths = PriorityQueue()                                                         # Työjono
# Aloitus
    i,j = istart, jstart
    count = 0
    nsteps = 0
    while True:
        count += 1
# Seuraavat mahdolliset ruudut
        if i < ysize - 1 and not visited[i+1][j]:                                   # Alas
            next_xy(i,j,i+1,j,iend,jend,map,cost,previous,paths,nsteps,heuristic)
        if i > 0  and not visited[i-1][j]:                                          # Ylös         
            next_xy(i,j,i-1,j,iend,jend,map,cost,previous,paths,nsteps,heuristic)
        if j < xsize - 1 and not visited[i][j+1]:                                   # Oikealle
            next_xy(i,j,i,j+1,iend,jend,map,cost,previous,paths,nsteps,heuristic)
        if j > 0  and not visited[i][j-1]:                                          # Vasemmalle
            next_xy(i,j,i,j-1,iend,jend,map,cost,previous,paths,nsteps,heuristic)
        visited[i][j] = True
# Reittiä ei löytynyt
        if paths.empty():
            return -1,nsteps,count,[]
# Seuraava reitin ruutu
        d,nsteps,i,j = paths.get()
# Maali
        if i == iend and j == jend:
            tend = timer()
            print(f'Laskenta vei {tend-tstart:.3f} sekuntia')
            break
    return cost[iend][jend], nsteps, count, get_path(previous,istart,jstart,iend,jend)

# Ruudun tietojen talletus priorityjonoon, xy-siirrot
def next_xy(i,j,inext,jnext,iend,jend,map,cost,previous,paths,nsteps,heuristic):
    newcost = cost[i][j] + map[inext,jnext]
    if newcost < cost[inext][jnext]:
        cost[inext][jnext] = newcost
        previous[inext][jnext] = (i,j)
        fcost= newcost + heuristic(inext,jnext,iend,jend)
        paths.put((fcost,nsteps+1,inext,jnext))


# DIJKSTRA DIAGONAALISUUNNAT

def astar_diagonal(map,istart,jstart,iend,jend,heuristic):
    tstart = timer()
    ysize = map.shape[0]
    xsize = map.shape[1]
# Taulukoiden alustus
    cost = [[float('inf')]*xsize for _ in range(ysize)]
    cost[istart][jstart] = 0.0
    previous = [[(0,0)]*xsize for _ in range(ysize)]
    visited = [[False]*xsize for _ in range(ysize)]
    paths = PriorityQueue()
# Aloitus
    i,j = istart, jstart
    count = 0
    nsteps = 0
    while True:
        count += 1
# Seuraavat mahdolliset ruudut
        if i < ysize - 1 and not visited[i+1][j]:                                           # Alas
            next_diag(i,j,i+1,j,iend,jend,map,cost,previous,paths,nsteps,heuristic)
            if j < xsize - 1 and not visited[i+1][j+1]:                                     # Alas oikealle
                next_diag(i,j,i+1,j+1,iend,jend,map,cost,previous,paths,nsteps,heuristic)
            if j > 0 and not visited[i+1][j-1]:                                             # Alas vasemmalle
                next_diag(i,j,i+1,j-1,iend,jend,map,cost,previous,paths,nsteps,heuristic)
        if i > 0 and not visited[i-1][j]:                                                   # Ylös
            next_diag(i,j,i-1,j,iend,jend,map,cost,previous,paths,nsteps,heuristic)
            if j < xsize - 1 and not visited[i-1][j+1]:                                     # Ylös oikealle
                next_diag(i,j,i-1,j+1,iend,jend,map,cost,previous,paths,nsteps,heuristic)
            if j > 0 and not visited[i-1][j-1]:                                             # Ylös vasemmalle
                next_diag(i,j,i-1,j-1,iend,jend,map,cost,previous,paths,nsteps,heuristic)
        if j < xsize - 1 and not visited[i][j+1]:                                           # Oikealle
                next_diag(i,j,i,j+1,iend,jend,map,cost,previous,paths,nsteps,heuristic)
        if j > 0 and not visited[i][j-1]:                                                   # Vasemmalle
                next_diag(i,j,i,j-1,iend,jend,map,cost,previous,paths,nsteps,heuristic)
        visited[i][j] = True
# Reittiä ei löytynyt
        if paths.empty():
            return -1, nsteps, count, []
# Seuraava reitin ruutu
        d,nsteps,i,j = paths.get()
# Maali
        if i == iend and j == jend:
            tend = timer()
            print(f'Laskenta vei {tend-tstart:.3f} sekuntia')
            break
    return cost[iend][jend], nsteps, count, get_path(previous,istart,jstart,iend,jend)

# Ruudun tietojen talletus priorityjonoon, diagonaalisiirrot
def next_diag(i,j,inext,jnext,iend,jend,map,cost,previous,paths,nsteps,heuristic):
    if inext == i or jnext == j:
        newcost = cost[i][j] + (map[i,j] + map[inext,jnext]) / 2.0
    else:
        newcost = cost[i][j] + (map[i,j] + map[inext,jnext]) / sqrt(2.0)
    if newcost < cost[inext][jnext]:
        cost[inext][jnext] = newcost
        previous[inext][jnext] = (i,j)
        fcost= newcost + heuristic(inext,jnext,iend,jend)
        paths.put((fcost,nsteps+1,inext,jnext))

# Manhattan heuristiikka
def manhattan(i1,j1,i2,j2):
	return abs(i1 - i2) + abs(j1 - j2)

# Euklidiininen heuristiikka
def euclidian(i1,j1,i2,j2):
	return sqrt((i1 - i2)**2 + (j1 - j2)**2)
