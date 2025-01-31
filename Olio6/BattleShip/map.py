from string import ascii_uppercase as LETTERS
from coordinates import Coordinates
from square import Square

class Map:
    '''
    A map class that contains squares with sea or ship parts. 

    This class exposes the following methods:
    - add_ship_random(ship): To add a ship to a random position of the map.
    - hit(map_coordinates): To hit/attack a certain place of the map.
    - is_hit(map_coordinates): To check if a certain place of the map has been hit.
    - mark_neighbors(ship): To mark the neighbor squares of a ship as hit.
    - print_map(): To print a representation of the map.
    - print_hit_map(): To print a representation of the map with only the places that have been hit.
    '''
    def __init__(self, width: int, height: int) -> None:
        self.squares = {Coordinates(x, y): Square() for x in range(width) for y in range(height)}
        self.width = width
        self.height = height
        self.ships = []

    def __contains__(self, coordinates: 'Coordinates') -> bool:
        '''Returns True if the map contains the given coordinates. False otherwise.'''
        return coordinates in self.squares

    def _get_coordinates_from_map_coordinates(self, map_coordinates: str) -> 'Coordinates':
        '''Get the general coordinates (x, y) that correspond to a certain map coordinates (eg. B7).'''
        letter = map_coordinates[0].upper()
        if letter not in LETTERS[:self.width]:
            raise TypeError('First map coordinate must be a letter')
        
        try:
            number = int(map_coordinates[1:])
        except:
            raise TypeError('Second map coordinate must be an integer number')
        
        coordinates = Coordinates(LETTERS.index(letter), number - 1)
        if coordinates not in self:
            raise ValueError('Map coordinates not in map')

        return coordinates

    def hit(self, map_coordinates: str) -> 'None|Ship':
        coordinates = self._get_coordinates_from_map_coordinates(map_coordinates)

        return self.squares[coordinates].hit()
    
    def is_hit(self, map_coordinates: str) -> bool:
        coordinates = self._get_coordinates_from_map_coordinates(map_coordinates)

        return self.squares[coordinates].is_hit
    
    def print_map(self):
        '''Print the map.'''
        print(f'   {LETTERS[:self.width]}')
        for y in range(self.height):
            print(f'{y+1:>2}', end=' ')
            for x in range(self.width):
                print(self.squares[Coordinates(x, y)], end='')
            print()

    def print_hit_map(self):
        '''Print map with hitting places'''
        print(f'   {LETTERS[:self.width]}')
        for y in range(self.height):
            print(f'{y+1:>2}', end=' ')
            for x in range(self.width):
                print(self.squares[Coordinates(x, y)].hit_str(), end='')
            print()