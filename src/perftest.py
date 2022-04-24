import pygame
from map import Map

class Perftest:
    """Luokka, joka käynnistää eri algoritmit

    Attributes:
        ui: Käyttöliittymä
        map: Karttaruudukko
        algorithm: Laskentarutiini
        drawfunc: Piirtofunktio
        ncols: Kartan ruutujen määrä x-suunnassa
        nrows: Kartan ruutujen määrä y-suunnassa
    """


    def __init__(self, WIDTH, THEIGHT, win, map, algorithm, drawfunc):
        """Konstruktori, joka luo uuden Test-alkion

        Args:
            map: Karttaruudukko
            drawfunc: Piirtofunktio
        """
        self.WIDTH = WIDTH
        self.THEIGHT = THEIGHT
        self.win = win
        self.map = map
        self.algorithm = algorithm
        self.drawfunc = drawfunc
        self.ncols = 100
        self.nrows = 100
        self.gsize = WIDTH // self.ncols
        self.width = self.gsize * self.ncols
        self.height = WIDTH + THEIGHT


    def test(self):
        """Suorituskyvyn testausrutiini.
        """
        results = [0, 0, 0]
        self.algorithm.method = 'D'
        ntests = 10
        for _ in range(ntests):
            self.newmap(None)
            node = self.map.nodes[0][0]
            node.set_start()
            self.map.set_start(node)
            node = self.map.nodes[self.nrows-1][self.ncols-1]
            node.set_goal()
            self.map.set_goal(node)
            for i in range(3):
                self.drawfunc.reset()
                result = self.algorithm.calculate()
                self.drawfunc.drawmap()
                results[i] += result[3]
                self.algorithm.set_method()
        results[0] /= ntests
        results[1] /= ntests
        results[2] /= ntests
        self.drawfunc.test_results(results)


    def newmap(self, maparray):
        """Kartan ja Pygame-ikkunan muutos.

        Args:
            maparray: Kartta kirjaintaulukkona
        """
        # Kartan parametrit
        self.gsize = self.WIDTH // self.ncols
        self.width = self.gsize * self.ncols
        self.height = self.width + self.THEIGHT

        # Uusi Pygame-ikkuna
        oldwin = self.win
        self.win = pygame.display.set_mode((self.width, self.height))
        del oldwin

        # Uusi kartta
        oldmap = self.map
        self.map = Map(self.nrows, self.ncols, self.gsize)
        del oldmap

        # Ruutujen cost-arvot
        self.map.generate_costs()

        # Algoritmin ja piirtofunktion asetukset
        self.algorithm.set_map(self.map)
        self.drawfunc.set_win(self.win, self.width, self.height, self.map)
        self.drawfunc.set_texts(self.algorithm)
