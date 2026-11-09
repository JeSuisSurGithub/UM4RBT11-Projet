import pygame

# Dictionnaire de correspondance entre les touches du clavier et les actions du jeu
MAPPING = {
    pygame.K_UP: "accelerate",
    pygame.K_DOWN: "decelerate",
    pygame.K_LSHIFT: "brake",
}


class InputHandler:
    """Gère la capture des entrées utilisateur via le clavier avec Pygame

    Attributs
    --------
    mapping: dict
        Dictionnaire associant les touches Pygame aux actions du jeu
    """

    def __init__(self):
        """Initialise le gestionnaire d'entrées avec le mapping des touches par défaut"""
        self.mapping = MAPPING

    def get_inputs(self) -> dict:
        """Récupère l'état actuel des touches du clavier et renvoie un dictionnaire des actions activées

        Retourne
        --------
        dict
            Dictionnaire associant chaque action à un booléen indiquant si elle est active
        """
        keys = pygame.key.get_pressed()
        p = {action: False for action in self.mapping.values()}
        for key, action in self.mapping.items():
            if keys[key]:
                p[action] = True

        return p