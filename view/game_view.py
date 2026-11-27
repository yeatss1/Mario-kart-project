import pygame
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TILE_SIZE,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COLOR_PANEL, COLOR_PANEL_BORDER,
    GameState
)
from model.game_model import GameModel


class GameView:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, model: GameModel) -> None:
        self.screen.fill(COLOR_BG)
        if model.state == GameState.MENU:
            self._draw_menu(model)
        elif model.state == GameState.MENU_JEU:
            self._draw_menu_jeu(model)
        elif model.state == GameState.RACING:
            self._draw_racing(model)
        pygame.display.flip()

    def _draw_menu(self, model: GameModel) -> None:
        cx = WINDOW_WIDTH // 2

        title_surf = self.font.render(
            "Jeu de course 2D", True, COLOR_ACCENT)
        self.screen.blit(title_surf, title_surf.get_rect(center=(cx, 160)))

        options = [("JOUER (Enter)", GameState.RACING),
                   ("QUITTER (Escape)", None)]
        for i, (label, _) in enumerate(options):
            y = 320 + i * 80
            rect = pygame.Rect(cx - 140, y - 25, 280, 50)
            pygame.draw.rect(self.screen, COLOR_PANEL, rect, border_radius=8)
            pygame.draw.rect(self.screen, COLOR_PANEL_BORDER,
                             rect, 2, border_radius=8)
            text_surf = self.font.render(
                label, True, COLOR_ACCENT if i == 0 else COLOR_TEXT)
            self.screen.blit(text_surf, text_surf.get_rect(center=rect.center))

    def _draw_menu_jeu(self, model : GameModel):
        cx = WINDOW_WIDTH // 2
        title = self.font.render("Choisissez un circuit", True, COLOR_ACCENT)
        self.screen.blit(title, title.get_rect(center=(cx, 100)))

        options = [("CIRCUIT 1", GameState.RACING),
                   ("CIRCUIT 2", GameState.RACING), 
                   ("CIRCUIT 3", GameState.RACING)]
        
        btn_w, btn_h, gap = 240, 50, 30
        x0 = (WINDOW_WIDTH - (3 * btn_w + 2 * gap)) // 2

        for i, (label, _) in enumerate(options):
            selected = (i == model.selected)
            rect = pygame.Rect(x0 + i * (btn_w + gap), 320 - btn_h // 2, btn_w, btn_h)

            pygame.draw.rect(self.screen, COLOR_PANEL, rect, border_radius=8)
            pygame.draw.rect(self.screen,
                             COLOR_ACCENT if selected else COLOR_PANEL_BORDER,
                             rect, 4 if selected else 2, border_radius=8)

            text_surf = self.font.render(
                label, True, COLOR_ACCENT if selected else COLOR_TEXT)
            self.screen.blit(text_surf, text_surf.get_rect(center=rect.center))

    def _draw_racing(self, model: GameModel) -> None:
        
        if model.circuit is None or model.car is None:
            return

        for row_idx, row in enumerate(model.circuit.grid):
            for col_idx, tile in enumerate(row):
                sprite = tile.get_sprite(TILE_SIZE)
                self.screen.blit(
                    sprite, (col_idx * TILE_SIZE, row_idx * TILE_SIZE))

        surf, rect = model.car.get_rotated_sprite()
        self.screen.blit(surf, rect)
