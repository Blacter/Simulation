from random import shuffle

from settings import Settings
from settings import MapSettings
from coordinates import Coordinates
from coordinates import CoordinatesUtil
from map import Map
from entity.entity import Entity
from entity.rock import Rock
from entity.tree import Tree
from entity.grass import Grass
from entity.herbivore import Herbivore
from entity.predator import Predator

from actions.entity_generator import EntityGenerator


class InitMap:
    def __init__(self):
        self.settings: Settings = Settings()
        self.entity_generator: EntityGenerator = EntityGenerator()
        self.coordinates_util: CoordinatesUtil = CoordinatesUtil()

    def get_initial_entities(self) -> list[Entity]:
        total_entities: int = self.settings.get_total_entities_number()

        map_settings: MapSettings = self.settings.get_map_settings()
        
        empty_square_coordinates_stack: list[Coordinates] = self.coordinates_util.get_random_coordinates(
            total_entities, map_settings)

        entities: list = []
        entities.extend(self.entity_generator.get_rock_entities(
            empty_square_coordinates_stack))
        entities.extend(self.entity_generator.get_tree_entities(
            empty_square_coordinates_stack))
        entities.extend(self.entity_generator.get_grass_entities(
            empty_square_coordinates_stack))
        entities.extend(self.entity_generator.get_herbivore_entities(
            empty_square_coordinates_stack))
        entities.extend(self.entity_generator.get_predator_entities(
            empty_square_coordinates_stack))

        return entities

    def init_map(self) -> Map:
        entities = self.get_initial_entities()
        map_grid = {}
        for entity in entities:
            map_grid[entity.coordinates] = entity

        return Map(map_grid, self.settings.map_height, self.settings.map_width)
