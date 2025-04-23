from coordinates import Coordinates
from entity.entity import Entity
from entity.rock import Rock
from entity.tree import Tree
from entity.grass import Grass


class Map:
    def __init__(self, grid: dict[Coordinates, Entity], height: int, width: int) -> None:
        self.__width: int = width
        self.__height: int = height
        self.__grid: dict[Coordinates, Entity] = grid

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
        return False

    def get_neighbor_entity(self, coordinates: Coordinates, entity_type: Entity) -> Coordinates | None:
        x: int = coordinates.x
        y: int = coordinates.y
        result: bool = False
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
    
    def destroy_entity(self, coordinates: Coordinates):
        del self.__grid[coordinates]
