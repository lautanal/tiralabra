from ui import Ui


MAXWIDTH = 1200
MAXHEIGHT = 1000
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
