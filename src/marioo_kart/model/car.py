import math
import pygame
from constants import (
    CAR_ACCELERATION, CAR_BRAKE, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)


class Car:
    """Représente une voiture dans le jeu, gérant sa position, sa vitesse, son angle et son affichage

    Attributs
    --------
    x: float
        Position horizontale de la voiture
    y: float
        Position verticale de la voiture
    speed: float
        Vitesse actuelle de la voiture
    angle: float
        Orientation de la voiture en degrés
    sprite: pygame.Surface
        Surface représentant visuellement la voiture
    """

    def __init__(self, start_col: int, start_row: int):
        """Initialise la voiture à une position de départ en grille avec une vitesse et un angle nuls

        Paramètres
        --------
        start_col: int
            Colonne de départ sur la grille
        start_row: int
            Ligne de départ sur la grille
        """
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()

    def accelerate(self, forward=True) -> None:
        """Modifie la vitesse de la voiture pour l'accélérer ou la faire reculer

        Paramètres
        --------
        forward: bool
            Indique si la voiture accélère vers l'avant (True) ou vers l'arrière (False)
        """
        if forward:
            self.speed += CAR_ACCELERATION
        else:
            self.speed -= CAR_ACCELERATION

    def brake(self) -> None:
        """Applique les freins pour réduire la vitesse de la voiture
        """
        self.speed /= CAR_BRAKE

    def update_position(self) -> None:
        """Met à jour la position verticale de la voiture en fonction de sa vitesse actuelle
        """
        self.y += self.speed

    def build_sprite(self) -> pygame.Surface:
        """Crée et renvoie la surface graphique représentant la voiture

        Retourne
        --------
        pygame.Surface
            Surface graphique de la voiture
        """
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Calcule et renvoie la surface et le rectangle de la voiture après rotation selon son angle

        Retourne
        --------
        tuple[pygame.Surface, pygame.Rect]
            Surface pivotée et son rectangle centré sur la position actuelle
        """
        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect