import pygame


class Draw:
    def __init__(self, win, width, height, map):
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

    # Koko kartan piirtäminen
    def drawmap(self):
        font = pygame.font.SysFont('Arial', self.gsize // 2)
        for row in self.map.nodes:
            for node in row:
                pygame.draw.rect(self.win, node.color, (node.x, node.y, self.gsize, self.gsize))
                if not node.blocked:
                    if node.cost < 10:
                        self.win.blit(font.render(str(node.cost), True, (128, 128, 128)),
                                (node.x+2*(self.gsize//5), node.y+self.gsize//4))
                    else:
                        self.win.blit(font.render(str(node.cost), True, (128, 128, 128)),
                                (node.x+self.gsize//3, node.y+self.gsize//4))

        for i in range(self.nrows):
            pygame.draw.line(self.win, (128, 128, 128), (0, i * self.gsize), (self.width, i * self.gsize))
        for j in range(self.ncols):
            pygame.draw.line(self.win, (128, 128, 128), (j * self.gsize, 0), (j * self.gsize, self.nrows * self.gsize))

        pygame.draw.rect(self.win, (180, 180, 180), (0, self.nrows*self.gsize, self.width,
                self.height-self.nrows*self.gsize))
        pygame.draw.line(self.win, (60, 60, 60), (0, self.nrows*self.gsize), (self.width, self.nrows*self.gsize))

        font = pygame.font.SysFont('Arial', 15)
        self.win.blit(font.render(str(self.text1), True, (64, 64, 64)), (40, self.nrows*self.gsize + 20))
        self.win.blit(font.render(str(self.text2), True, (64, 64, 64)), (40, self.nrows*self.gsize + 45))
        self.win.blit(font.render(str(self.text3), True, (64, 64, 64)), (40, self.nrows*self.gsize + 70))
        self.win.blit(font.render(str(self.text4), True, (64, 64, 64)), (40, self.nrows*self.gsize + 95))
        self.win.blit(font.render(str(self.text5), True, (64, 64, 64)), (self.width // 2, self.nrows*self.gsize + 20))
        self.win.blit(font.render(str(self.text6), True, (64, 64, 64)), (self.width // 2, self.nrows*self.gsize + 45))
        self.win.blit(font.render(str(self.text7), True, (64, 64, 64)), (self.width // 2, self.nrows*self.gsize + 70))

        pygame.display.update()

    # Yksittäisen ruudun piirtäminen
    def drawnode(self, node):
        font = pygame.font.SysFont('Arial', self.gsize // 2)
        pygame.draw.rect(self.win, node.color, (node.x, node.y, self.gsize, self.gsize))
        if node.cost < 10:
            self.win.blit(font.render(str(node.cost), True, (128, 128, 128)),
                    (node.x+2*(self.gsize//5), node.y+self.gsize//4))
        else:
            self.win.blit(font.render(str(node.cost), True, (128, 128, 128)),
                    (node.x+self.gsize//3, node.y+self.gsize//4))
        pygame.display.update()

    # Kartan reset
    def reset(self):
        for row in self.map.nodes:
            for node in row:
                node.visited = False
                if not node.start and not node.goal and not node.blocked:
                    ngrey = (10 - node.cost) * 24
                    node.color = (ngrey, ngrey, ngrey)

    # Ikkunan asetukset
    def set_win(self, win, width, height, map):
        self.win = win
        self.map = map
        self.width = width
        self.height = height
        self.nrows = map.nrows
        self.ncols = map.ncols
        self.gsize = map.gsize

    # Ikkunan tekstit
    def set_texts(self, algorithm):
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
        self.text6 = ''
        self.text7 = ''

    # Laskennan tulokset näkyville
    def set_results(self, result):
        if result[0]:
            self.text5 = f'Polun pituus {result[1]}'
            self.text6 = f'Polun painotettu pituus {result[2]:.1f}'
            self.text7 = f'Laskenta vei {result[3]:.3f} sekuntia'
            self.text8 = ''
        else:
            self.text5 = '*** REITTIÄ EI LÖYTYNYT ***'
            self.text6 = ''
            self.text7 = ''
            self.text8 = ''

