class ShipPart:
    def __init__(self, ship: 'Ship') -> None:
        self.ship = ship
        self._is_destroyed = False

    def hit(self) -> None:
        self._is_destroyed = True

    @property
    def is_hit(self) -> bool:
        '''Returns True if ship part has been hit/destroyed. False otherwise.'''
        return self._is_destroyed

    def __repr__(self) -> str:
        return f'<ShipPart of {self.ship} (intact: {not self._is_destroyed})>'

class Ship:
    def __init__(self, size: int) -> None:
        self.size = size

        # self.parts = []
        # for _ in range(size):
        #     self.parts.append(ShipPart(self))
        self.parts = [ShipPart(self) for _ in range(size)]

    def is_destroyed(self) -> bool:
        # for part in self.parts:
        #     if not part.is_destroyed:
        #         return False
        # return True
        return all(part.is_hit for part in self.parts)
    
    def __getitem__(self, index: int) -> ShipPart:
        if index >= self.size:
            raise IndexError('ShipPart index out of range.')
        return self.parts[index]

    def __repr__(self) -> str:
        return f'Ship({self.size})'
    
    def __len__(self) -> int:
        return self.size
    
    def __contains__(self, part: ShipPart) -> bool:
        return part in self.parts