from random import shuffle

from settings import MapSettings


class Coordinates:
    def __init__(self, x: int, y: int):
        self._x: int = x
        self._y: int = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, coordinates):
        return self.x == coordinates.x and self.y == coordinates.y

    def __repr__(self) -> str:
        return 'Coordinates' + str((self.x, self.y))


class CoordinatesUtil:
    @staticmethod
    def get_coordinates_by_number(square_number: list[int], map_settings: MapSettings) -> int:
        return Coordinates(square_number // map_settings.width, square_number % map_settings.width)

    @staticmethod
    def get_random_coordinates(number_of_coordinates: int, map_settings: MapSettings) -> list[Coordinates]:
        square_numbers = CoordinatesUtil.get_random_coordinates_numbers(number_of_coordinates, map_settings)

        # coordinates = []
        # for square_number in square_numbers:
        #     coordinates.append(CoordinatesUtil.get_coordinates_by_number(
        #         square_number, map_settings))
        coordinates: list[Coordinates] = CoordinatesUtil.get_coordinates_by_numbers(square_numbers, map_settings)

        return coordinates

    @staticmethod
    def get_numbers(number_of_coordinates: int) -> list[int]:
        return [i for i in range(number_of_coordinates)]
    
    @staticmethod
    def get_random_coordinates_numbers(number_of_coordinates: int, map_settings: MapSettings) -> list[int]:
        square_numbers = CoordinatesUtil.get_numbers(map_settings.num_squares) # get_empty_squares_number 
        shuffle(square_numbers)
        square_numbers = square_numbers[:number_of_coordinates]
        return square_numbers
    
    @staticmethod
    def get_coordinates_by_numbers(numbers: list[int], map_settings: MapSettings) -> list[Coordinates]:
        coordinates: list[Coordinates] = []
        for number in numbers:
            coordinates.append(CoordinatesUtil.get_coordinates_by_number(
                number, map_settings))
        return coordinates