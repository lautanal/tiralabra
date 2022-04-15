from ui import Ui

WIDTH = 1200
THEIGHT = 150
NCOLS = 20
NROWS = 20

# Käyttöliittymän käynnistys
if __name__ == "__main__":
    ui = Ui(WIDTH, THEIGHT, NROWS, NCOLS)
    ui.start()
