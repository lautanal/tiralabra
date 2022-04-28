import pygame


class Draw:
    """Luokka, jossa on Pygame-piirtorutiinit

    Attributes:
        win = Pygame-ikkuna
        map = Karttaruudukko
        width = Pygame-ikkunan leveys
        height = Pygame-ikkunan korkeus
        nrows = Karttaruudukon rivien lukumäärä
        ncols = Karttaruudukon sarakkeiden lukumäärä
        gsize = Ruudun koko pikseleinä
        text1 = Teksti 1
        text2 = Teksti 2
        text3 = Teksti 3
        text4 = Teksti 4
        text5 = Teksti 5
        text6 = Teksti 6
        text7 = Teksti 7
        text8 = Teksti 8
        text9 = Teksti 9
        text10 = Teksti 10
    """


    def __init__(self, win, width, height, map):
        """Konstruktori, joka luo uuden Draw-alkion

        Attributes:
            win = Pygame-ikkuna
            width = Pygame-ikkunan leveys
            height = Pygame-ikkunan korkeus
            map = Karttaruudukko
        """
        self.win = win
        self.map = map
        self.width = width
        self.height = height
        self.nrows = map.nrows
        self.ncols = map.ncols
        self.gsize = map.gsize
        self.text1 = ''
        self.text2 = ''
        self.text3 = ''
        self.text4 = ''
        self.text5 = ''
        self.text6 = ''
        self.text7 = ''
        self.text8 = ''
        self.text9 = ''
        self.text10 = ''


    def drawmap(self):
        """Koko karttaruudukon piirto
        """
        font = pygame.font.SysFont('Arial', self.gsize // 2)
        for row in self.map.nodes:
            for node in row:
                pygame.draw.rect(self.win, node.color, (node.x, node.y, self.gsize, self.gsize))
#                if not node.blocked:
#                    if node.cost < 10:
#                        self.win.blit(font.render(str(node.cost), True, (128, 128, 128)),
#                                (node.x+2*(self.gsize//5), node.y+self.gsize//4))
#                    else:
#                        self.win.blit(font.render(str(node.cost), True, (128, 128, 128)),
#                                (node.x+self.gsize//3, node.y+self.gsize//4))

        for i in range(self.nrows):
            pygame.draw.line(self.win, (128, 128, 128), (0, i * self.gsize), (self.width, i * self.gsize))
        for j in range(self.ncols):
            pygame.draw.line(self.win, (128, 128, 128), (j * self.gsize, 0), (j * self.gsize, self.nrows * self.gsize))

        pygame.draw.rect(self.win, (180, 180, 180), (0, self.nrows*self.gsize, self.width,
                self.height-self.nrows*self.gsize))
        pygame.draw.line(self.win, (60, 60, 60), (0, self.nrows*self.gsize), (self.width, self.nrows*self.gsize))

        font = pygame.font.SysFont('Arial', 15)
        self.win.blit(font.render(str(self.text1), True, (64, 64, 64)), (40, self.nrows*self.gsize + 20))
        self.win.blit(font.render(str(self.text2), True, (64, 64, 64)), (40, self.nrows*self.gsize + 40))
        self.win.blit(font.render(str(self.text3), True, (64, 64, 64)), (40, self.nrows*self.gsize + 60))
        self.win.blit(font.render(str(self.text4), True, (64, 64, 64)), (40, self.nrows*self.gsize + 80))
        self.win.blit(font.render(str(self.text5), True, (64, 64, 64)), (40, self.nrows*self.gsize + 100))
        self.win.blit(font.render(str(self.text6), True, (64, 64, 64)), (self.width // 2, self.nrows*self.gsize + 20))
        self.win.blit(font.render(str(self.text7), True, (64, 64, 64)), (self.width // 2, self.nrows*self.gsize + 40))
        self.win.blit(font.render(str(self.text8), True, (64, 64, 64)), (self.width // 2, self.nrows*self.gsize + 60))
        self.win.blit(font.render(str(self.text9), True, (64, 64, 64)), (self.width // 2, self.nrows*self.gsize + 80))

        pygame.display.update()


    def drawnode(self, node):
        """Yhden karttaruudun piirto
        """
        font = pygame.font.SysFont('Arial', self.gsize // 2)
        pygame.draw.rect(self.win, node.color, (node.x, node.y, self.gsize, self.gsize))
        if node.cost < 10:
            self.win.blit(font.render(str(node.cost), True, (128, 128, 128)),
                    (node.x+2*(self.gsize//5), node.y+self.gsize//4))
        else:
            self.win.blit(font.render(str(node.cost), True, (128, 128, 128)),
                    (node.x+self.gsize//3, node.y+self.gsize//4))
        pygame.display.update()


    def reset(self):
        """Karttaruutujen värien reset
        """
        for row in self.map.nodes:
            for node in row:
                node.visited = False
                if not node.start and not node.goal and not node.blocked:
                    node.reset_color()


    def set_win(self, win, width, height, map):
        """Pygame-ikkunan asetukset
        """
        self.win = win
        self.map = map
        self.width = width
        self.height = height
        self.nrows = map.nrows
        self.ncols = map.ncols
        self.gsize = map.gsize


    def set_texts(self, algorithm):
        """Pygame-ikkunan tekstit
        """
        if algorithm.method == 'D':
            self.text1 = 'Metodi (m): Dijkstra'
        elif algorithm.method == 'A':
            self.text1 = 'Metodi (m): A*'
        elif algorithm.method == 'I':
            self.text1 = 'Metodi (m): IDA*'
        if algorithm.diagonal:
            self.text2 = 'Polun tyyppi (d): viisto'
        else:
            self.text2 = 'Polun tyyppi (d): x, y'
        if algorithm.animate:
            self.text3 = 'Animaatio (a): kyllä'
        else:
            self.text3 = 'Animaatio (a): ei'
        self.text4 = f'Kartan koko: {self.nrows} x {self.ncols}'
        self.text5 = ''
        if self.map.start:
            self.text5 = f'Lähtö x,y: {str(self.map.start.col)},{str(self.map.start.row)}      '
        if self.map.goal:
            self.text5 += f'Maali x,y: {str(self.map.goal.col)},{str(self.map.goal.row)}'
        self.text6 = ''
        self.text7 = ''
        self.text8 = ''
        self.text9 = ''
        self.text10 = ''


    def set_results(self, result):
        """Laskennan tulokset näkyville
        """
        if result[0]:
            self.text6 = f'Polun pituus {result[1]}'
            self.text7 = f'Polun painotettu pituus {result[2]:.1f}'
            self.text8 = f'Laskenta vei {result[3]:.3f} sekuntia'
            self.text9 = ''
        else:
            self.text6 = '*** REITTIÄ EI LÖYTYNYT ***'
            self.text7 = ''
            self.text8 = ''
            self.text9 = ''


    def test_results(self, result):
        """Testilaskennan tulokset näkyville
        """
        self.text6 = f'Dijkstra keskimäärin: {result[0]:.4f} sekuntia'
        self.text7 = f'A* keskimäärin : {result[1]:.4f} sekuntia'
        self.text8 = f'IDA* keskimäärin: {result[2]:.4f} sekuntia'
        self.text9 = ''
