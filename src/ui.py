import pygame
from map import Map
from draw import Draw
from algorithm import Algorithm


# Käyttöliittymä
class Ui:
    def __init__(self, WIDTH, THEIGHT, nrows, ncols):
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
        self.algorithm = Algorithm(self.drawfunc, self.map)
        self.drawfunc.set_texts(self.algorithm)

        self.edit = False
        self.run = True

# Käynnistys
    def start(self):
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

# Klikkauksen koordinaatit
    def get_clickpos(self, pos):
        col = pos[0] // self.gsize
        row = pos[1] // self.gsize
        return row, col

# Uusi kartta
    def mapinit(self, maparray):
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

# Kartan luku tiedostosta
    def mapread(self, fname):
        map = []
        try:
            with open(fname) as file:
                for row in file:
                    row = row.replace("\n", "")
                    map.append([char for char in row])
        except FileNotFoundError:
            print('Tiedostoa ei löytynyt')
        return map

# Kartan kirjoitus tiedostoon
    def mapwrite(self, fname):
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
