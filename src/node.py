import pygame
from queue import PriorityQueue

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)

class Node:
	def __init__(self, row, col, gsize):
		self.row = row
		self.col = col
		self.x = col * gsize
		self.y = row * gsize
		self.gsize = gsize
		self.color = WHITE
		self.start = False
		self.end = False
		self.blocked = False
		self.visited = False
		self.previous = None
		self.neighbors = []
		self.cost = 11
		self.costsum = float("inf")

	def clear(self):
		self.start = False
		self.end = False
		self.blocked = False
		ngrey = (10 - self.cost) * 24
		self.color = (ngrey,ngrey,ngrey)

	def get_pos(self):
		return self.row, self.col

	def mark_path(self):
		self.color = RED

	def set_blocked(self):
		self.blocked = True
		self.color = BLACK

	def set_end(self):
		self.end = True
		self.blocked = False
		self.color = ORANGE
		return self

	def set_start(self):
		self.start = True
		self.blocked = False
		self.color = BLUE
		return self

	def set_visited(self, animate):
		self.visited = True
		if animate and not self.start:
			self.color = GREEN

