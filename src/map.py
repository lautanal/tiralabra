import random
from math import sqrt
from node import Node


class Map:
    """Luokka, joka mallintaa karttaruudukon

    Attributes:
        nrows: Rivien lukumäärä
        ncols: Sarakkeiden lukumäärä
        gsize: Karttaruudun koko pikseleinä
        nodes: Karttaruudut taulukkona
        start: Lähtöruutu
        goal: Maaliruutu
    """

    def __init__(self, nrows, ncols, gsize):
        """Luokan konstruktori, joka luo uuden karttaruudukon.

        Args:
            nrows: Rivien lukumäärä
            ncols: Sarakkeiden lukumäärä
            gsize: Karttaruudun koko pikseleinä
        """
        self.nrows = nrows
        self.ncols = ncols
        self.gsize = gsize
        self.nodes = []
        self.start = None
        self.goal = None
        self.make()


    def make(self):
        """ Solmujen luonti
        """
        for i in range(self.nrows):
            self.nodes.append([])
            for j in range(self.ncols):
                node = Node(i, j, self.gsize)
                self.nodes[i].append(node)


    def generate_costs(self):
        """ Kartan random-generointi (solmujen painot)
        """
        costmap = [[random.randrange(1, 10, 1) for _ in range(self.ncols)] for _ in range(self.nrows)]
        for row in self.nodes:
            for node in row:
                node.cost = costmap[node.row][node.col]
                ngrey = (10 - node.cost) * 24
                node.color = (ngrey, ngrey, ngrey)


    def set_costs(self, maparray):
        """ Kartan generointi (kartta luettu tiedostosta)
        """
        for row in self.nodes:
            for node in row:
                if maparray[node.row][node.col] == 'B':
                    node.cost = 1
                    node.blocked = True
                    node.color = (0, 0, 0)
                else:
                    node.cost = int(maparray[node.row][node.col])
                    ngrey = (10 - node.cost) * 24
                    node.color = (ngrey, ngrey, ngrey)


    def set_start(self, start):
        """ Lähtöpiste
        """
        self.start = start


    def set_goal(self, goal):
        """ Maalipiste
        """
        self.goal = goal


    def neighbors_xy(self):
        """ Solmujen naapurit, xy-polku
        """
        for row in self.nodes:
            for node in row:
                node.costsum = float("inf")

                node.neighbors = []
                if node.row < self.nrows - 1 and not self.nodes[node.row + 1][node.col].blocked:
                    node.neighbors.append(self.nodes[node.row + 1][node.col])

                if node.row > 0 and not self.nodes[node.row - 1][node.col].blocked:
                    node.neighbors.append(self.nodes[node.row - 1][node.col])

                if node.col < self.ncols - 1 and not self.nodes[node.row][node.col + 1].blocked:
                    node.neighbors.append(self.nodes[node.row][node.col + 1])

                if node.col > 0 and not self.nodes[node.row][node.col - 1].blocked:
                    node.neighbors.append(self.nodes[node.row][node.col - 1])


    def neighbors_diag(self):
        """ Solmujen naapurit, viisto polku
        """
        for row in self.nodes:
            for node in row:
                node.costsum = float("inf")

                node.neighbors = []
                if node.row < self.nrows - 1:
                    if not self.nodes[node.row + 1][node.col].blocked:
                        node.neighbors.append(self.nodes[node.row + 1][node.col])
                    if node.col < self.ncols - 1 and not self.nodes[node.row + 1][node.col + 1].blocked:
                        node.neighbors.append(self.nodes[node.row + 1][node.col + 1])
                    if node.col > 0 and not self.nodes[node.row + 1][node.col - 1].blocked:
                        node.neighbors.append(self.nodes[node.row + 1][node.col - 1])

                if node.row > 0:
                    if not self.nodes[node.row - 1][node.col].blocked:
                        node.neighbors.append(self.nodes[node.row - 1][node.col])
                    if node.col < self.ncols - 1 and not self.nodes[node.row - 1][node.col + 1].blocked:
                        node.neighbors.append(self.nodes[node.row - 1][node.col + 1])
                    if node.col > 0 and not self.nodes[node.row - 1][node.col - 1].blocked:
                        node.neighbors.append(self.nodes[node.row - 1][node.col - 1])

                if node.col < self.ncols - 1 and not self.nodes[node.row][node.col + 1].blocked:
                    node.neighbors.append(self.nodes[node.row][node.col + 1])

                if node.col > 0 and not self.nodes[node.row][node.col - 1].blocked:
                    node.neighbors.append(self.nodes[node.row][node.col - 1])


    def heuristic_manhattan(self, goal):
        """ Manhattan heuristiikka
        """
        for row in self.nodes:
            for node in row:
                y1, x1 = node.get_pos()
                y2, x2 = goal.get_pos()
                node.heuristic = abs(x1 - x2) + abs(y1 - y2)


    def heuristic_euclidian(self, goal):
        """ Eukliidinen heuristiikka
        """
        for row in self.nodes:
            for node in row:
                y1, x1 = node.get_pos()
                y2, x2 = goal.get_pos()
                node.heuristic = sqrt((x1 - x2)**2 + (y1 - y2)**2)


    def track_path(self, diagonal):
        """ Polun track
        """
        node = self.goal.previous
        count = 0
        while node != self.start:
            count += 1
            node.mark_path()
            node = node.previous
        costsum = self.goal.costsum
        if not diagonal:
            costsum = self.goal.costsum - self.goal.cost
        return count, costsum
