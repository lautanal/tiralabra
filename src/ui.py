import os
import pygame
from map import Map
from draw import Draw
from algorithm import Algorithm
from files import Files
from perftest import Perftest


# Käyttöliittymä
class Ui:
    """Käyttöliittymän luokka

    Attributes:
        WIDTH: Ikkunan maksimileveys pikseleinä
        THEIGHT: Ikkunan tekstiosan korkeus pikseleinä
        nrows: Rivien lukumäärä
        ncols: Sarakkeiden lukumäärä
        gsize: Karttaruudun koko pikseleinä
        win: Pygame-ikkuna
        width: Pygame-ikkunan leveys pikseleinä
        height: Pygame-ikkunan korkeus pikseleinä
        map: Karttaruudukko
        drawfunc: Piirtorutiini
        algorithm: Algoritmien käynnistysrutiini
        files = Tiedostojen käsittelijä
        edit: Kartan editointi käynnissä
        run: Pygame-käynnissä
    """

    def __init__(self, WIDTH, THEIGHT, nrows, ncols):
        """Luokan konstruktori, joka luo uuden käyttöliittymän.

        Args:
            WIDTH: Ikkunan maksimileveys pikseleinä
            THEIGHT: Ikkunan tekstiosan korkeus pikseleinä
            nrows: Rivien lukumäärä
            ncols: Sarakkeiden lukumäärä
        """

        # Ikkunan kokoparametrit
        self.WIDTH = WIDTH
        self.THEIGHT = THEIGHT
        self.gsize = WIDTH // ncols
        self.width = self.gsize * ncols
        self.height = WIDTH + THEIGHT
        self.nrows = nrows
        self.ncols = ncols

        # Pygame-ikkunan luonti
        pygame.init()
        pygame.display.set_caption('Paras reitti')
        self.win = pygame.display.set_mode((self.width, self.height))

        # Kartan alustus
        self.map = Map(self.nrows, self.ncols, self.gsize)
        self.map.generate_costs()

        # Algoritmi- ja piirtofunktioiden alustus
        self.drawfunc = Draw(self.win, self.width, self.height, self.map)
        self.algorithm = Algorithm(self.map, self.drawfunc.drawnode)
        self.drawfunc.set_texts(self.algorithm)
        self.files = Files()

        self.edit = False
        self.run = True


    def start(self):
        """Käyttöliittymän käynnistys.
        """

        # Event loop
        while self.run:
            self.drawfunc.drawmap()
            for event in pygame.event.get():
                # Lopetus
                if event.type == pygame.QUIT:
                    self.run = False

            # Hiirikomennot
                # Alku-, loppupisteet, esteiden syöttö  ja editointi (hiiren vasen näppäin)
                if pygame.mouse.get_pressed()[0]:
                    self.leftclick()

                # Pisteiden pyyhkiminen (hiiren oikea näppäin)
                elif pygame.mouse.get_pressed()[2]:
                    self.rightclick()

            # Näppäinkomennot
                if event.type == pygame.KEYDOWN:
                    self.keyboard(event)

        pygame.quit()


    def leftclick(self):
        """Hiiren vasemman näppäimen klikkaus.
        """
        pos = pygame.mouse.get_pos()
        row, col = self.get_clickpos(pos)
        if row < self.nrows:
            node = self.map.nodes[row][col]
            if self.edit:
                if not node.blocked and node.cost < 9:
                    node.cost += 1
                    node.reset_color()
            else:
                if not self.map.start:
                    node.set_start()
                    self.map.set_start(node)
                elif not self.map.goal and node != self.map.start:
                    node.set_goal()
                    self.map.set_goal(node)
                elif node != self.map.goal and node != self.map.start:
                    node.set_blocked()


    def rightclick(self):
        """Hiiren oikean näppäimen klikkaus.
        """
        pos = pygame.mouse.get_pos()
        row, col = self.get_clickpos(pos)
        if row < self.nrows:
            node = self.map.nodes[row][col]
            if self.edit:
                if not node.blocked and node.cost > 1:
                    node.cost -= 1
                    node.reset_color()
            else:
                node = self.map.nodes[row][col]
                if node == self.map.start:
                    self.map.set_start(None)
                if node == self.map.goal:
                    self.map.set_goal(None)
                node.clear()


    def get_clickpos(self, pos):
        """Klikkauksen koordinaatit.

        Args:
            pos: Klikkauksen positio pikseleinä

        Returns:
            row: Klikatun ruudun rivi
            col: Klikatun ruudun sarake
        """
        col = pos[0] // self.gsize
        row = pos[1] // self.gsize
        return row, col


    def keyboard(self, event):
        """Näppäinkomennot.
        """
        # Animaatio päälle / pois
        if event.key == pygame.K_a:
            self.algorithm.set_animate()
            self.drawfunc.set_texts(self.algorithm)

        # Uusi random-kartta
        if event.key == pygame.K_c:
            self.newmap(None)

        # Polun tyyppi
        if event.key == pygame.K_d:
            self.algorithm.set_diagonal()
            self.drawfunc.set_texts(self.algorithm)

        # Ruutujen editoinnin aloitus ja lopetus
        if event.key == pygame.K_e:
            print('Editointi aloitus')
            self.edit = True

        if event.key == pygame.K_q:
            print('Editointi lopetus')
            self.edit = False

        # Metodin valinta
        if event.key == pygame.K_m:
            self.algorithm.set_method()
            self.drawfunc.set_texts(self.algorithm)

        # Reset, uusi laskenta samalla kartalla
        if event.key == pygame.K_r:
            self.drawfunc.reset()
            self.drawfunc.set_texts(self.algorithm)

        # Laskennan aloitus
        if event.key == pygame.K_s:
            if self.map.start and self.map.goal:
                self.drawfunc.reset()
                result = self.algorithm.calculate()
                self.drawfunc.set_results(result)

        # Suorituskykytesti
        if event.key == pygame.K_t:
            perftest = Perftest(self.WIDTH, self.THEIGHT, self.win, self.map, self.algorithm, self.drawfunc)
            perftest.test()
            del perftest

        # Kartan kirjoitus tiedostoon f.map
        if event.key == pygame.K_w:
            self.files.fname = 'f.map'
            self.files.write(self.map)

        # Kartan luku tiedostosta f.map
        if event.key == pygame.K_f:
            self.files.fname = 'f.map'
            maparray = self.files.read()
            if maparray:
                self.newmap(maparray)

        # Uusi kartta tiedostosta 1.map .... 9.map
        if event.key >= pygame.K_1 and event.key <= pygame.K_9:
            fname = str(event.key-48) + '.map'
            self.files.fname = fname
            maparray = self.files.read()
            if maparray:
                self.newmap(maparray)

        # Uusi kartta, ruutujen määrän lisäys (+10 molemmissa suunnissa)
        if event.key == pygame.K_PLUS and self.ncols < 500:
            self.ncols += 10
            self.nrows += 10
            self.newmap(None)

        # Uusi kartta, ruutujen määrän vähennys (-10 molemmissa suunnissa)
        if event.key == pygame.K_MINUS and self.ncols > 10:
            self.ncols -= 10
            self.nrows -= 10
            self.newmap(None)


    def newmap(self, maparray):
        """Uusi kartta ja Pygame-ikkuna.

        Args:
            maparray: Kartta kirjaintaulukkona
        """
        # Kartan parametrit
        if maparray:
            self.ncols = len(maparray[0])
            self.nrows = len(maparray)
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
        if maparray:
            self.map.set_costs(maparray)
        else:
            self.map.generate_costs()

        # Algoritmin ja piirtofunktion asetukset
        self.algorithm.set_map(self.map)
        self.drawfunc.set_win(self.win, self.width, self.height, self.map)
        self.drawfunc.set_texts(self.algorithm)
