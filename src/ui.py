import pygame
from map import Map
from algorithm import Algorithm


class Ui:
    def __init__(self, WIDTH, THEIGHT, nrows, ncols):
        # Ruudun ja ikkunan koko
        self.WIDTH = WIDTH
        self.THEIGHT = THEIGHT
        self.gsize = WIDTH // ncols
        self.width = self.gsize * ncols
        self.height = WIDTH + THEIGHT
        self.nrows = nrows
        self.ncols = ncols
        self.maxcost = 9
        self.edit = False

        # Pygame-ikkuna
        pygame.init()
        self.win = pygame.display.set_mode((self.width, self.height))

        # Karttaruudukon generointi
        self.map = Map(self.win, self.width, self.height, self.nrows, self.ncols, self.gsize)
        self.map.generate_costs(self.maxcost)

        # Algoritmin alustus
        self.algorithm = Algorithm(self.map)

        # Alkuasetukset
        self.run = True
        pygame.display.set_caption('Paras reitti')
        self.set_texts()

# Käyttöliittymä
    def start(self):
        # Event loop
        while self.run:
            self.map.draw()
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
                            if not self.algorithm.start:
                                node.set_start()
                                self.algorithm.set_start(node)
                            elif not self.algorithm.goal and node != self.algorithm.start:
                                node.set_goal()
                                self.algorithm.set_goal(node)
                            elif node != self.algorithm.goal and node != self.algorithm.start:
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
                            if node == self.algorithm.start:
                                self.algorithm.set_start(None)
                            if node == self.algorithm.goal:
                                self.algorithm.set_goal(None)
                            node.clear()

            # Näppäinkomennot
                if event.type == pygame.KEYDOWN:

                    # Animaatio
                    if event.key == pygame.K_a:
                        self.algorithm.set_animate()
                        self.set_texts()

                    # Uusi random-kartta
                    if event.key == pygame.K_c:
                        self.map = Map(self.win, self.width, self.height, self.nrows, self.ncols, self.gsize)
                        self.map.generate_costs(self.maxcost)
                        self.algorithm.set_map(self.map)
                        self.set_texts()

                    # Polun tyypin valinta
                    if event.key == pygame.K_d:
                        self.algorithm.set_diagonal()
                        self.set_texts()

                    # Ruutujen editoinnin aloitus ja lopetus
                    if event.key == pygame.K_e:
                        self.edit = True

                    if event.key == pygame.K_q:
                        self.edit = False

                    # Metodin valinta
                    if event.key == pygame.K_m:
                        self.algorithm.set_method()
                        self.set_texts()

                    # Reset, uusi laskenta samalla kartalla
                    if event.key == pygame.K_r:
                        self.map.reset()
                        self.set_texts()

                    # Laskennan aloitus
                    if event.key == pygame.K_s:
                        if self.algorithm.start and self.algorithm.goal:
                            self.map.reset()
                            result = self.algorithm.calculate()
                            if result[0]:
                                self.map.text4 = f'Polun pituus {result[1]}'
                                self.map.text5 = f'Polun painotettu pituus {result[2]:.1f}'
                                self.map.text6 = f'Laskenta vei {result[3]:.3f} sekuntia'
                            else:
                                self.map.text4 = f'*** REITTIÄ EI LÖYTYNYT ***'
                                self.map.text5 = f''
                                self.map.text6 = f''

                    # Kartan kirjoitus tiedostoon f.map
                    if event.key == pygame.K_w:
                        self.mapwrite('./maps/f.map')

                    # Kartan luku tiedostosta f.map
                    if event.key == pygame.K_f:
                        mapfile = self.mapread("maps/f.map")
                        if mapfile:
                            oldwin = self.win
                            self.win = pygame.display.set_mode((self.width, self.height))
                            self.map = Map(self.win, self.width, self.height, self.nrows, self.ncols, self.gsize)
                            self.map.set_costs(mapfile)
                            self.algorithm.set_map(self.map)
                            self.set_texts()
                            del oldwin

                    # Uusi kartta tiedostosta 1.map .... 9.map
                    if event.key >= pygame.K_1 and event.key <= pygame.K_9:
                        mapname = './maps/' + str(event.key-48) + '.map'
                        mapfile = self.mapread(mapname)
                        if mapfile:
                            oldwin = self.win
                            self.win = pygame.display.set_mode((self.width, self.height))
                            self.map = Map(self.win, self.width, self.height, self.nrows, self.ncols, self.gsize)
                            self.map.set_costs(mapfile)
                            self.algorithm.set_map(self.map)
                            self.set_texts()
                            del oldwin

                    # Uusi kartta, ruutujen määrän lisäys (+10 molemmissa suunnissa)
                    if event.key == pygame.K_PLUS and self.ncols < 500:
                        self.ncols += 10
                        self.nrows += 10
                        self.gsize = self.WIDTH // self.ncols
                        self.width = self.gsize * self.ncols
                        self.height = self.width + self.THEIGHT
                        oldwin = self.win
                        self.win = pygame.display.set_mode((self.width, self.height))
                        self.map = Map(self.win, self.width, self.height, self.nrows, self.ncols, self.gsize)
                        self.map.generate_costs(self.maxcost)
                        self.algorithm.set_map(self.map)
                        self.set_texts()
                        del oldwin

                    # Uusi kartta, ruutujen määrän vähennys (-10 molemmissa suunnissa)
                    if event.key == pygame.K_MINUS and self.ncols > 10:
                        self.ncols -= 10
                        self.nrows -= 10
                        self.gsize = self.WIDTH // self.ncols
                        self.width = self.gsize * self.ncols
                        self.height = self.width + self.THEIGHT
                        oldwin = self.win
                        self.win = pygame.display.set_mode((self.width, self.height))
                        self.map = Map(self.win, self.width, self.height, self.nrows, self.ncols, self.gsize)
                        self.map.generate_costs(self.maxcost)
                        self.algorithm.set_map(self.map)
                        self.set_texts()

        pygame.quit()

# Klikkauksen koordinaatit
    def get_clickpos(self, pos):
        col = pos[0] // self.gsize
        row = pos[1] // self.gsize
        return row, col

# Ikkunan tekstit
    def set_texts(self):
        if self.algorithm.method == 'D':
            self.map.text1 = 'Metodi (m): Dijkstra'
        elif self.algorithm.method == 'A':
            self.map.text1 = 'Metodi (m): A*'
        elif self.algorithm.method == 'I':
            self.map.text1 = 'Metodi (m): IDA*'
        if self.algorithm.diagonal:
            self.map.text2 = 'Polun tyyppi (d): viisto'
        else:
            self.map.text2 = 'Polun tyyppi (d): x, y'
        if self.algorithm.animate:
            self.map.text3 = 'Animaatio (a): kyllä'
        else:
            self.map.text3 = 'Animaatio (a): ei'
        self.map.text4 = ''
        self.map.text5 = ''
        self.map.text6 = ''

# Kartan luku tiedostosta
    def mapread(self, fname):
        map = []
        try:
            with open(fname) as file:
                for row in file:
                    row = row.replace("\n", "")
                    map.append([char for char in row])
                self.ncols = len(map[0])
                self.nrows = len(map)
                self.gsize = self.WIDTH // self.ncols
                self.width = self.gsize * self.ncols
                self.height = self.width + self.THEIGHT
        except FileNotFoundError:
            print('Tiedostoa ei löytynyt')
        return map

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
