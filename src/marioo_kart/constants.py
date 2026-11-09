WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

CAR_ACCELERATION = 0.05
CAR_BRAKE = 1.1
CAR_WIDTH = 30
CAR_HEIGHT = 50


class GameState:
    """Définit les différents états possibles du jeu

    Attributs
    --------
    MENU: str
        État correspondant au menu principal
    RACING: str
        État correspondant à la course en cours
    """
    MENU = "menu"
    RACING = "racing"


COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)