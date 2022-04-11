import pygame
from queue import PriorityQueue

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)


class Node:
    def __init__(self, row, col, gsize):
        self.row = row
        self.col = col
        self.x = col * gsize
        self.y = row * gsize
        self.gsize = gsize
        self.color = WHITE
        self.start = False
        self.goal = False
        self.blocked = False
        self.visited = False
        self.previous = None
        self.neighbors = []
        self.cost = 1
        self.costsum = float("inf")
        self.heuristic = float("inf")

    def __lt__(self, other):
        return self.costsum + self.heuristic < other.costsum + other.heuristic

# Ruudun reset
    def clear(self):
        self.start = False
        self.goal = False
        self.blocked = False
        ngrey = (10 - self.cost) * 24
        self.color = (ngrey, ngrey, ngrey)

# Ruudun paikka
    def get_pos(self):
        return self.row, self.col

# Polun merkintä
    def mark_path(self):
        self.color = RED

# Ruudun värin reset
    def reset_color(self):
        ngrey = (10 - self.cost) * 24
        self.color = (ngrey, ngrey, ngrey)

# Estetty ruutu
    def set_blocked(self):
        self.blocked = True
        self.color = BLACK

# Maaliruutu
    def set_goal(self):
        self.goal = True
        self.blocked = False
        self.color = ORANGE
        return self

# Lähtöruutu
    def set_start(self):
        self.start = True
        self.blocked = False
        self.color = BLUE
        return self

# Vierailtu ruutu
    def set_visited(self, animate):
        self.visited = True
        if animate and not self.start:
            self.color = GREEN
