import numpy as np
from map import generate_map
from dijkstra import dijkstra_traditional, dijkstra_diagonal
from plotmap import plot_map

if __name__ == "__main__":
    ysize = 40
    xsize = 80
    istart = 0
    jstart = 0
    iend = ysize-1
    jend = xsize-1
    levels = 6
    limit = 5
    map = generate_map(ysize,xsize,levels)

    print('\nDijkstra traditionaalinen')
    wdist,nsteps,iters,path1 = dijkstra_traditional(map,istart,jstart,iend,jend,limit)
    if wdist > 0:
        print('Iteraatiot: ', iters)
        print('Polun pituus:', nsteps)
        print(f'Polun painotettu pituus: {wdist}')
    else:
        print('Iteraatiot: ', iters)
        print('Ei ratkaisua')

    print('\nDijkstra diagonaalinen')
    wdist,nsteps,iters,path2 = dijkstra_diagonal(map,istart,jstart,iend,jend,limit)
    if wdist > 0:
        print('Iteraatiot: ', iters)
        print('Polun pituus:', nsteps)
        print(f'Polun painotettu pituus: {wdist:.1f}')
    else:
        print('Iteraatiot: ', iters)
        print('Ei ratkaisua')
    plot_map(map,istart,jstart,iend,jend,path1,'green',path2,'blue',True)
