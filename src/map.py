import numpy as np
from random import randint

def generate_map(ysize,xsize,levels):
#Generate map
    map = np.random.randint(1, levels+1, size=(ysize, xsize))
#    generate_hills(map,int(ysize/2),int(ysize/10),int(ysize/10),levels,int(1.5*levels))
    generate_hills(map,10,8,8,levels,int(1.5*levels))
    return map

def generate_hills(map,n,dy,dx,low,high):
    ysize = map.shape[0]
    xsize = map.shape[1]
    for k in range(n):
        hillmap= np.random.randint(low, high+1, size=(dy, dx))
        yhill = randint(int(dy/2),int(ysize-dy/2-1))
        xhill = randint(int(dx/2),int(xsize-dx/2-1))
        for i in range(dy):
            for j in range(dx):
                map[int(yhill-dy/2+i),int(xhill-dx/2+j)] = hillmap[i,j]
