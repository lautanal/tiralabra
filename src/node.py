WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAYSHADES = [(240,240,240),(220,220,220),(200,200,200),(180,180,180),(160,160,160),(140,140,140),(120,120,120),(100,100,100),(80,80,80),(60,60,60),(0,0,0)]


class Node:
    """Luokka, joka mallintaa karttaruudun

    Attributes:
        row: Rivinumero
        col: Sarakenumero
        x: Ruudun x-koordinaatti (vasen ylänurkka)
        y: Ruudun y-koordinaatti (vasen ylänurkka)
        color: Ruudun väri
        start: Ruutu on lähtöruutu
        goal: Ruutu on maaliruutu
        blocked: Ruutu on este
        visited: Ruudussa on vierailtu
        visited_jps: Ruudun kautta kulkeva reitti on tutkittu (JPS)
        previous: Edellinen ruutu reitillä
        cost: Ruudun painoarvo
        costsum: Reitin hinta (tai aika)
        heuristic: Ruudulle laskettu heuristiikka
    """


    def __init__(self, row, col, gsize):
        """Luokan konstruktori, joka luo uuden karttaruudun.

        Args:
            row: Rivinumero
            col: Sarakenumero
            gsize: Karttaruudun koko pikseleinä
        """
        self.row = row
        self.col = col
        self.x = col * gsize
        self.y = row * gsize
        self.color = WHITE
        self.start = False
        self.goal = False
        self.blocked = False
        self.visited = False
        self.visited_jps = [0,0,0,0,0,0,0,0]
        self.previous = None
        self.neighbors = []
        self.cost = 1
        self.costsum = float("inf")
        self.heuristic = float("inf")


    def __lt__(self, other):
        return self.costsum + self.heuristic < other.costsum + other.heuristic


    def clear(self):
        """ Ruudun reset
        """
        self.start = False
        self.goal = False
        self.blocked = False
        self.color = GRAYSHADES[self.cost]


    def get_pos(self):
        """ Ruudun paikka

        Returns:
            row, col (Tuple): Ruudun rivi ja sarake
        """
        return self.row, self.col


    def mark_path(self):
        """ Reittiruudun väritys punaiseksi
        """
        self.color = RED


    def reset_color(self):
        """ Ruudun värin palautus normaaliksi
        """
        self.color = GRAYSHADES[self.cost]
        if self.blocked:
            self.color = BLACK


    def set_color(self, color):
        """ Ruudun väritys
        """
        self.color = color


    def set_blocked(self):
        """ Esteruutu
        """
        self.blocked = True
        self.color = BLACK


    def set_goal(self):
        """ Maaliruutu
        """
        self.goal = True
        self.blocked = False
        self.color = ORANGE
        return self


    def set_start(self):
        """ Lähtöruutu
        """
        self.start = True
        self.blocked = False
        self.color = BLUE
        return self


    def set_visited(self):
        """ Vierailtu ruutu
        """
        self.visited = True


    def set_visited_jps(self, dir):
        """ Vierailtu ruutu ja skannaussuunta
        """
        if dir == (1,0):
            self.visited_jps[0] = 1
        elif dir == (1,1):
            self.visited_jps[1] = 1
        elif dir == (0,1):
            self.visited_jps[2] = 1
        elif dir == (-1,1):
            self.visited_jps[3] = 1
        elif dir == (-1,0):
            self.visited_jps[4] = 1
        elif dir == (-1,-1):
            self.visited_jps[5] = 1
        elif dir == (0,-1):
            self.visited_jps[6] = 1
        elif dir == (1,-1):
            self.visited_jps[7] = 1


    def check_visited_jps(self, dir):
        """ Tarkistetaan reitti jo tutkittu
        """
        if dir == (1,0):
            return self.visited_jps[0] == 1
        elif dir == (1,1):
            return self.visited_jps[1] == 1
        elif dir == (0,1):
            return self.visited_jps[2] == 1
        elif dir == (-1,1):
            return self.visited_jps[3] == 1
        elif dir == (-1,0):
            return self.visited_jps[4] == 1
        elif dir == (-1,-1):
            return self.visited_jps[5] == 1
        elif dir == (0,-1):
            return self.visited_jps[6] == 1
        elif dir == (1,-1):
            return self.visited_jps[7] == 1
