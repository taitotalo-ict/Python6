from ship import Ship
from map import Map

class Fleet:

    def __init__(self, board_size: int) -> None:
        SHIP_QUANTITY = {1: 3, 2: 3, 3: 2, 4: 1, 5: 1}
        # self._ships = []
        # for size, quantity in SHIP_QUANTITY.items():
        #     for _ in range(quantity):
        #         self._ships.append(Ship(size))
        
        self._ships = [Ship(size) for size, quantity in SHIP_QUANTITY.items() for _ in range(quantity)]
        self._map = Map(board_size, board_size)
        self.add_to_map()

