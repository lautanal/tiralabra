from node import Node
from map import Map
from dijkstra import dijkstra
from astar import astar
from idastar import idastar


class Algorithm:
    def __init__(self, map):
        self.map = map
        self.method = 'D'
        self.diagonal = False
        self.animate = False

# Metodi
    def set_method(self):
        if self.method == 'D':
            self.method = 'A'
        elif self.method == 'A':
            self.method = 'I'
        elif self.method == 'I':
            self.method = 'D'

# Polun tyyppi
    def set_diagonal(self):
        if self.diagonal:
            self.diagonal = False
        else:
            self.diagonal = True

# Animaatio
    def set_animate(self):
        if self.animate:
            self.animate = False
        else:
            self.animate = True

# Laskennan käynnistys
    def calculate(self):
        if self.method == 'D':
            result, time = dijkstra(self.map, self.diagonal, self.animate)
        elif self.method == 'A':
            result, time = astar(self.map, self.diagonal, self.animate)
        elif self.method == 'I':
            result, time = idastar(self.map, self.diagonal, self.animate)
        if result:
            print(f'*** REITTI LÖYTYI ***\nLaskenta vei {time:.3f} sekuntia')
            # Polku
            npath, costsum = self.map.track_path(self.diagonal)
            return True, npath, costsum, time
        else:
            return False, 0, 0, 0
