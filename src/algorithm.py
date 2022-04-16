from dijkstra import dijkstra
from astar import astar
from idastar import idastar


class Algorithm:
    """Luokka, joka käynnistää eri algoritmit

    Attributes:
        map: Karttaruudukko
        drawfunc: Piirtofunktio
        method: Käytetty metodi
        diagonal: Polun tyyppi (diagonal / xy)
        animate: Animaatio päällä
    """


    def __init__(self, map, drawfunc):
        """Konstruktori, joka luo uuden Algorithm-alkion

        Args:
            map: Karttaruudukko
            drawfunc: Piirtofunktio
        """
        self.drawfunc = drawfunc
        self.map = map
        self.method = 'D'
        self.diagonal = False
        self.animate = False


    def set_method(self):
        """Metodin vaihto
        """
        if self.method == 'D':
            self.method = 'A'
        elif self.method == 'A':
            self.method = 'I'
        elif self.method == 'I':
            self.method = 'D'


    def set_diagonal(self):
        """Polun tyyppi (diagonal / xy)
        """
        if self.diagonal:
            self.diagonal = False
        else:
            self.diagonal = True


    def set_animate(self):
        """Animaatio päällä / pois
        """
        if self.animate:
            self.animate = False
        else:
            self.animate = True


    def set_map(self, map):
        """Uusi kartta
        """
        self.map = map


    def calculate(self):
        """Laskennan käynnistys
        """
        if self.method == 'D':
            result, time = dijkstra(self.map, self.diagonal, self.animate, self.drawfunc)
        elif self.method == 'A':
            result, time = astar(self.map, self.diagonal, self.animate, self.drawfunc)
        elif self.method == 'I':
            result, time = idastar(self.map, self.diagonal, self.animate, self.drawfunc)
        if result:
            # Polku
            npath, costsum = self.map.track_path(self.diagonal)
            print(f'*** REITTI LÖYTYI ***\nLaskenta vei {time:.3f} sekuntia\nPolun pituus {npath}\nPolun painotettu pituus {costsum}')
            return True, npath, costsum, time
        else:
            return False, 0, 0, 0
