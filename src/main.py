import pygame
from ui import ui

WIDTH = 800
NCOLS = 50
NROWS = 40

if __name__ == "__main__":
# Gridin ruudun koko
	gsize = int(WIDTH / NCOLS)

# Pygame ikkuna
	height = gsize * NROWS
	pygame.init()
	win = pygame.display.set_mode((WIDTH, height))

# Käyttöliittymän käynnistys
	ui(win, NROWS, NCOLS, gsize)