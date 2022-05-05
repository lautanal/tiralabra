import pygame
from ui import Ui


WIDTHMARGIN = 0
HEIGHTMARGIN = 150
THEIGHT = 150
NCOLS = 200
NROWS = 100


def main():
    """Käyttöliittymän käynnistys.
    """
    pygame.init()
    infoObject = pygame.display.Info()
    maxw = infoObject.current_w - WIDTHMARGIN
    maxh = infoObject.current_h - HEIGHTMARGIN
    ui = Ui(maxw, maxh, THEIGHT, NROWS, NCOLS)
    ui.start()


if __name__ == "__main__":
    main()
