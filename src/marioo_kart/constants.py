WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

CAR_ACCEL = 0.1
CAR_SPEED_MAX = 9
CAR_SPEED_DECAY = 0.1
CAR_ANGULAR_ACCEL = 0.1
CAR_ANGULAR_DECAY = 0.5
CAR_BRAKE = 0.4
CAR_WIDTH = 30
CAR_HEIGHT = 50
OVERDRIFT_WEIGHT = 0.2

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

class TileType:
    ROUTE = "ROUTE"
    GLACE = "GLACE"

class Terrain:
    def __init__(self, color, traction, lat_grip, drift_threshold):
        self.color = color
        self.traction = traction
        self.lat_grip = lat_grip
        self.drift_threshold = drift_threshold

TERRAINS = {
    "ROUTE":
        Terrain(
            color = (127, 127, 127),
            traction = 2,
            lat_grip = 0.3,
            drift_threshold = 2.2,
        ),
    "GLACE":
        Terrain(
            color = (0, 0, 255),
            traction = 0.5,
            lat_grip = 0.03,
            drift_threshold = 0.22,
        )
}