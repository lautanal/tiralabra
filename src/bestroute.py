from ui import Ui

WIDTH = 800
THEIGHT = 150
NCOLS = 40
NROWS = 40


if __name__ == "__main__":
    """Käyttöliittymän käynnistys.
    """
    ui = Ui(WIDTH, THEIGHT, NROWS, NCOLS)
    ui.start()
