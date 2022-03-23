import numpy as np
import matplotlib.pyplot as plt
import copy
from timeit import default_timer as timer


def plot_map(map,istart,jstart,iend,jend,path1,pathcolor1,path2,pathcolor2,numbers):
    tstart = timer()
    ysize = map.shape[0]
    xsize = map.shape[1]
# Alustus
    cmap1 = copy.copy(plt.cm.get_cmap("Greys"))
    cmap1.set_bad(color=pathcolor1)
    cmap1.set_under(color='blue')
    cmap1.set_over(color='green')
    cmap2 = copy.copy(plt.cm.get_cmap("Greys"))
    cmap2.set_bad(color=pathcolor2)
    cmap2.set_under(color='blue')
    cmap2.set_over(color='green')
    fig, (ax1, ax2) = plt.subplots(2,1,figsize=(12,12))
# Plot 1 
    plottemp=map.astype(float)
    for i in range(len(path1)):
        i,j = path1[i]
        plottemp[i,j] = None
    plottemp[istart,jstart] = -100
    plottemp[iend,jend] = 100
    ax1.matshow(plottemp, cmap=cmap1,vmin=0,vmax=10)
    if numbers:
        for i in range(xsize):
            for j in range(ysize):
                nr = map[j,i]
                ax1.text(i,j,nr,va='center',ha='center')       
# Plot 2 
    plottemp=map.astype(float)
    for i in range(len(path2)):
        i,j = path2[i]
        plottemp[i,j] = None
    plottemp[istart,jstart] = -100
    plottemp[iend,jend] = 100
    ax2.matshow(plottemp, cmap=cmap2,vmin=0,vmax=10)
    if numbers:
        for i in range(xsize):
            for j in range(ysize):
                nr = map[j,i]
                ax2.text(i,j,nr,va='center',ha='center')

    tend = timer()
    print(f'\nPlottaus vei {tend-tstart:.3f} sekuntia')
    plt.show()
