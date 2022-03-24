import numpy as np
from map import generate_map
from dijkstra import dijkstra_traditional, dijkstra_diagonal
from plotmap import plot_map

def maproute():
# Luodaan kartta
    ysize = 40
    xsize = 40
    levels = 6
    map = generate_map(ysize,xsize,levels)

# Reitin alku- ja loppupisteet
    istart = 0
    jstart = 0
    iend = ysize-1
    jend = xsize-1

# Dijsktran menetelmä, vain vaaka- ja pystysiirtymät
    print('\nDijkstra traditionaalinen')
    wdist,nsteps,iters,path1 = dijkstra_traditional(map,istart,jstart,iend,jend)
    if wdist > 0:
        print('Iteraatiot: ', iters)
        print('Polun pituus:', nsteps)
        print(f'Polun painotettu pituus: {wdist}')
    else:
        print('Iteraatiot: ', iters)
        print('Ei ratkaisua')

# Dijsktran menetelmä, diagonaalisiirtymät sallittu
    print('\nDijkstra diagonaalinen')
    wdist,nsteps,iters,path2 = dijkstra_diagonal(map,istart,jstart,iend,jend)
    if wdist > 0:
        print('Iteraatiot: ', iters)
        print('Polun pituus:', nsteps)
        print(f'Polun painotettu pituus: {wdist:.1f}')
    else:
        print('Iteraatiot: ', iters)
        print('Ei ratkaisua')
    plot_map(map,istart,jstart,iend,jend,path1,path2,True)

if __name__ == "__main__":
    maproute()