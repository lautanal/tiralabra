import pygame
import numpy as np
from node import Node

WHITE = (255, 255, 255)
GREY = (128, 128, 128)

class Map:
	def __init__(self, win, rows, cols, gsize):
		self.win = win
		self.rows = rows
		self.cols = cols
		self.gsize = gsize
		self.nodes = []

# Solmujen luonti
	def make(self):
		for i in range(self.rows):
			self.nodes.append([])
			for j in range(self.cols):
				node = Node(i, j, self.gsize)
				self.nodes[i].append(node)

# Kartan generointi
	def generate_costs(self,levels):
		costmap = np.random.randint(1, levels+1, size=(self.rows, self.cols))
		for row in self.nodes:
			for node in row:
				node.cost = costmap[node.row][node.col]
				ngrey = (20 - node.cost) * 12
				node.color = (ngrey,ngrey,ngrey)

# Solmujen alustus laskentaa varten, xy-liike
	def initnodes_xy(self):
		for row in self.nodes:
			for node in row:
				node.costsum = float("inf")

				node.neighbors = []
				if node.row < self.rows - 1 and not self.nodes[node.row + 1][node.col].blocked:
					node.neighbors.append(self.nodes[node.row + 1][node.col])

				if node.row > 0 and not self.nodes[node.row - 1][node.col].blocked:
					node.neighbors.append(self.nodes[node.row - 1][node.col])

				if node.col < self.cols - 1 and not self.nodes[node.row][node.col + 1].blocked:
					node.neighbors.append(self.nodes[node.row][node.col + 1])

				if node.col > 0 and not self.nodes[node.row][node.col - 1].blocked:
					node.neighbors.append(self.nodes[node.row][node.col - 1])

# Solmujen alustus laskentaa varten, diagonaaliset liikkeet
	def initnodes_diag(self):
		for row in self.nodes:
			for node in row:
				node.costsum = float("inf")

				node.neighbors = []
				if node.row < self.rows - 1 and not self.nodes[node.row + 1][node.col].blocked:
					node.neighbors.append(self.nodes[node.row + 1][node.col])
					if node.col < self.cols - 1 and not self.nodes[node.row + 1][node.col + 1].blocked:
						node.neighbors.append(self.nodes[node.row + 1][node.col + 1])
					if node.col > 0 and not self.nodes[node.row + 1][node.col - 1].blocked:
						node.neighbors.append(self.nodes[node.row + 1][node.col - 1])

				if node.row > 0 and not self.nodes[node.row - 1][node.col].blocked:
					node.neighbors.append(self.nodes[node.row - 1][node.col])
					if node.col < self.cols - 1 and not self.nodes[node.row - 1][node.col + 1].blocked:
						node.neighbors.append(self.nodes[node.row - 1][node.col + 1])
					if node.col > 0 and not self.nodes[node.row - 1][node.col - 1].blocked:
						node.neighbors.append(self.nodes[node.row - 1][node.col - 1])

				if node.col < self.cols - 1 and not self.nodes[node.row][node.col + 1].blocked:
					node.neighbors.append(self.nodes[node.row][node.col + 1])

				if node.col > 0 and not self.nodes[node.row][node.col - 1].blocked:
					node.neighbors.append(self.nodes[node.row][node.col - 1])

# Kartan reset
	def reset(self):
		for row in self.nodes:
			for node in row:
				if not node.start and not node.end and not node.blocked:
					ngrey = (20 - node.cost) * 12
					node.color = (ngrey,ngrey,ngrey)
					node.visited = False

# Kartan piirtäminen
	def draw(self):
		self.win.fill(WHITE)
		font = pygame.font.SysFont('Arial', self.gsize // 2)

		for row in self.nodes:
			for node in row:
				pygame.draw.rect(self.win, node.color, (node.x, node.y, self.gsize, self.gsize))
				if node.cost < 10:
					self.win.blit(font.render(str(node.cost), True, (128,128,128)), (node.x+2*(self.gsize//5), node.y+self.gsize//4))
				else:
					self.win.blit(font.render(str(node.cost), True, (128,128,128)), (node.x+self.gsize//3, node.y+self.gsize//4))

		for i in range(self.rows):
			pygame.draw.line(self.win, GREY, (0, i * self.gsize), (self.cols * self.gsize, i * self.gsize))
		for j in range(self.cols):
			pygame.draw.line(self.win, GREY, (j * self.gsize, 0), (j * self.gsize, self.rows * self.gsize))

		pygame.display.update()



