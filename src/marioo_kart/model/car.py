import math
import pygame
from constants import (
    CAR_ACCEL, CAR_SPEED_MAX, CAR_ANGULAR_ACCEL, CAR_BRAKE,
    CAR_ANGULAR_DECAY, CAR_SPEED_DECAY, OVERDRIFT_WEIGHT,
    CAR_WIDTH, CAR_HEIGHT,
    TILE_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH, TileType, TERRAINS
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
        self.angle: float = -math.pi/2
        self.agl_speed: float = 0.0
        self.speed: pygame.Vector2 = pygame.Vector2(0.0, 0.0)
        self.sprite = self.build_sprite()
        self.tiletype: TileType | None = TileType.ROUTE

    def decay2rate(scalar, decay):
        """
            Fonction d'aide pour réduire linéairement une valeur à 0 sous forme de facteur
        Paramètres
        --------
        scalar: float
            Valeur visée
        decay: float
            Valeur à soustraire 
        """
        if scalar <= decay:
            return 0
        else:
            return (scalar - decay) / scalar

    def accelerate(self, forward=True) -> None:
        """Modifie la vitesse de la voiture pour l'accélérer ou la faire reculer

        Paramètres
        --------
        forward: bool
            Indique si la voiture accélère vers l'avant (True) ou vers l'arrière (False)
        """
        rad = math.radians(self.angle)
        forward_vector = pygame.Vector2(math.sin(rad), -math.cos(rad))
        terrain = TERRAINS[self.tiletype]

        # Si l'utilisateur ne fait rien
        if forward is None:
            norm = self.speed.magnitude()
            self.speed.x *= Car.decay2rate(norm, CAR_SPEED_DECAY)
            self.speed.y *= Car.decay2rate(norm, CAR_SPEED_DECAY)
        elif forward:
            self.speed += CAR_ACCEL * forward_vector * terrain.traction
        else:
            self.speed -= CAR_ACCEL * forward_vector * terrain.traction

        if self.speed.length_squared() > 0:
            self.speed.clamp_magnitude_ip(CAR_SPEED_MAX)

    def steering(self, clockwise=True) -> None:
        if clockwise is None:
            self.agl_speed *= Car.decay2rate(self.agl_speed, CAR_ANGULAR_DECAY)
        elif clockwise:
            self.agl_speed += CAR_ANGULAR_ACCEL
        else:
            self.agl_speed -= CAR_ANGULAR_ACCEL

    def brake(self) -> None:
        """
            Applique les freins pour réduire la vitesse de la voiture
        """
        terrain = TERRAINS[self.tiletype]

        norm = self.speed.magnitude()
        self.speed.x *= Car.decay2rate(norm, CAR_BRAKE * terrain.traction)
        self.speed.y *= Car.decay2rate(norm, CAR_BRAKE * terrain.traction)

    def update_position(self, tiletype: TileType) -> None:
        """
            Met à jour la position verticale de la voiture en fonction de sa vitesse actuelle
        """
        rad = math.radians(self.angle)
        forward = pygame.Vector2(math.sin(rad), -math.cos(rad))
        right = pygame.Vector2(math.sin(rad - (math.pi / 2.0)), -math.cos(rad - (math.pi / 2.0)))

        v_forward = self.speed.dot(forward)
        v_right = self.speed.dot(right)

        self.tiletype = tiletype
        terrain = TERRAINS[self.tiletype]

        # Dérapage
        if abs(v_right) <= terrain.drift_threshold:
            v_right = 0.0
        else:
            overdrift = max(0.0, abs(v_right) - terrain.drift_threshold)
            reduced_grip = terrain.lat_grip / (1.0 + OVERDRIFT_WEIGHT * overdrift)
            v_right *= (1.0 - reduced_grip)

        self.speed = forward * v_forward + right * v_right

        self.angle += self.agl_speed
        self.x += self.speed.x
        self.y += self.speed.y

        # Collisions
        _, bounds = self.get_rotated_sprite()
        if bounds.x < 0:
            self.x = bounds.w / 2
        elif (bounds.left + bounds.w) > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - bounds.w / 2
        if bounds.y < 0:
            self.y = bounds.h / 2
        elif (bounds.top + bounds.h) > WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - bounds.h / 2

    def build_sprite(self) -> pygame.Surface:
        """Crée et renvoie la surface graphique représentant la voiture

        Retourne
        --------
        pygame.Surface
            Surface graphique de la voiture
        """
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (127, 0, 0), (0, 0, CAR_WIDTH, CAR_HEIGHT-40), border_radius=2)
        pygame.draw.rect(surf, (255, 0, 0), (0, CAR_HEIGHT-40, CAR_WIDTH, CAR_HEIGHT), border_radius=0)
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