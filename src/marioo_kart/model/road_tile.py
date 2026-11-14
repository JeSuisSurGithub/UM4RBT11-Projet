import pygame
from constants import TILE_SIZE, C1_COLOR, C2_COLOR


class RoadTile:
    """Représente une tuile individuelle de route sur le circuit

    Attributs
    --------
    col: int
        Indice de la colonne de la tuile
    row: int
        Indice de la ligne de la tuile
    sprite: pygame.Surface | None
        Surface graphique représentant la tuile
    """

    def __init__(self, col: int, row: int):
        """Initialise une tuile de route avec ses coordonnées de colonne et de ligne

        Paramètres
        --------
        col: int
            Indice de la colonne
        row: int
            Indice de la ligne
        """
        self.col = col
        self.row = row
        self.sprite: pygame.Surface | None = None
        self.color : tuple | None

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        """Génère et renvoie la surface graphique représentant la tuile de route

        Paramètres
        --------
        tile_size: int
            Taille de la tuile en pixels

        Retourne
        --------
        pygame.Surface
            Surface graphique de la tuile
        """
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill(self.color)
        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite