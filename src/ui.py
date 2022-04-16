import pygame
from map import Map
from draw import Draw
from algorithm import Algorithm


# Käyttöliittymä
class Ui:
    """Käyttöliittymän luokka

    Attributes:
        WIDTH: Ikkunan maksimileveys pikseleinä
        THEIGHT: Ikkunan tekstiosan korkeus pikseleinä
        nrows: Rivien lukumäärä
        ncols: Sarakkeiden lukumäärä
        gsize: Karttaruudun koko pikseleinä
        width: Pygame-ikkunan leveys pikseleinä
        height: Pygame-ikkunan korkeus pikseleinä
        win: Pygame-ikkuna
        map: Karttaruudukko
        drawfunc: Piirtorutiini
        algorithm: Algoritmien käynnistys
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
                # Alku-, loppupisteet, esteiden syöttö  ja editointi(hiiren vasen näppäin)
                if pygame.mouse.get_pressed()[0]:
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

                # Pisteiden pyyhkiminen (hiiren oikea näppäin)
                elif pygame.mouse.get_pressed()[2]:
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

            # Näppäinkomennot
                if event.type == pygame.KEYDOWN:

                    # Animaatio päälle / pois
                    if event.key == pygame.K_a:
                        self.algorithm.set_animate()
                        self.drawfunc.set_texts(self.algorithm)

                    # Uusi random-kartta
                    if event.key == pygame.K_c:
                        self.mapinit(None)

                    # Polun tyyppi
                    if event.key == pygame.K_d:
                        self.algorithm.set_diagonal()
                        self.drawfunc.set_texts(self.algorithm)

                    # Ruutujen editoinnin aloitus ja lopetus
                    if event.key == pygame.K_e:
                        self.edit = True

                    if event.key == pygame.K_q:
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

                    # Laskennan aloitus
                    if event.key == pygame.K_t:
                        self.test()

                    # Kartan kirjoitus tiedostoon f.map
                    if event.key == pygame.K_w:
                        self.mapwrite('./maps/f.map')

                    # Kartan luku tiedostosta f.map
                    if event.key == pygame.K_f:
                        maparray = self.mapread("maps/f.map")
                        if maparray:
                            self.mapinit(maparray)

                    # Uusi kartta tiedostosta 1.map .... 9.map
                    if event.key >= pygame.K_1 and event.key <= pygame.K_9:
                        mapname = './maps/' + str(event.key-48) + '.map'
                        maparray = self.mapread(mapname)
                        if maparray:
                            self.mapinit(maparray)

                    # Uusi kartta, ruutujen määrän lisäys (+10 molemmissa suunnissa)
                    if event.key == pygame.K_PLUS and self.ncols < 500:
                        self.ncols += 10
                        self.nrows += 10
                        self.mapinit(None)

                    # Uusi kartta, ruutujen määrän vähennys (-10 molemmissa suunnissa)
                    if event.key == pygame.K_MINUS and self.ncols > 10:
                        self.ncols -= 10
                        self.nrows -= 10
                        self.mapinit(None)

        pygame.quit()


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


    def mapinit(self, maparray):
        """Uusi kartta.

        Args:
            maparray: Kartta tekstimuodossa
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


    def mapread(self, fname):
        """Kartan luku tiedostosta.

        Args:
            fname: Tiedoston nimi

        Returns:
            map: Luettu kartta taulukkona
        """
        map = []
        try:
            with open(fname) as file:
                for row in file:
                    row = row.replace("\n", "")
                    map.append([char for char in row])
        except FileNotFoundError:
            print('Tiedostoa ei löytynyt')
        return map


    def mapwrite(self, fname):
        """Kartan kirjoitus tiedostoon.

        Args:
            fname: Tiedoston nimi
        """
        with open(fname, "w") as file:
            for row in self.map.nodes:
                s = ''
                for node in row:
                    if node.blocked:
                        s += 'B'
                    else:
                        s += str(node.cost)
                s += '\n'
                file.write(s)


    def test(self):
        """Suorituskyvyn testausrutiini.
        """
        self.ncols = 100
        self.nrows = 100
        results = [0, 0, 0]
        self.algorithm.method = 'D'
        ntests = 10
        for _ in range(ntests):
            self.mapinit(None)
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
