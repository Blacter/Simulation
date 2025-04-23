from random import shuffle

from settings import Settings
from coordinates import Coordinates
from map import Map
from entity.entity import Entity
from entity.rock import Rock
from entity.tree import Tree
from entity.grass import Grass
from entity.herbivore import Herbivore
from entity.predator import Predator


class InitMap:
    @staticmethod
    def get_initial_num_rock(map_size: int, rock_rarity: int) -> int:
        return int(rock_rarity * map_size)

    @staticmethod
    def get_initial_num_tree(map_size: int, tree_rarity: int) -> int:
        return int(tree_rarity * map_size)

    @staticmethod
    def get_initial_num_grass(map_size: int, grass_rarity: int) -> int:
        return int(grass_rarity * map_size)

    @staticmethod
    def get_initial_num_herbivore(map_size: int, herbivore_rarity: int) -> int:
        return int(herbivore_rarity * map_size)

    @staticmethod
    def get_initial_num_predator(map_size: int, predator_rarity: int) -> int:
        return int(predator_rarity * map_size)

    @staticmethod
    def get_coordinates_by_number(square_number: list[int], map_height: int, map_width: int) -> int:
        return Coordinates(square_number // map_width, square_number % map_width)

    @staticmethod
    def get_rock_entities(square_coordinates_stack: list[Coordinates], map_size: int, num_rock: int) -> list[Rock]:
        rock_entities: list[Rock] = []
        for i in range(num_rock):
            rock_entities.append(Rock(square_coordinates_stack.pop()))
        return rock_entities

    @staticmethod
    def get_tree_entities(square_coordinates_stack: list[Coordinates], map_size: int, num_tree: int) -> list[Tree]:
        tree_entities: list[Tree] = []
        for i in range(num_tree):
            tree_entities.append(Tree(square_coordinates_stack.pop()))
        return tree_entities

    @staticmethod
    def get_grass_entities(square_coordinates_stack: list[Coordinates], map_size: int, num_grass: int,
                           grass_hp: int) -> list[Grass]:
        grass_entities: list[Grass] = []
        for i in range(num_grass):
            grass_entities.append(
                Grass(square_coordinates_stack.pop(), grass_hp))
        return grass_entities

    @staticmethod
    def get_herbivore_entities(square_coordinates_stack: list[Coordinates], map_size: int, num_herbivore: int,
                               herbivore_speed: int, herbivore_hp: int) -> list[Herbivore]:
        herbivore_entities: list[Herbivore] = []
        for i in range(num_herbivore):
            herbivore_entities.append(
                Herbivore(square_coordinates_stack.pop(), herbivore_speed, herbivore_hp)
            )
        return herbivore_entities

    @staticmethod
    def get_predator_entities(square_coordinates_stack: list[Coordinates], map_size: int, num_predator: int,
                              predator_speed: int, predator_hp: int, predator_damage: int) -> list[Predator]:
        predator_entities: list[Predator] = []
        for i in range(num_predator):
            predator_entities.append(
                Predator(square_coordinates_stack.pop(), predator_speed, predator_hp, predator_damage)
            )
        return predator_entities

    @staticmethod
    def get_random_coordinates(total_entities: int, map_height: int, map_width: int) -> list[Coordinates]:
        map_size: int = map_height * map_width
        square_numbers = [i for i in range(map_size)]
        shuffle(square_numbers)
        square_numbers = square_numbers[:total_entities]

        coordinates = []
        for square_number in square_numbers:
            coordinates.append(InitMap.get_coordinates_by_number(
                square_number, map_height, map_width))

        return coordinates

    @staticmethod
    def get_initial_entities(settings: Settings) -> list[Entity]:
        map_size: int = settings.map_height * settings.map_width

        num_rock: int = InitMap.get_initial_num_rock(
            map_size, settings.rock_rarity)
        num_tree: int = InitMap.get_initial_num_tree(
            map_size, settings.tree_rarity)
        num_grass: int = InitMap.get_initial_num_grass(
            map_size, settings.grass_rarity)
        num_herbivore: int = InitMap.get_initial_num_herbivore(
            map_size, settings.herbivore_rarity)
        num_predator: int = InitMap.get_initial_num_herbivore(
            map_size, settings.predator_rarity)

        total_entities: int = sum(
            (num_rock, num_tree, num_grass, num_herbivore, num_predator))

        square_coordinates_stack: list[Coordinates] = InitMap.get_random_coordinates(
            total_entities, settings.map_height, settings.map_width)

        entities: list = []
        entities.extend(InitMap.get_rock_entities(
            square_coordinates_stack, map_size, num_rock))
        entities.extend(InitMap.get_tree_entities(
            square_coordinates_stack, map_size, num_tree))
        entities.extend(InitMap.get_grass_entities(
            square_coordinates_stack, map_size, num_grass, settings.grass_hp))
        entities.extend(InitMap.get_herbivore_entities(
            square_coordinates_stack, map_size, num_herbivore, settings.herbivore_speed, settings.herbivore_hp))
        entities.extend(InitMap.get_predator_entities(
            square_coordinates_stack, map_size, num_predator, settings.predator_speed, settings.predator_hp, settings.predator_damage))

        return entities

    @staticmethod
    def init_map(settings: Settings) -> Map:
        entities = InitMap.get_initial_entities(settings)
        map_grid = {}
        for entity in entities:
            map_grid[entity.coordinates] = entity

        return Map(map_grid, settings.map_height, settings.map_width)

