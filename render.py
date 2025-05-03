from map import Map
from coordinates import Coordinates
from entity.entity import Entity
from entity.grass import Grass
from entity.rock import Rock
from entity.tree import Tree
from entity.herbivore import Herbivore
from entity.predator import Predator
from printer import Sprites

from settings import Settings

sprites: Sprites = Sprites()

settings: Settings = Settings()

horizontal_border_piece: str = '-'
horizontal_border_lenght: int = 3*settings.map_width

vertical_border_piece: str = '|'

class Render:
    @staticmethod
    def get_entity_sprite(entity: Entity) -> str:
        if isinstance(entity, Grass):
            return sprites.grass_sprite
        elif isinstance(entity, Rock):
            return sprites.rock_sprite
        elif isinstance(entity, Tree):
            return sprites.tree_sprite
        elif isinstance(entity, Herbivore):
            return sprites.herbivore_sprite
        elif isinstance(entity, Predator):
            return sprites.predator_sprite
        else:
            return sprites.empty_square_sprite

    @staticmethod
    def render(map: Map) -> None:
        for i in range(map.height):
            for j in range(map.width):
                square: Entity | None = map.grid.get(Coordinates(i, j))
                if isinstance(square, Entity):
                    print(
                        f'{Render.get_entity_sprite(map.grid.get(Coordinates(i, j)))}', end='')
                else:
                    print(
                        f'{Render.get_empty_square_sprite(Coordinates(i, j))}', end='')
            Render.print_vertical_border_piece()
        Render.print_horizontal_map_border()

    @staticmethod
    def get_empty_square_sprite(coordinates: Coordinates) -> str:
        if (coordinates.x + coordinates.y) % 2 == 0:
            return sprites.empty_square_sprite_one
        else:
            return sprites.empty_square_sprite_two
        
    @staticmethod
    def print_horizontal_map_border() -> None:
        print(horizontal_border_piece * horizontal_border_lenght)
        
    @staticmethod
    def print_vertical_border_piece() -> None:
        print(vertical_border_piece)