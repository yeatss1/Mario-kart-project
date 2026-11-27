from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit, Circuit2
from model.road_tile import RoadTile


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None

        self.selected = 0 

    def select_next(self) -> None:
        self.selected = (self.selected + 1) % 3

    def select_previous(self) -> None:
        self.selected = (self.selected - 1) % 3

    def load_circuit(self) -> None:
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for col_idx in range(GRID_COLS)] for row_idx in range(GRID_ROWS)]
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    # Fonction depart de la course (ici (7,1) signifie que la voiture va apparaitre en
    # colonne 7 ligne 1 du circuit

    def spawn_car(self) -> None:
        self.car = Car(7, 1)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
