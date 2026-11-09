from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile


class GameModel:
    """Représente le modèle global du jeu, gérant l'état actuel, le circuit et la voiture

    Attributs
    --------
    state: str
        État actuel du jeu (menu, course, etc.)
    circuit: Circuit | None
        Circuit chargé dans la partie
    car: Car | None
        Voiture présente dans la partie
    """

    def __init__(self):
        """Initialise le modèle du jeu avec un état initial de menu et aucun circuit ni voiture"""
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None

    def load_circuit(self) -> None:
        """Charge ou initialise le circuit du jeu sous forme d'une grille et fait apparaître la voiture"""
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for row_idx in range(GRID_COLS)] for col_idx in range(GRID_ROWS)]
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        """Fait apparaître la voiture sur le circuit à une position prédéfinie"""
        self.car = Car(7, 1)

    def update(self) -> None:
        """Met à jour l'état du modèle de jeu à chaque cycle si la course est en cours"""
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()