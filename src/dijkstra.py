import numpy as np
from queue import PriorityQueue
from math import sqrt
from timeit import default_timer as timer
from path import get_path

# Dijkstran metodi, vain vaaka- ja pystysuorat siirtymät
def dijkstra_traditional(map,istart,jstart,iend,jend,limit):
    tstart = timer()
    ysize = map.shape[0]
    xsize = map.shape[1]
# Taulukkojen alustus
    distance = [[999999999]*xsize for _ in range(ysize)]
    distance[istart][jstart] = map[istart,jstart]
    previous = [[(0,0)]*xsize for _ in range(ysize)]
    visited = [[False]*xsize for _ in range(ysize)]
    paths = PriorityQueue()

    i,j = istart, jstart
    count = 0
    nsteps = 0
    while True:
        count += 1
# Y-plus
        if i < ysize - 1 and not visited[i+1][j] and map[i+1,j] <= limit:
            dnew = distance[i][j] + map[i+1,j]
            if dnew < distance[i+1][j]:
                distance[i+1][j] = dnew
                paths.put((dnew,nsteps+1,i+1,j))
                previous[i+1][j] = (i,j)
# Y-minus
        if i > 0 and not visited[i-1][j] and map[i-1,j] <= limit:
            dnew = distance[i][j] + map[i-1,j]
            if dnew < distance[i-1][j]:
                distance[i-1][j] = dnew
                paths.put((dnew,nsteps+1,i-1,j))
                previous[i-1][j] = (i,j)
# X-plus
        if j < xsize - 1 and not visited[i][j+1] and map[i,j+1] <= limit:
            dnew = distance[i][j] + map[i,j+1]
            if dnew < distance[i][j+1]:
                distance[i][j+1] = dnew
                paths.put((dnew,nsteps+1,i,j+1))
                previous[i][j+1] = (i,j)
# X-minus
        if j > 0 and not visited[i][j-1] and map[i,j-1] <= limit:
            dnew = distance[i][j] + map[i,j-1]
            if dnew < distance[i][j-1]:
                distance[i][j-1] = dnew
                paths.put((dnew,nsteps+1,i,j-1))
                previous[i][j-1] = (i,j)

        visited[i][j] = True

        if paths.empty():
            return -1,nsteps,count,[]

        d,nsteps,i,j = paths.get()
        if i == iend and j == jend:
            tend = timer()
            print(f'Laskenta vei {tend-tstart:.3f} sekuntia')
            break

    return distance[iend][jend], nsteps, count, get_path(previous,istart,jstart,iend,jend)


# Dijkstran metodi, diagonaalisiirtymät sallittu
def dijkstra_diagonal(map,istart,jstart,iend,jend,limit):
    tstart = timer()
    ysize = map.shape[0]
    xsize = map.shape[1]
# Taulukoiden alustus
    distance = [[float('inf')]*xsize for _ in range(ysize)]
    distance[istart][jstart] = 0.0
    previous = [[(0,0)]*xsize for _ in range(ysize)]
    visited = [[False]*xsize for _ in range(ysize)]
    paths = PriorityQueue()

    i,j = istart, jstart
    count = 0
    nsteps = 0
    while True:
        count += 1
# Y-plus
        if i < ysize - 1 and not visited[i+1][j] and map[i+1,j] <= limit:
            dnew = distance[i][j] + (map[i,j] + map[i+1,j]) / 2.0
            if dnew < distance[i+1][j]:
                distance[i+1][j] = dnew
                paths.put((dnew,nsteps+1,i+1,j))
                previous[i+1][j] = (i,j)
# Diagonal directions
            if j < xsize - 1 and not visited[i+1][j+1] and map[i+1,j+1] <= limit:
                dnew = distance[i][j] + (map[i,j] + map[i+1,j+1]) / sqrt(2.0)
                if dnew < distance[i+1][j+1]:
                    distance[i+1][j+1] = dnew
                    paths.put((dnew,nsteps+1,i+1,j+1))
                    previous[i+1][j+1] = (i,j)
            if j > 0 and not visited[i+1][j-1] and map[i+1,j-1] <= limit:
                dnew = distance[i][j] + (map[i,j] + map[i+1,j-1]) / sqrt(2.0)
                if dnew < distance[i+1][j-1]:
                    distance[i+1][j-1] = dnew
                    paths.put((dnew,nsteps+1,i+1,j-1))
                    previous[i+1][j-1] = (i,j)
# Y-minus
        if i > 0 and not visited[i-1][j] and map[i-1,j] <= limit:
            dnew = distance[i][j] + (map[i,j] + map[i-1,j]) / 2.0
            if dnew < distance[i-1][j]:
                distance[i-1][j] = dnew
                paths.put((dnew,nsteps+1,i-1,j))
                previous[i-1][j] = (i,j)
# Diagonal directions
            if j < xsize - 1 and not visited[i-1][j+1] and map[i-1,j+1] <= limit:
                dnew = distance[i][j] + (map[i,j] + map[i-1,j+1]) / sqrt(2.0)
                if dnew < distance[i-1][j+1]:
                    distance[i-1][j+1] = dnew
                    paths.put((dnew,nsteps+1,i-1,j+1))
                    previous[i-1][j+1] = (i,j)
            if j > 0 and not visited[i-1][j-1] and map[i-1,j-1] <= limit:
                dnew = distance[i][j] + (map[i,j] + map[i-1,j-1]) / sqrt(2.0)
                if dnew < distance[i-1][j-1]:
                    distance[i-1][j-1] = dnew
                    paths.put((dnew,nsteps+1,i-1,j-1))
                    previous[i-1][j-1] = (i,j)
# X-plus
        if j < xsize - 1 and not visited[i][j+1] and map[i,j+1] <= limit:
            dnew = distance[i][j] + (map[i,j] + map[i,j+1]) / 2.0
            if dnew < distance[i][j+1]:
                distance[i][j+1] = dnew
                paths.put((dnew,nsteps+1,i,j+1))
                previous[i][j+1] = (i,j)
# X-minus
        if j > 0 and not visited[i][j-1] and map[i,j-1] <= limit:
            dnew = distance[i][j] + (map[i,j] + map[i,j-1]) / 2.0
            if dnew < distance[i][j-1]:
                distance[i][j-1] = dnew
                paths.put((dnew,nsteps+1,i,j-1))
                previous[i][j-1] = (i,j)

        visited[i][j] = True

        if paths.empty():
            return -1, nsteps, count, []

        d,nsteps,i,j = paths.get()
        if i == iend and j == jend:
            tend = timer()
            print(f'Laskenta vei {tend-tstart:.3f} sekuntia')
            break

    return distance[iend][jend], nsteps, count, get_path(previous,istart,jstart,iend,jend)

