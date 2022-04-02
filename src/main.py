from ui import Ui

WIDTH = 800
NCOLS = 60
NROWS = 60

if __name__ == "__main__":
# Gridin ruudun koko
	gsize = WIDTH // NCOLS

# Pygame ikkunan koko
	width = gsize * NCOLS
	height = gsize * NROWS

# Käyttöliittymän käynnistys
	ui = Ui(NROWS, NCOLS, width, height, gsize)
	ui.start()