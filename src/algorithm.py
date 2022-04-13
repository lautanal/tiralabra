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
        self.start = None
        self.goal = None

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

# Kartta
    def set_map(self, map):
        self.map = map
        self.start = None
        self.goal = None

# Lähtöpiste
    def set_start(self, start):
        self.start = start

# Maalipiste
    def set_goal(self, goal):
        self.goal = goal

# Laskennan käynnistys
    def calculate(self):
        if self.method == 'D':
            result, time = dijkstra(self.map, self.start, self.goal, self.diagonal, self.animate)
        elif self.method == 'A':
            result, time = astar(self.map, self.start, self.goal, self.diagonal, self.animate)
        elif self.method == 'I':
            result, time = idastar(self.map, self.start, self.goal, self.diagonal, self.animate)
        if result:
            print(f'*** REITTI LÖYTYI ***\nLaskenta vei {time:.3f} sekuntia')
            npath, costsum = self.results()
            return True, npath, costsum, time
        else:
            return False, 0, 0, 0

# Tulosten laskeminen
    def results(self):
        npath = self.track_path(self.start, self.goal)
        costsum = self.goal.costsum
        if not self.diagonal:
            costsum = self.goal.costsum - self.goal.cost
        return npath, costsum

# Polun track
    def track_path(self, start, goal):
        node = goal.previous
        count = 0
        while node != start:
            count += 1
            node.mark_path()
            node = node.previous
        return count
