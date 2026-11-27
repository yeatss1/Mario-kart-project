WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

CAR_ACCELERATION = 0.15
CAR_BRAKE = 0.3
CAR_REVERSE_ACCELERATION = 0.05

CAR_AIR_DRAG = 0.02    #Frottement de l'air - fraction de vitesse perdue par frame
CAR_STOP_SPEED = 0.04   #En dessous de cette vitesse -> Voiture arrétée
CAR_MAX_SPEED = 7
CAR_MAX_REVERSE_SPEED = 2.5

CAR_WIDTH = 30
CAR_LENGTH = 50
CAR_TURN_ANGLE = 0.05


class GameState:
    MENU = "menu"
    MENU_JEU = "menu_jeu"
    RACING = "racing"


# --- Couleurs UI ---
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)
