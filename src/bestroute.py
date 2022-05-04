from ui import Ui


MAXWIDTH = 1600
MAXHEIGHT = 1200
THEIGHT = 150
NCOLS = 100
NROWS = 100


def main():
    """Käyttöliittymän käynnistys.
    """
    ui = Ui(MAXWIDTH, MAXHEIGHT, THEIGHT, NROWS, NCOLS)
    ui.start()


if __name__ == "__main__":
    main()
