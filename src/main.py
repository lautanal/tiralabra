import pygame
from ui import Ui

WIDTH = 800
NCOLS = 60
NROWS = 60

if __name__ == "__main__":
# Gridin ruudun koko
	gsize = WIDTH // NCOLS

# Pygame ikkuna
	width = gsize * NCOLS
	height = gsize * NROWS
	pygame.init()
	win = pygame.display.set_mode((width, height))

# Käyttöliittymän käynnistys
	ui = Ui(win, NROWS, NCOLS, gsize)
	ui.start()