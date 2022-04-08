import pygame
import numpy as np
from node import Node

class Map:
	def __init__(self, win, nrows, ncols, width, height, gsize):
		self.win = win
		self.nrows = nrows
		self.ncols = ncols
		self.width = width
		self.height = height
		self.gsize = gsize
		self.nodes = []
		self.text1 = ''
		self.text2 = ''
		self.text3 = ''
		self.text4 = ''
		self.text5 = ''
		self.text6 = ''
		self.make()


# Solmujen luonti
	def make(self):
		for i in range(self.nrows):
			self.nodes.append([])
			for j in range(self.ncols):
				node = Node(i, j, self.gsize)
				self.nodes[i].append(node)

# Kartan random-generointi (solmujen painot)
	def generate_costs(self,levels):
		costmap = np.random.randint(1, levels+1, size=(self.nrows, self.ncols))
		for row in self.nodes:
			for node in row:
				node.cost = costmap[node.row][node.col]
				ngrey = (10 - node.cost) * 24
				node.color = (ngrey,ngrey,ngrey)

# Kartan generointi (kartta luettu tiedostosta)
	def set_costs(self, map):
		for row in self.nodes:
			for node in row:
				if map[node.row][node.col] == 'B':
					node.cost = 11
					node.blocked = True
					node.color = (0,0,0)
				else:
					node.cost = int(map[node.row][node.col])
					ngrey = (10 - node.cost) * 24
					node.color = (ngrey,ngrey,ngrey)

# Kartan piirtäminen
	def draw(self):
		font = pygame.font.SysFont('Arial', self.gsize // 2)
		for row in self.nodes:
			for node in row:
				pygame.draw.rect(self.win, node.color, (node.x, node.y, self.gsize, self.gsize))
				if not node.blocked:
					if node.cost < 10:
						self.win.blit(font.render(str(node.cost), True, (128,128,128)), (node.x+2*(self.gsize//5), node.y+self.gsize//4))
					else:
						self.win.blit(font.render(str(node.cost), True, (128,128,128)), (node.x+self.gsize//3, node.y+self.gsize//4))

		for i in range(self.nrows):
			pygame.draw.line(self.win, (128,128,128), (0, i * self.gsize), (self.ncols * self.gsize, i * self.gsize))
		for j in range(self.ncols):
			pygame.draw.line(self.win, (128,128,128), (j * self.gsize, 0), (j * self.gsize, self.nrows * self.gsize))
		
		pygame.draw.rect(self.win, (180,180,180), (0, self.nrows*self.gsize, self.width, self.height-self.nrows*self.gsize))
		pygame.draw.line(self.win, (60,60,60), (0, self.nrows*self.gsize), (self.ncols * self.gsize, self.nrows*self.gsize))

		font = pygame.font.SysFont('Arial', 15)
		self.win.blit(font.render(str(self.text1), True, (64,64,64)), (self.width/20, self.nrows*self.gsize + 20))
		self.win.blit(font.render(str(self.text2), True, (64,64,64)), (self.width/20, self.nrows*self.gsize + 45))
		self.win.blit(font.render(str(self.text3), True, (64,64,64)), (self.width/20, self.nrows*self.gsize + 70))
		self.win.blit(font.render(str(self.text4), True, (64,64,64)), (self.width/20, self.nrows*self.gsize + 110))
		self.win.blit(font.render(str(self.text5), True, (64,64,64)), (self.width/20, self.nrows*self.gsize + 135))
		self.win.blit(font.render(str(self.text6), True, (64,64,64)), (self.width/20, self.nrows*self.gsize + 160))

		pygame.display.update()

# Kartan reset
	def reset(self):
		for row in self.nodes:
			for node in row:
				node.visited = False
				if not node.start and not node.end and not node.blocked:
					ngrey = (10 - node.cost) * 24
					node.color = (ngrey,ngrey,ngrey)

# Solmujen naapurit, xy-polku
	def neighbors_xy(self):
		for row in self.nodes:
			for node in row:
				node.costsum = float("inf")

				node.neighbors = []
				if node.row < self.nrows - 1 and not self.nodes[node.row + 1][node.col].blocked:
					node.neighbors.append(self.nodes[node.row + 1][node.col])

				if node.row > 0 and not self.nodes[node.row - 1][node.col].blocked:
					node.neighbors.append(self.nodes[node.row - 1][node.col])

				if node.col < self.ncols - 1 and not self.nodes[node.row][node.col + 1].blocked:
					node.neighbors.append(self.nodes[node.row][node.col + 1])

				if node.col > 0 and not self.nodes[node.row][node.col - 1].blocked:
					node.neighbors.append(self.nodes[node.row][node.col - 1])

# Solmujen naapurit, viisto polku
	def neighbors_diag(self):
		for row in self.nodes:
			for node in row:
				node.costsum = float("inf")

				node.neighbors = []
				if node.row < self.nrows - 1:
					if not self.nodes[node.row + 1][node.col].blocked:
						node.neighbors.append(self.nodes[node.row + 1][node.col])
					if node.col < self.ncols - 1 and not self.nodes[node.row + 1][node.col + 1].blocked:
						node.neighbors.append(self.nodes[node.row + 1][node.col + 1])
					if node.col > 0 and not self.nodes[node.row + 1][node.col - 1].blocked:
						node.neighbors.append(self.nodes[node.row + 1][node.col - 1])

				if node.row > 0:
					if not self.nodes[node.row - 1][node.col].blocked:
						node.neighbors.append(self.nodes[node.row - 1][node.col])
					if node.col < self.ncols - 1 and not self.nodes[node.row - 1][node.col + 1].blocked:
						node.neighbors.append(self.nodes[node.row - 1][node.col + 1])
					if node.col > 0 and not self.nodes[node.row - 1][node.col - 1].blocked:
						node.neighbors.append(self.nodes[node.row - 1][node.col - 1])

				if node.col < self.ncols - 1 and not self.nodes[node.row][node.col + 1].blocked:
					node.neighbors.append(self.nodes[node.row][node.col + 1])

				if node.col > 0 and not self.nodes[node.row][node.col - 1].blocked:
					node.neighbors.append(self.nodes[node.row][node.col - 1])

