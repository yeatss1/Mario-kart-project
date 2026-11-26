import pygame
import math as m
from constants import (
    CAR_ACCELERATION, CAR_BRAKE, CAR_REVERSE_ACCELERATION,
    CAR_MAX_SPEED, CAR_MAX_REVERSE_SPEED,
    CAR_WIDTH, CAR_LENGTH, TILE_SIZE, CAR_TURN_ANGLE
)


class Car:

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        """Touche avancer: accélère en marche avant / freine en marche arrière"""
        if self.speed < 0:
            self.speed = min(0.0, self.speed + CAR_BRAKE)
        else:
            self.speed += CAR_ACCELERATION

    def decelerate(self) -> None:
        """Touche reculer: freine en marche avant / recule si la voiture est arrêtée."""
        if self.speed > 0:
            self.speed = max(0.0, self.speed - CAR_BRAKE)
        else:
            self.speed -= CAR_REVERSE_ACCELERATION

    def turn_left(self):
        self.angle += CAR_TURN_ANGLE    
        
    def turn_right(self):
        self.angle -= CAR_TURN_ANGLE

    def max_speed(self) -> None:
        """Limite la vitesse en marche avant/arrière"""
        self.speed = max(-CAR_MAX_REVERSE_SPEED, min(self.speed, CAR_MAX_SPEED))

    def update_position(self) -> None:
        """Limite la vitesse puis déplace la voiture de "speed" pixels dans la direction de son angle"""
        self.max_speed()
        self.x += self.speed * m.cos(self.angle)
        self.y -= self.speed * m.sin(self.angle)    #Axe y orienté vers le bas

        print(round(self.speed, 2))

    def build_sprite(self) -> pygame.Surface:
        """Dessine la voiture orientée vers la droite (angle 0)"""
        surf = pygame.Surface((CAR_LENGTH, CAR_WIDTH), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_LENGTH, CAR_WIDTH),
                         border_radius=5)

        #Dessin d'un pare prise pour repérer l'avant
        pygame.draw.rect(surf, (180, 220, 255), (CAR_LENGTH-18, 4, 8, CAR_WIDTH-8), border_radius=2)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Renvoie le sprite tourné selon l'angle et on rectangle centré sur la voiture"""
        rotated = pygame.transform.rotate(self.sprite, m.degrees(self.angle))
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
