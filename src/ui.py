import pygame
from map import Map
from algorithm import astar, dijkstra


def ui(win, nrows, ncols, gsize):
# Gridin teko
	map = Map(win,nrows, ncols, gsize)
	map.make()
	map.generate_costs(5)

# Alkuasetukset
	startnode = None
	endnode = None
	run = True
	searchmode = 'D'
	diagonal = False
	animation = True
	maxcost = 5
	set_caption(searchmode, diagonal, animation)

# Event loop
	while run:
		map.draw()
		for event in pygame.event.get():

# Lopetus
			if event.type == pygame.QUIT:
				run = False

# Alku-, loppu-, ja esteiden pisteeiden syöttö (hiiren vasen näppäin)
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_clickpos(pos, gsize)
				node = map.nodes[row][col]
				if not startnode:
					startnode = node.set_start()
				elif not endnode and node != startnode:
					endnode = node.set_end()
				elif node != endnode and node != startnode:
					node.set_blocked()

# Esteiden pyyhkiminen (hiiren oikea näppäin)
			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = get_clickpos(pos, gsize)
				node = map.nodes[row][col]
				if node != startnode and node != endnode:
					node.clear()

			if event.type == pygame.KEYDOWN:

# Metodin valinta
				if event.key == pygame.K_m:
					if searchmode == 'D':
						searchmode = 'A'
					else:
						searchmode = 'D'
					set_caption(searchmode, diagonal, animation)

# Liikkeen tyypin valinta
				if event.key == pygame.K_d:
					if diagonal:
						diagonal = False
					else:
						diagonal = True
					set_caption(searchmode, diagonal, animation)

# Animaation valinta
				if event.key == pygame.K_a:
					if animation:
						animation = False
					else:
						animation = True
					set_caption(searchmode, diagonal, animation)

# Maxcost minus ja uusi kartta
				if event.key == pygame.K_MINUS:
					if maxcost > 1:
						maxcost -= 1
					startnode = None
					endnode = None
					map = Map(win,nrows, ncols, gsize)
					map.make()
					map.generate_costs(maxcost)

# Maxcost plus ja uusi kartta
				if event.key == pygame.K_PLUS:
					if maxcost < 20:
						maxcost += 1
					startnode = None
					endnode = None
					map = Map(win,nrows, ncols, gsize)
					map.make()
					map.generate_costs(maxcost)

# Uusi kartta
				if event.key == pygame.K_c:
					startnode = None
					endnode = None
					map = Map(win,nrows, ncols, gsize)
					map.make()
					map.generate_costs(maxcost)

# Laskennan aloitus
				if event.key == pygame.K_s:
					print(startnode,endnode)
					if startnode and endnode:
						if searchmode == 'D':
							dijkstra(map, startnode, endnode, diagonal, animation)
						else:
							astar(map, startnode, endnode, diagonal, animation)

# Uusi laskenta samalla kartalla
				if event.key == pygame.K_r:
					map.reset()

	pygame.quit()

# Klikkauksen koordinaatit
def get_clickpos(pos, gsize):
	col = pos[0] // gsize
	row = pos[1] // gsize
	return row, col

# Ikkunan otsikko
def set_caption(searchmode, diagonal, animation):
	if searchmode == 'D':
		caption = 'Paras reitti - Dijkstran menetelmä'
	else:
		caption = 'Paras reitti - A* menetelmä'
	if diagonal:
		caption += ' - diagonaalisuunnat'
	else:
		caption += ' - xy-suunnat'
	if animation:
		caption += ' - animaatiolla'
	else:
		caption += ' - ilman animaatiota'
	pygame.display.set_caption(caption)

