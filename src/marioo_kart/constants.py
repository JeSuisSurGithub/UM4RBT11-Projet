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
    CIRCUIT: str 
        Etat pour choisir le circuit
    RACING: str
        État correspondant à la course en cours
    """
    MENU = "menu"
    CIRCUIT = "circuit"
    RACING = "racing"


COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)

# Couleur du premier circuit 
C1_COLOR = (80, 80, 20)

# Couleur du deuxieme circuit 
C2_COLOR = (30, 30, 100)