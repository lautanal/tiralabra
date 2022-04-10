from ui import Ui

WIDTH = 800
THEIGHT = 200
NCOLS = 20
NROWS = 20

# Käyttöliittymän käynnistys
if __name__ == "__main__":
    ui = Ui(WIDTH, THEIGHT, NROWS, NCOLS)
    ui.start()
