import pygame
from math import sqrt
from queue import PriorityQueue
from timeit import default_timer as timer
from node import Node
from map import Map

class Algorithm:
	def __init__(self, map):
		self.map = map
		self.method = 'D'
		self.diagonal = False
		self.animate = False
		self.start = None
		self.goal = None

	def set_method(self):
		if self.method == 'D':
			self.method = 'A'
		elif self.method == 'A':
			self.method = 'I'
		elif self.method == 'I':
			self.method = 'D'

	def set_diagonal(self):
		if self.diagonal:
			self.diagonal = False
		else:
			self.diagonal = True

	def set_animate(self):
		if self.animate:
			self.animate = False
		else:
			self.animate = True

	def set_map(self, map):
		self.map = map
		self.start = None
		self.goal = None

	def set_start(self, start):
		self.start = start

	def set_goal(self, goal):
		self.goal = goal

	def calculate(self):
		if self.method == 'D':
			return self.dijkstra()
		elif self.method == 'A':
			return self.a_star()
		elif self.method == 'I':
			return self.ida_star()


# Dijkstran algoritmi
	def dijkstra(self):
		tstart = timer()
		if self.diagonal:
			self.map.neighbors_diag()
		else:
			self.map.neighbors_xy()
		self.start.costsum = 0
		prqueue = PriorityQueue()
		prqueue.put((0, 0, self.start))
		count = 0

		while not prqueue.empty():
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			node = prqueue.get()[2]
			if node == self.goal:
				tend = timer()
				print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
				count = self.track_path()
				if not self.diagonal:
					costsum = node.costsum - (self.start.cost + self.goal.cost) / 2
				else:
					costsum = node.costsum
				return True, count, costsum, tend-tstart

			for neighbor in node.neighbors:
				deltacost = sqrt((node.row - neighbor.row)**2 + (node.col - neighbor.col)**2) * (node.cost + neighbor.cost) / 2
				newcostsum = node.costsum + deltacost
				if not neighbor.visited and newcostsum < neighbor.costsum:
					count += 1
					neighbor.previous = node
					neighbor.costsum = newcostsum
					prqueue.put((newcostsum, count, neighbor))

			node.set_visited(self.animate)

			if self.animate:
				self.map.draw()


		tend = timer()
		print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

		return False, 0, 0, 0


# A* -algoritmi
	def a_star(self):
		tstart = timer()
		if self.diagonal:
			self.map.neighbors_diag()
			heuristic = self.euclidian
		else:
			self.map.neighbors_xy()
			heuristic = self.manhattan
		self.start.costsum = 0
		prqueue = PriorityQueue()
		prqueue.put((0, 0, self.start))
		count = 0

		while not prqueue.empty():
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			node = prqueue.get()[2]
			if node == self.goal:
				tend = timer()
				print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
				count = self.track_path()
				if not self.diagonal:
					costsum = node.costsum - (self.start.cost + self.goal.cost) / 2
				else:
					costsum = node.costsum
				return True, count, costsum, tend-tstart

			for neighbor in node.neighbors:
				deltacost = sqrt((node.row - neighbor.row)**2+(node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
				newcostsum = node.costsum + deltacost
				if not neighbor.visited and newcostsum < neighbor.costsum:
					count += 1
					neighbor.previous = node
					neighbor.costsum = newcostsum
					fcostsum = newcostsum + heuristic(neighbor.get_pos(), self.goal.get_pos())
					prqueue.put((fcostsum, count, neighbor))

			node.set_visited(self.animate)

			if self.animate:
				self.map.draw()


		tend = timer()
		print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

		return False, 0, 0, 0

# IDA* -algoritmi
	def ida_star(self):
		tstart = timer()
		if self.diagonal:
			self.map.neighbors_diag()
			heuristic = self.euclidian
		else:
			self.map.neighbors_xy()
			heuristic = self.manhattan

		threshold = heuristic(self.start.get_pos(), self.goal.get_pos())
		while True:
			path = [self.start]		
			costsum = self.ida_star_search(path, 0, threshold, heuristic)
			if costsum == float("inf"):
				return False, 0, 0, 0
			elif costsum < 0:
				tend = timer()
				print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
				self.ida_path(path)
				count = len(path) - 2
				if not self.diagonal:
					costsum = -costsum - (self.start.cost + self.goal.cost) / 2
				else:
					costsum = -costsum
				return True, count, costsum, tend-tstart
			else:
				threshold = costsum


	def ida_star_search(self, path, costsum, threshold, heuristic):
		node = path[-1]
		node.set_visited(self.animate)
		if self.animate:
			self.map.draw()

		if node == self.goal:
			return -costsum

		estimate = costsum + heuristic(node.get_pos(), self.goal.get_pos())
		if estimate > threshold:
			return estimate

		tmin = float("inf")
		for neighbor in node.neighbors:
			if neighbor not in path:
				path.append(neighbor)
				deltacost = sqrt((node.row - neighbor.row)**2+(node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
				newcostsum = costsum + deltacost
				
				res = self.ida_star_search(path, newcostsum, threshold, heuristic)
				if res < 0:
					return res
				elif res < tmin:
					tmin = res
				path.pop()

		return tmin

# Manhattan-heuristiikka
	def manhattan(self, p1, p2):
		y1, x1 = p1
		y2, x2 = p2
		return abs(x1 - x2) + abs(y1 - y2)

# Euklidiininen heuristiikka
	def euclidian(self, p1,p2):
		y1, x1 = p1
		y2, x2 = p2
		return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Polun track, Dijkstra ja A*
	def track_path(self):
		node = self.goal.previous
		count = 0
		while node != self.start:
			count += 1
			node.mark_path()
			node = node.previous
		return count

# Polun track, IDA*
	def ida_path(self, path):
		for node in path:
			if node != self.start and node != self.goal:
				node.mark_path()

