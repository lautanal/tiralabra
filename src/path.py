
def get_path(previous,istart,jstart,iend,jend):
    path = []
    i,j = iend, jend
    while i != istart or j != jstart:
        path.append([i,j])
        i,j = previous[i][j]
    path.append([i,j])
    path.reverse()
    return path
