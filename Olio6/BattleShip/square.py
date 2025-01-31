from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship import Ship, ShipPart

class Sea:
    def __init__(self) -> None:
        self._is_hit = False

    def hit(self) -> None:
        self._is_hit = True
    
    @property
    def is_hit(self) -> bool:
        return self._is_hit

class Square:
    def __init__(self) -> None:
        self.content = Sea()
    
    def hit(self) -> 'None|Ship':
        return self.content.hit()
    
    @property
    def is_hit(self) -> bool:
        return self.content.is_hit
    
    def set_ship_part(self, ship_part: 'ShipPart') -> None:
        if not isinstance(self.content, Sea):
            raise Exception('Square is not empty.')
        self.content = ship_part

    def __str__(self) -> str:
        '''
        Returns a character representing the content of this square:
           - '·': Sea that has not been hit.
           - 'o': Sea that has been hit.
           - '#': Ship part that has not been hit.
           - 'X': Ship part that has been hit.
        '''
        if isinstance(self.content, Sea):
            return 'o' if self.content.is_hit else '·'
        else:
            return 'X' if self.content.is_hit else '#'

    def __repr__(self) -> str:
        '''Representation of the square.'''
        return f'Square[{self.content.__class__.__name__}]'