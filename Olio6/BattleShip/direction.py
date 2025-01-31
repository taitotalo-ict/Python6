from enum import Enum
from random import choice

class Direction(Enum):
    '''These constants represent the main directions that ships can be placed.'''
    UP = (0, -1)
    UP_RIGHT = (1, -1)
    RIGHT = (1, 0)
    DOWN_RIGHT = (1, 1)
    DOWN = (0, 1)
    DOWN_LEFT = (-1, 1)
    LEFT = (-1, 0)
    UP_LEFT = (-1, -1)

    @property
    def x(self) -> int:
        '''Returns x component (-1, 0, 1) of the direction as int.'''
        return self.value[0]
    
    @property
    def y(self) -> int:
        '''Returns y component (-1, 0, 1) of the direction as int.'''
        return self.value[1]

    @classmethod
    def get_values(cls) -> list['Direction']:
        '''Returns a list of directions in a clockwise direction starting from up.'''
        return [dir for dir in Direction]

    @classmethod
    def get_random(cls) -> 'Direction':
        '''Return a random direction (not diagonals!).'''
        return choice((Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT))

