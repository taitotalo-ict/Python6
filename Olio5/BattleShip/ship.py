class ShipPart:
    def __init__(self, ship: 'Ship') -> None:
        self.ship = ship
        self._is_destroyed = False

    def hit(self) -> None:
        self._is_destroyed = True

    @property
    def is_destroyed(self) -> bool:
        return self._is_destroyed


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
        return all(part.is_destroyed for part in self.parts)
    
    def __getitem__(self, index: int) -> ShipPart:
        if index >= self.size:
            raise IndexError('ShipPart index out of range.')
        return self.parts[index]
