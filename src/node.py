WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)


class Node:
    """Luokka, joka mallintaa karttaruudun

    Attributes:
        row: Rivinumero
        col: Sarakenumero
        gsize: Karttaruudun koko pikseleinä
        color: Ruudun väri
        start: Ruutu on lähtöruutu
        goal: Ruutu on maaliruutu
        blocked: Ruutu on este
        visited: Ruudussa on vierailtu
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


    def clear(self):
        """ Ruudun reset
        """
        self.start = False
        self.goal = False
        self.blocked = False
        ngrey = (10 - self.cost) * 24
        self.color = (ngrey, ngrey, ngrey)


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
        ngrey = (10 - self.cost) * 24
        self.color = (ngrey, ngrey, ngrey)


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


    def set_visited(self, animate):
        """ Vierailtu ruutu
        """
        self.visited = True
        if animate and not self.start:
            self.color = GREEN
