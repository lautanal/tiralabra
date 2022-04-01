import pygame
from map import Map
from algorithm import astar, dijkstra

class Ui:
	def __init__(self, win, nrows, ncols, gsize):
		self.win = win
		self.nrows = nrows
		self.ncols = ncols
		self.gsize = gsize

# Gridin teko
		self.map = Map(self.win, self.nrows, self.ncols, self.gsize)
		self.map.make()
		self.map.generate_costs(5)

# Alkuasetukset
		self.startnode = None
		self.endnode = None
		self.run = True
		self.searchmode = 'D'
		self.diagonal = False
		self.animation = False
		self.maxcost = 5
		self.set_caption()

	def start(self):
	# Event loop
		while self.run:
			self.map.draw()
			for event in pygame.event.get():

	# Lopetus
				if event.type == pygame.QUIT:
					self.run = False

	# Alku-, loppu-, ja esteiden pisteeiden syöttö (hiiren vasen näppäin)
				if pygame.mouse.get_pressed()[0]:
					pos = pygame.mouse.get_pos()
					row, col = self.get_clickpos(pos)
					node = self.map.nodes[row][col]
					if not self.startnode:
						self.startnode = node.set_start()
					elif not self.endnode and node != self.startnode:
						self.endnode = node.set_end()
					elif node != self.endnode and node != self.startnode:
						node.set_blocked()

	# Esteiden pyyhkiminen (hiiren oikea näppäin)
				elif pygame.mouse.get_pressed()[2]:
					pos = pygame.mouse.get_pos()
					row, col = self.get_clickpos(pos)
					node = self.map.nodes[row][col]
					if node == self.startnode:
						self.startnode = None
					if node == self.endnode:
						self.endnode = None
					node.clear()

				if event.type == pygame.KEYDOWN:

	# Metodin valinta
					if event.key == pygame.K_m:
						if self.searchmode == 'D':
							self.searchmode = 'A'
						else:
							self.searchmode = 'D'
						self.set_caption()

	# Polun tyypin valinta
					if event.key == pygame.K_d:
						if self.diagonal:
							self.diagonal = False
						else:
							self.diagonal = True
						self.set_caption()

	# Animaation valinta
					if event.key == pygame.K_a:
						if self.animation:
							self.animation = False
						else:
							self.animation = True
						self.set_caption()

	# Maxcost minus ja uusi kartta
					if event.key == pygame.K_MINUS:
						if self.maxcost > 1:
							self.maxcost -= 1
						self.startnode = None
						self.endnode = None
						self.map = Map(self.win,self.nrows, self.ncols, self.gsize)
						self.map.make()
						self.map.generate_costs(self.maxcost)

	# Maxcost plus ja uusi kartta
					if event.key == pygame.K_PLUS:
						if self.maxcost < 20:
							self.maxcost += 1
						self.startnode = None
						self.endnode = None
						self.map = Map(self.win,self.nrows, self.ncols, self.gsize)
						self.map.make()
						self.map.generate_costs(self.maxcost)

	# Uusi kartta
					if event.key == pygame.K_c:
						self.startnode = None
						self.endnode = None
						self.map = Map(self.win,self.nrows, self.ncols, self.gsize)
						self.map.make()
						self.map.generate_costs(self.maxcost)

	# Laskennan aloitus
					if event.key == pygame.K_s:
						print(self.startnode,self.endnode)
						if self.startnode and self.endnode:
							if self.searchmode == 'D':
								dijkstra(self.map, self.startnode, self.endnode, self.diagonal, self.animation)
							else:
								astar(self.map, self.startnode, self.endnode, self.diagonal, self.animation)

	# Uusi laskenta samalla kartalla
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
		if self.searchmode == 'D':
			caption = 'Paras reitti - Dijkstran menetelmä'
		else:
			caption = 'Paras reitti - A* menetelmä'
		if self.diagonal:
			caption += ' - diagonaalisuunnat'
		else:
			caption += ' - xy-suunnat'
		if self.animation:
			caption += ' - animaatiolla'
		else:
			caption += ' - ilman animaatiota'
		pygame.display.set_caption(caption)

