import pygame
from controller.game_controller import GameController


def main():
    """Point d'entrée principal du programme, initialise Pygame, lance le contrôleur de jeu et gère la fermeture propre"""
    pygame.init()
    pygame.display.set_caption("Projet Python - Jeu de course 2D")

    controller = GameController()
    controller.run()
    #Lancer la boucle principale du jeu

    pygame.quit()


if __name__ == "__main__":
    main()