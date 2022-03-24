import numpy as np
from queue import PriorityQueue
from math import sqrt
from timeit import default_timer as timer
from path import get_path

# DIJKSTRA XY-SUUNNAT

def dijkstra_traditional(map,istart,jstart,iend,jend):
    tstart = timer()
    ysize = map.shape[0]
    xsize = map.shape[1]
# Taulukkojen alustus
    distance = [[999999999]*xsize for _ in range(ysize)]
    distance[istart][jstart] = map[istart,jstart]
    previous = [[(0,0)]*xsize for _ in range(ysize)]
    visited = [[False]*xsize for _ in range(ysize)]
    paths = PriorityQueue()
# Aloitus
    i,j = istart, jstart
    count = 0
    nsteps = 0
    while True:
        count += 1
# Seuraavat mahdolliset pisteet
        if i < ysize - 1 and not visited[i+1][j]:
            next_xy(i,j,i+1,j,map,distance,previous,paths,nsteps)
        if i > 0  and not visited[i-1][j]:
            next_xy(i,j,i-1,j,map,distance,previous,paths,nsteps)
        if j < xsize - 1 and not visited[i][j+1]:
            next_xy(i,j,i,j+1,map,distance,previous,paths,nsteps)
        if j > 0  and not visited[i][j-1]:
            next_xy(i,j,i,j-1,map,distance,previous,paths,nsteps)
        visited[i][j] = True
# Seuraava lyhimmän matkan piste
        if paths.empty():
            return -1,nsteps,count,[]
        d,nsteps,i,j = paths.get()
# Maali
        if i == iend and j == jend:
            tend = timer()
            print(f'Laskenta vei {tend-tstart:.3f} sekuntia')
            break
    return distance[iend][jend], nsteps, count, get_path(previous,istart,jstart,iend,jend)

def next_xy(i,j,inext,jnext,map,distance,previous,paths,nsteps):
        dnew = distance[i][j] + map[inext,jnext]
        if dnew < distance[inext][jnext]:
            distance[inext][jnext] = dnew
            previous[inext][jnext] = (i,j)
            paths.put((dnew,nsteps+1,inext,jnext))



# DIJKSTRA DIAGONAALISUUNNAT

def dijkstra_diagonal(map,istart,jstart,iend,jend):
    tstart = timer()
    ysize = map.shape[0]
    xsize = map.shape[1]
# Taulukoiden alustus
    distance = [[float('inf')]*xsize for _ in range(ysize)]
    distance[istart][jstart] = 0.0
    previous = [[(0,0)]*xsize for _ in range(ysize)]
    visited = [[False]*xsize for _ in range(ysize)]
    paths = PriorityQueue()
# Aloitus
    i,j = istart, jstart
    count = 0
    nsteps = 0
    while True:
        count += 1
# Seuraavat mahdolliset pisteet
        if i < ysize - 1 and not visited[i+1][j]:
            next_diag(i,j,i+1,j,map,distance,previous,paths,nsteps)
            if j < xsize - 1 and not visited[i+1][j+1]:
                next_diag(i,j,i+1,j+1,map,distance,previous,paths,nsteps)
            if j > 0 and not visited[i+1][j-1]:
                next_diag(i,j,i+1,j-1,map,distance,previous,paths,nsteps)
        if i > 0 and not visited[i-1][j]:
            next_diag(i,j,i-1,j,map,distance,previous,paths,nsteps)
            if j < xsize - 1 and not visited[i-1][j+1]:
                next_diag(i,j,i-1,j+1,map,distance,previous,paths,nsteps)
            if j > 0 and not visited[i-1][j-1]:
                next_diag(i,j,i-1,j-1,map,distance,previous,paths,nsteps)
        if j < xsize - 1 and not visited[i][j+1]:
                next_diag(i,j,i,j+1,map,distance,previous,paths,nsteps)
        if j > 0 and not visited[i][j-1]:
                next_diag(i,j,i,j-1,map,distance,previous,paths,nsteps)
        visited[i][j] = True
# Seuraava lyhimmän matkan piste
        if paths.empty():
            return -1, nsteps, count, []
        d,nsteps,i,j = paths.get()
# Maali
        if i == iend and j == jend:
            tend = timer()
            print(f'Laskenta vei {tend-tstart:.3f} sekuntia')
            break
    return distance[iend][jend], nsteps, count, get_path(previous,istart,jstart,iend,jend)

def next_diag(i,j,inext,jnext,map,distance,previous,paths,nsteps):
    if inext == i or jnext == j:
        dnew = distance[i][j] + (map[i,j] + map[inext,jnext]) / 2.0
    else:
        dnew = distance[i][j] + (map[i,j] + map[inext,jnext]) / sqrt(2.0)
    if dnew < distance[inext][jnext]:
        distance[inext][jnext] = dnew
        previous[inext][jnext] = (i,j)
        paths.put((dnew,nsteps+1,inext,jnext))

