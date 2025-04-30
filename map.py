from random import randint

from coordinates import Coordinates
from coordinates import CoordinatesUtil
from entity.entity import Entity
from entity.rock import Rock
from entity.tree import Tree
from entity.grass import Grass

from settings import Settings
from settings import MapSettings

class Map:
    def __init__(self, grid: dict[Coordinates, Entity], height: int, width: int) -> None:
        self.__width: int = width
        self.__height: int = height
        self.__grid: dict[Coordinates, Entity] = grid
        self.map_settings: MapSettings = Settings().get_map_settings()

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def map_size(self) -> int:
        return self.__height * self.__width

    @property
    def grid(self) -> dict[Coordinates, Entity]:
        return self.__grid.copy()

    def show_debug(self):
        for coordinates, entity in self.grid.items():
            print(f"{coordinates}: {entity}")

    def is_empty_square(self, square: Coordinates) -> bool:
        return square not in self.grid

    def move_creature(self, start_coordinates: Coordinates, finish_coordinates: Coordinates):
        if start_coordinates != finish_coordinates:
            self.__grid[finish_coordinates] = self.__grid[start_coordinates]
            del self.__grid[start_coordinates]

    def get_entity(self, coordinates: Coordinates) -> Entity:
        return self.__grid.get(coordinates)

    def get_nearest_empty_squares_around_coordinates(self, coordinates: Coordinates) -> list[Coordinates]:
        x: int = coordinates.x
        y: int = coordinates.y
        result: list[Coordinates] = []
        # x-axis
        if x > 0:
            if Coordinates(x-1, y) not in self.__grid:
                result.append(Coordinates(x-1, y))
        if x < self.height - 1:
            if Coordinates(x+1, y) not in self.__grid:
                result.append(Coordinates(x+1, y))
        # y-axis
        if y > 0:
            if Coordinates(x, y-1) not in self.__grid:
                result.append(Coordinates(x, y-1))
        if y < self.width - 1:
            if Coordinates(x, y+1) not in self.__grid:
                result.append(Coordinates(x, y+1))
        return result

    def is_neighbor_entity_near_coordinates(self, coordinates: Coordinates, entity_type: Entity) -> bool:
        x: int = coordinates.x
        y: int = coordinates.y
        result: bool = False
        # x-axis
        if x > 0:
            if isinstance(self.__grid.get(Coordinates(x-1, y)), entity_type):
                return True
        if x < self.height - 1:
            if isinstance(self.__grid.get(Coordinates(x+1, y)), entity_type):
                return True
        # y-axis
        if y > 0:
            if isinstance(self.__grid.get(Coordinates(x, y-1)), entity_type):
                return True
        if y < self.width - 1:
            if isinstance(self.__grid.get(Coordinates(x, y+1)), entity_type):
                return True
            
        # if self.get_nearest_empty_squares_around_coordinates(coordinates, entity_type) is not None:
        #     return True
        
        return False

    def get_neighbor_entity_coordinates(self, coordinates: Coordinates, entity_type: Entity) -> Coordinates | None:
        x: int = coordinates.x
        y: int = coordinates.y
        # x-axis
        if x > 0:
            if isinstance(self.__grid.get(Coordinates(x-1, y)), entity_type):
                return Coordinates(x-1, y)
        if x < self.height - 1:
            if isinstance(self.__grid.get(Coordinates(x+1, y)), entity_type):
                return Coordinates(x+1, y)
        # y-axis
        if y > 0:
            if isinstance(self.__grid.get(Coordinates(x, y-1)), entity_type):
                return Coordinates(x, y-1)
        if y < self.width - 1:
            if isinstance(self.__grid.get(Coordinates(x, y+1)), entity_type):
                return Coordinates(x, y+1)
        return None
    
    def get_diagonally_neighbor_entity_coordinates(self, coordinates, entity_type) -> Coordinates | None:
        x: int = coordinates.x
        y: int = coordinates.y
        if x > 0:
            if isinstance(self.__grid.get(Coordinates(x+1, y+1)), entity_type):
                return Coordinates(x-1, y)
        if x < self.height - 1:
            if isinstance(self.__grid.get(Coordinates(x+1, y-1)), entity_type):
                return Coordinates(x+1, y)
        if y > 0:
            if isinstance(self.__grid.get(Coordinates(x-1, y+1)), entity_type):
                return Coordinates(x, y-1)
        if y < self.width - 1:
            if isinstance(self.__grid.get(Coordinates(x-1, y-1)), entity_type):
                return Coordinates(x, y+1)
        return None
    
    def destroy_entity(self, coordinates: Coordinates):
        del self.__grid[coordinates]

    def get_number_of_entity_on_map(self, entity_type: Entity) -> int:
        result: int = 0
        for entity in self.__grid.values():
            if isinstance(entity, entity_type):
                result += 1
        return result
    
    def get_number_of_empty_squares(self) -> int:
        result: int = self.map.__size - len(self.__gird)
        return result
    
    def get_random_empty_coordinates(self) -> Coordinates:
        number_of_empty_coordinates: int = self.map_size - self.get_number_of_entity_on_map(Entity)
        print(f'{self.map_size = } | {number_of_empty_coordinates = }')
        coordinates_random_number: int = randint(0, number_of_empty_coordinates - 1)        
        return self.get_empty_coordinates_by_number(coordinates_random_number)
    
    def get_empty_coordinates_by_number(self, number: int) -> Coordinates:
        coordinates_util: CoordinatesUtil = CoordinatesUtil()
        empty_coordinates_pass: int = 0
        all_coordinates_pass_number: int = 0
        while empty_coordinates_pass < number:
            coordinates: Coordinates = coordinates_util.get_coordinates_by_number(all_coordinates_pass_number, self.map_settings)
            if coordinates not in self.__grid:
                empty_coordinates_pass += 1
            all_coordinates_pass_number += 1
            
        result: Coordinates = coordinates_util.get_coordinates_by_number(all_coordinates_pass_number - 1, self.map_settings)
        print(f'number: {all_coordinates_pass_number} | coordinates by number: {result}')
        return result
            
    def set_entity(self, entity: Entity):
        self.__grid[entity.coordinates] = entity
    