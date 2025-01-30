class Direction(Enum):
    '''These constants represent the main directions that ships can be placed.'''
    UP =
    UP_RIGHT =
    RIGHT =
    DOWN_RIGHT =
    DOWN =
    DOWN_LEFT =
    LEFT =
    UP_LEFT =

    @property
    def x(self) -> int:
        '''Returns x component of the direction as int.'''
    
    @property
    def y(self) -> int:
        '''Returns y component of the direction as int.'''

    @classmethod
    def get_values(cls) -> list['Direction']:
        '''Returns a list of directions in a clockwise direction starting from up.'''

    @classmethod
    def get_random(cls) -> 'Direction':
        '''Return a random direction (not diagonals!).'''
