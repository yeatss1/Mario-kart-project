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

    #initialisation du jeu en ouvrant la fenetre, le temps, le model ect
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:
        state = self.model.state

        if state == GameState.MENU:
            self.handle_menu_key(key)
        elif state == GameState.MENU_JEU:
            self.handle_menu_jeu_key(key)
        elif state == GameState.RACING:
            if key == pygame.K_ESCAPE:
                self.model.state = GameState.MENU_JEU  

    def handle_menu_key(self, key: int) -> None:
        # Premier menu / ecran principal façon
        if key == pygame.K_RETURN:
            self.model.state = GameState.MENU_JEU
        elif key == pygame.K_ESCAPE: #Quitte le jeu
            self.quit()

    def handle_menuJeu_key(self, key:int):
        if key in (pygame.K_RIGHT, pygame.K_d): # d ou fleche de droite
            self.model.select_next()
        elif key in (pygame.K_LEFT, pygame.K_q): # q ou fleche de gauche
            self.model.select_previous()
        elif key == pygame.K_RETURN: # entrée
            self.model.load_circuit()
            self.model.state = GameState.RACING
        elif key == pygame.K_ESCAPE:
            self.model.state = GameState.MENU # retour au menu d'accueils

    def update(self) -> None:
        if self.model.state != GameState.RACING:
            return

        p1_input = self.input_handler.get_inputs()
        car = self.model.car
        self.apply_input(car, p1_input)
        self.model.update()

    def apply_input(self, car, player_input) -> None:
        # IN GAME INPUTS ////////////////////////////////////////////////
        if player_input['accelerate']:
            car.accelerate()
        if player_input['decelerate']:
            car.decelerate()
        if player_input['turn_left']:
            car.turn_left()
        if player_input['turn_right']:
            car.turn_right()
        # if player_input['echap']:
        #     pygame.quit() 

    def render(self) -> None:
        self.view.draw(self.model)

    def quit(self) -> None:
        self.running = False
        pygame.quit()
        sys.exit()
