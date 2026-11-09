from model.road_tile import RoadTile
from constants import TILE_SIZE


class Circuit:
    """Représente le circuit du jeu sous forme d'une grille de tuiles de route

    Attributs
    --------
    grid: list[list[RoadTile]]
        Grille bidimensionnelle représentant le circuit
    rows: int
        Nombre de lignes dans la grille
    cols: int
        Nombre de colonnes dans la grille
    """

    def __init__(self,  grid: list[list[RoadTile]]):
        """Initialise le circuit avec une grille de tuiles donnée

        Paramètres
        --------
        grid: list[list[RoadTile]]
            Grille à deux dimensions représentant le circuit
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

    def get_tile(self, col: int, row: int) -> RoadTile | None:
        """Récupère la tuile située à une colonne et une ligne données, ou None si hors limites

        Paramètres
        --------
        col: int
            Indice de la colonne
        row: int
            Indice de la ligne

        Retourne
        --------
        RoadTile | None
            La tuile correspondante ou None
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def get_tile_at_pixel(self, px: float, py: float) -> RoadTile | None:
        """Récupère la tuile située aux coordonnées en pixels (px, py)

        Paramètres
        --------
        px: float
            Position horizontale en pixels
        py: float
            Position verticale en pixels

        Retourne
        --------
        RoadTile | None
            La tuile correspondante ou None
        """
        col = int(px // TILE_SIZE)
        row = int(py // TILE_SIZE)
        return self.get_tile(col, row)

    def pixel_width(self) -> int:
        """Calcule et renvoie la largeur totale du circuit en pixels

        Retourne
        --------
        int
            Largeur totale en pixels
        """
        return self.cols * TILE_SIZE

    def pixel_height(self) -> int:
        """Calcule et renvoie la hauteur totale du circuit en pixels

        Retourne
        --------
        int
            Hauteur totale en pixels
        """
        return self.rows * TILE_SIZE