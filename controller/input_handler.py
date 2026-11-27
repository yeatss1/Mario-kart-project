import pygame

# Dico lien entre input et action : 
MAPPING = {
    pygame.K_UP:     "accelerate",
    pygame.K_z : "accelerate",
    pygame.K_s : "decelerate",
    pygame.K_DOWN : "decelerate",
    pygame.K_LEFT : "turn_left",
    pygame.K_q : "turn_left",
    pygame.K_RIGHT : "turn_right",
    pygame.K_d : "turn_right",
    pygame.K_ESCAPE : "echap"  
}

class InputHandler:

    def __init__(self):
        self.mapping = MAPPING

# fonction pour lié input et action, si fleche du haut ou z appuyé, accelerate : True (p1 ou p2) à voir

    def get_inputs(self) -> dict:
        keys = pygame.key.get_pressed()
        p = {action: False for action in self.mapping.values()}

        for key, action in self.mapping.items():
            if keys[key]:
                p[action] = True
        #print(p)
        return p
