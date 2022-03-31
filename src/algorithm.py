import pygame
from math import sqrt
from queue import PriorityQueue
from timeit import default_timer as timer
from node import Node


# Dijkstran algoritmi
def dijkstra(map, start, end, diagonal, animate):
	tstart = timer()
	if diagonal:
		map.initnodes_diag()
	else:
		map.initnodes_xy()
	start.costsum = 0
	prqueue = PriorityQueue()
	prqueue.put((0, 0, start))
	count = 0

	while not prqueue.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		node = prqueue.get()[2]
		if node == end:
			tend = timer()
			print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
			track_path(start, end)
			map.draw()
			return True

		for neighbor in node.neighbors:
			deltacost = sqrt((node.row - neighbor.row)**2 + (node.col - neighbor.col)**2) * (node.cost + neighbor.cost) / 2
			newcostsum = node.costsum + deltacost
			if not neighbor.visited and newcostsum < neighbor.costsum:
				count += 1
				neighbor.previous = node
				neighbor.costsum = newcostsum
				prqueue.put((newcostsum, count, neighbor))

		if animate:
			map.draw()

		node.set_visited(animate)

	tend = timer()
	print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

	return False


# A* -algoritmi
def astar(map, start, end, diagonal, animate):
	tstart = timer()
	if diagonal:
		map.initnodes_diag()
		heuristic = euclidian
	else:
		map.initnodes_xy()
		heuristic = manhattan
	start.costsum = 0
	prqueue = PriorityQueue()
	prqueue.put((0, 0, start))
	count = 0

	while not prqueue.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		node = prqueue.get()[2]
		if node == end:
			tend = timer()
			print(f'*** REITTI LÖYTYI ***\nLaskenta vei {tend-tstart:.3f} sekuntia')
			track_path(start, end)
			map.draw()
			return True

		for neighbor in node.neighbors:
			deltacost = sqrt((node.row - neighbor.row)**2+(node.col - neighbor.col)**2) * (node.cost + neighbor.cost)/2
			newcostsum = node.costsum + deltacost
			if not neighbor.visited and newcostsum < neighbor.costsum:
				count += 1
				neighbor.previous = node
				neighbor.costsum = newcostsum
				fcostsum = newcostsum + heuristic(neighbor.get_pos(), end.get_pos())
				prqueue.put((fcostsum, count, neighbor))

		if animate:
			map.draw()

		node.set_visited(animate)

	tend = timer()
	print(f'*** Reittiä ei löytynyt ***\nLaskenta vei {tend-tstart:.3f} sekuntia')

	return False


# Manhattan-heuristiikka
def manhattan(p1, p2):
	y1, x1 = p1
	y2, x2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

# Euklidiininen heuristiikka
def euclidian(p1,p2):
	y1, x1 = p1
	y2, x2 = p2
	return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Polun track
def track_path(start, end):
	node = end.previous
	while node != start:
		node.mark_path()
		node = node.previous
	end.set_end()


