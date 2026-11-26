import pygame
from constants import GameState, GRID_ROWS, GRID_COLS, TileType, TERRAINS
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

    def load_circuit(self, choice) -> None:
        """Charge ou initialise le circuit (1 ou 2) du jeu sous forme d'une grille et fait apparaître la voiture"""
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for row_idx in range(GRID_COLS)] for col_idx in range(GRID_ROWS)]
        if choice == pygame.K_1:
            RoadTile.type = TileType.ROUTE
        elif choice == pygame.K_2:
            RoadTile.type = TileType.GLACE

        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        """Fait apparaître la voiture sur le circuit à une position prédéfinie"""
        self.car = Car(7, 1)

    def update(self) -> None:
        """Met à jour l'état du modèle de jeu à chaque cycle si la course est en cours"""
        if self.state != GameState.RACING or self.circuit is None:
            return
        _, bounds = self.car.get_rotated_sprite()
        tiletype = self.circuit.get_tile_at_pixel(bounds.centerx, bounds.centery).type
        self.car.update_position(tiletype)

    def nokey(self) ->None:
        """Traite le cas ou aucune touche est appuyée durant la course (Racing = True)"""
        if self.state != GameState.RACING or self.circuit is None:
            return 
        if self.car.speed != 0.0 : 
            self.car.speed = 0.0