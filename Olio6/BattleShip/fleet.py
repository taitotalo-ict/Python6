from ship import Ship
from map import Map

class Fleet:

    def __init__(self, board_size: int) -> None:
        SHIP_QUANTITY = {1: 3, 2: 3, 3: 2, 4: 1, 5: 1}
        # self._ships = []
        # for size, quantity in SHIP_QUANTITY.items():
        #     for _ in range(quantity):
        #         self._ships.append(Ship(size))
        
        self._ships = [Ship(size) for size, quantity in sorted(SHIP_QUANTITY.items(), reverse=True) for _ in range(quantity)]
        self._map = Map(board_size, board_size)
        self.add_to_map()

    def __iter__(self):
        '''Returns an iterator of the ships.'''
        return iter(self._ships)

    def is_destroyed(self) -> bool:
        '''Returns True if all ships are destroyed. False otherwise.'''
        # for ship in self._ships:
        #     if not ship.is_destroyed():
        #         return False
        # return True
        return all(map(Ship.is_destroyed, self._ships))

    @property
    def map(self) -> Map:
        '''Returns the map where this fleet resides.'''
        return self._map

    def add_to_map(self) -> None:
        '''Add the ships of this fleet to the map. Returns None.'''
        for ship in self._ships:
            self._map.add_ship_random(ship)
