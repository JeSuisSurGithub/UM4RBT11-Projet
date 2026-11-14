import pygame
import sys
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    GameState
)
from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler


class GameController:
    """Contrôleur principal du jeu.

    Attributs
    --------
    screen: pygame.Surface
        Surface d'affichage de la fenêtre du jeu
    clock: pygame.time.Clock
        Horloge pour contrôler le taux de rafraîchissement
    model: GameModel
        Modèle contenant les données et la logique du jeu
    view: GameView
        Vue gérant l'affichage graphique
    input_handler: InputHandler
        Gestionnaire des entrées utilisateur
    running: bool
        Indicateur d'exécution de la boucle principale
    """

    def __init__(self):
        """Initialise les composants principaux du jeu : affichage, horloge,
        modèle, vue, gestionnaire d'entrées et état d'exécution.
        """
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True

    def run(self) -> None:
        """Lance la boucle principale du jeu.

        Exécute continuellement la gestion des événements, la mise à jour logique
        et le rendu graphique tout en respectant le nombre d'images par seconde (FPS).

        Retourne
        --------
        None
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
        """Récupère et traite les événements de la file d'attente Pygame."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:
        """Traite l'appui sur une touche spécifique en fonction de l'état actuel du jeu.

        Paramètres
        --------
        key: int
            Constante de la touche Pygame enfoncée.
        """
        state = self.model.state

        if state == GameState.MENU:
            self.handle_menu_key(key)

        if state == GameState.CIRCUIT: 
            self.handle_menu_circuit(key)

    def handle_menu_key(self, key: int) -> None:
        """Gère les entrées clavier lorsque le jeu se trouve dans le menu principal.

        Paramètres
        --------
        key: int
            Constante de la touche Pygame enfoncée.
        """
        if key == pygame.K_RETURN:
            #self.model.load_circuit()
            self.model.state = GameState.CIRCUIT
        elif key == pygame.K_ESCAPE:
            self.quit()

    def handle_menu_circuit(self, key:int) -> None : 
        if key == pygame.K_1: 
            self.model.load_circuit1()
            self.model.state = GameState.RACING
        elif key == pygame.K_2: 
            self.model.load_circuit2()
            self.model.state = GameState.RACING

    def update(self) -> None:
        """Met à jour la logique du jeu à chaque image si la course est active."""
        if self.model.state != GameState.RACING:
            return

        p1_input = self.input_handler.get_inputs()
        car = self.model.car
        self.apply_input(car, p1_input)
        self.model.update()

    def apply_input(self, car, player_input) -> None:
        """Applique les commandes du joueur (accélération, freinage) à l'objet voiture.

        Paramètres
        --------
        car:
            L'objet voiture contrôlé.
        player_input: dict
            Dictionnaire des états des commandes du joueur.
        """
        if player_input['accelerate']:
            car.accelerate(forward=True)
        elif player_input['decelerate']:
            car.accelerate(forward=False)
        if player_input['brake']:
            car.brake()

    def render(self) -> None:
        """Dessine l'état actuel du jeu à l'écran via la vue."""
        self.view.draw(self.model)

    def quit(self) -> None:
        """Arrête proprement l'exécution du jeu et ferme l'application Pygame."""
        self.running = False
        pygame.quit()
        sys.exit()  