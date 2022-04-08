from ui import Ui

HEIGHT = 1000
WIDTH = 800
NCOLS = 40
NROWS = 40

if __name__ == "__main__":
# Käyttöliittymän käynnistys
	ui = Ui(NROWS, NCOLS, WIDTH, HEIGHT)
	ui.start()