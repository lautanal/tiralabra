import pygame
from map import Map
from algorithm import Algorithm

class Ui:
	def __init__(self, nrows, ncols, width, height, gsize):
# Pygame-ikkuna
		pygame.init()
		self.win = pygame.display.set_mode((width, height))
		self.nrows = nrows
		self.ncols = ncols
		self.width = width
		self.height = height
		self.gsize = gsize

# Karttaruudukon teko
		self.map = Map(self.win, self.nrows, self.ncols, self.width, self.height, self.gsize)
		self.map.make()
		self.map.generate_costs(5)

# Algoritmin alustus
		self.algorithm = Algorithm(self.map)

# Alkuasetukset
		self.run = True
		self.maxcost = 5
		self.set_caption()

# Käyttöliittymä
	def start(self):
	# Event loop
		while self.run:
			self.map.draw()
			for event in pygame.event.get():

	# Lopetus
				if event.type == pygame.QUIT:
					self.run = False

	# Alku-, loppupisteet, ja esteiden syöttö (hiiren vasen näppäin)
				if pygame.mouse.get_pressed()[0]:
					pos = pygame.mouse.get_pos()
					row, col = self.get_clickpos(pos)
					node = self.map.nodes[row][col]
					if not self.algorithm.start:
						node.set_start()
						self.algorithm.set_start(node)
					elif not self.algorithm.end and node != self.algorithm.start:
						node.set_end()
						self.algorithm.set_end(node)
					elif node != self.algorithm.end and node != self.algorithm.start:
						node.set_blocked()

	# Pisteiden pyyhkiminen (hiiren oikea näppäin)
				elif pygame.mouse.get_pressed()[2]:
					pos = pygame.mouse.get_pos()
					row, col = self.get_clickpos(pos)
					node = self.map.nodes[row][col]
					if node == self.algorithm.start:
						self.algorithm.set_start(None)
					if node == self.algorithm.end:
						self.algorithm.set_end(None)
					node.clear()

				if event.type == pygame.KEYDOWN:

	# Metodin valinta
					if event.key == pygame.K_m:
						self.algorithm.set_method()
						self.set_caption()

	# Polun tyypin valinta
					if event.key == pygame.K_d:
						self.algorithm.set_diagonal()
						self.set_caption()

	# Animaation valinta
					if event.key == pygame.K_a:
						self.algorithm.set_animate()
						self.set_caption()

	# Maxcost minus ja uusi kartta
					if event.key == pygame.K_MINUS:
						if self.maxcost > 1:
							self.maxcost -= 1
						self.map = Map(self.win, self.nrows, self.ncols, self.width, self.height, self.gsize)
						self.map.make()
						self.map.generate_costs(self.maxcost)
						self.algorithm.set_map(self.map)
						self.algorithm.set_start(None)
						self.algorithm.set_end(None)

	# Maxcost plus ja uusi kartta
					if event.key == pygame.K_PLUS:
						if self.maxcost < 20:
							self.maxcost += 1
						self.map = Map(self.win, self.nrows, self.ncols, self.width, self.height, self.gsize)
						self.map.make()
						self.map.generate_costs(self.maxcost)
						self.algorithm.set_map(self.map)
						self.algorithm.set_start(None)
						self.algorithm.set_end(None)

	# Uusi kartta
					if event.key == pygame.K_c:
						self.map = Map(self.win, self.nrows, self.ncols, self.width, self.height, self.gsize)
						self.map.make()
						self.map.generate_costs(self.maxcost)
						self.algorithm.set_map(self.map)
						self.algorithm.set_start(None)
						self.algorithm.set_end(None)

	# Uusi kartta 1 TIEDOSTOSTA
					if event.key == pygame.K_1:
						self.map = Map(self.win, self.nrows, self.ncols, self.width, self.height, self.gsize)
						self.map.make()
						self.map.read("maps/1.map")
						self.algorithm.set_map(self.map)
						self.algorithm.set_start(None)
						self.algorithm.set_end(None)

	# Uusi kartta 2 TIEDOSTOSTA
					if event.key == pygame.K_2:
						self.map = Map(self.win, self.nrows, self.ncols, self.width, self.height, self.gsize)
						self.map.make()
						self.map.read("maps/2.map")
						self.algorithm.set_map(self.map)
						self.algorithm.set_start(None)
						self.algorithm.set_end(None)

	# Uusi kartta 3 TIEDOSTOSTA
					if event.key == pygame.K_3:
						self.map = Map(self.win, self.nrows, self.ncols, self.width, self.height, self.gsize)
						self.map.make()
						self.map.read("maps/3.map")
						self.algorithm.set_map(self.map)
						self.algorithm.set_start(None)
						self.algorithm.set_end(None)

	# Laskennan aloitus
					if event.key == pygame.K_s:
						if self.algorithm.start and self.algorithm.end:
							self.map.reset()
							self.algorithm.calculate()

	# Reset, uusi laskenta samalla kartalla
					if event.key == pygame.K_r:
						self.map.reset()

		pygame.quit()

	# Klikkauksen koordinaatit
	def get_clickpos(self, pos):
		col = pos[0] // self.gsize
		row = pos[1] // self.gsize
		return row, col

	# Ikkunan otsikko
	def set_caption(self):
		if self.algorithm.method == 'D':
			caption = 'Paras reitti - Dijkstran menetelmä'
		else:
			caption = 'Paras reitti - A* menetelmä'
		if self.algorithm.diagonal:
			caption += ' - diagonaalisuunnat'
		else:
			caption += ' - xy-suunnat'
		if self.algorithm.animate:
			caption += ' - animaatio'
		else:
			caption += ' - ilman animaatiota'
		pygame.display.set_caption(caption)

