from ui import Ui

WIDTH = 1200
THEIGHT = 150
NCOLS = 100
NROWS = 100


if __name__ == "__main__":
    """Käyttöliittymän käynnistys.
    """
    ui = Ui(WIDTH, THEIGHT, NROWS, NCOLS)
    ui.start()
