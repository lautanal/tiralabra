from ui import Ui

WIDTH = 800
THEIGHT = 200
NCOLS = 20
NROWS = 20

if __name__ == "__main__":
# Käyttöliittymän käynnistys
	ui = Ui(WIDTH, THEIGHT, NROWS, NCOLS)
	ui.start()