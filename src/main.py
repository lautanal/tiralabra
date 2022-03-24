import numpy as np
from map import generate_map
from dijkstra import dijkstra_xy, dijkstra_diagonal
from astar import astar_xy, astar_diagonal, manhattan, euclidian
from plotmap import plot_map

def maproute():
# Luodaan kartta
    ysize = 100
    xsize = 100
    levels = 10
    map = generate_map(ysize,xsize,levels)

# Reitin alku- ja loppupisteet
    istart = 0
    jstart = 0
    iend = ysize-1
    jend = xsize-1

# Dijsktran menetelmä
    print('\nDijkstra xy-siirrot')
    wdist,nsteps,iters,path1 = dijkstra_xy(map,istart,jstart,iend,jend)
    if wdist > 0:
        print('Iteraatiot: ', iters)
        print('Polun pituus:', nsteps)
        print(f'Polun painotettu pituus: {wdist}')
    else:
        print('Iteraatiot: ', iters)
        print('Ei ratkaisua')

# Dijkstra diagonal
    print('\nDijkstra diagonal-siirrot')
    wdist,nsteps,iters,path2 = dijkstra_diagonal(map,istart,jstart,iend,jend)
    if wdist > 0:
        print('Iteraatiot: ', iters)
        print('Polun pituus:', nsteps)
        print(f'Polun painotettu pituus: {wdist:.1f}')
    else:
        print('Iteraatiot: ', iters)
        print('Ei ratkaisua')

# A* menetelmä xy
    heuristic = manhattan
    print('\nA* xy-siirrot')
    wdist,nsteps,iters,path3 = astar_xy(map,istart,jstart,iend,jend, heuristic)
    if wdist > 0:
        print('Iteraatiot: ', iters)
        print('Polun pituus:', nsteps)
        print(f'Polun painotettu pituus: {wdist}')
    else:
        print('Iteraatiot: ', iters)
        print('Ei ratkaisua')

# A* diagonal
    print('\nA* diagonal-siirrot')
    wdist,nsteps,iters,path4 = astar_diagonal(map,istart,jstart,iend,jend, heuristic)
    if wdist > 0:
        print('Iteraatiot: ', iters)
        print('Polun pituus:', nsteps)
        print(f'Polun painotettu pituus: {wdist:.1f}')
    else:
        print('Iteraatiot: ', iters)
        print('Ei ratkaisua')

# Reittien tulostus
    plot_map(map,istart,jstart,iend,jend,path1,True)
#    plot_map(map,istart,jstart,iend,jend,path3,True)

if __name__ == "__main__":
    maproute()