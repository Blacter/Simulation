from coordinates import Coordinates

from entity.entity import Entity
from entity.grass import Grass
from entity.herbivore import Herbivore
from entity.predator import Predator
from entity.rock import Rock
from entity.tree import Tree

from settings import Settings


class EntityGenerator:
    def __init__(self):
        self.settings: Settings = Settings()
        self.map_size: int = self.settings.get_num_squares_on_map()

    def get_rock_entities(self, square_coordinates_stack: list[Coordinates]) -> list[Rock]:
        num_rock: int = self.settings.get_rock_initial_number()
        rock_entities: list[Rock] = []
        for i in range(num_rock):
            rock_entities.append(Rock(square_coordinates_stack.pop()))
        return rock_entities

    def get_tree_entities(self, square_coordinates_stack: list[Coordinates]) -> list[Tree]:
        num_tree: int = self.settings.get_tree_initial_number()
        tree_entities: list[Tree] = []
        for i in range(num_tree):
            tree_entities.append(Tree(square_coordinates_stack.pop()))
        return tree_entities

    def get_grass_entities(self, square_coordinates_stack: list[Coordinates]) -> list[Grass]:
        num_grass: int = self.settings.get_grass_initial_number()
        grass_hp: int = self.settings.grass_hp
        grass_entities: list[Grass] = []
        for i in range(num_grass):
            grass_entities.append(
                Grass(square_coordinates_stack.pop(), grass_hp))
        return grass_entities
    
    def get_grass_entity(self, square_coordinages: Coordinates) -> Grass:
        grass_hp: int = self.settings.grass_hp
        return Grass(square_coordinages, grass_hp)        

    def get_herbivore_entities(self, square_coordinates_stack: list[Coordinates]) -> list[Herbivore]:
        num_herbivore: int = self.settings.get_herbivore_initial_number()
        herbivore_speed: int = self.settings.herbivore_speed
        herbivore_hp: int = self.settings.herbivore_hp
        herbivore_entities: list[Herbivore] = []
        for i in range(num_herbivore):
            herbivore_entities.append(
                Herbivore(square_coordinates_stack.pop(),
                          herbivore_speed, herbivore_hp)
            )
        return herbivore_entities
    
    def get_herbivore_entity(self, coordinates: Coordinates) -> Herbivore:
        herbivore_speed: int = self.settings.herbivore_speed
        herbivore_hp: int = self.settings.herbivore_hp
        result: Herbivore = Herbivore(coordinates, herbivore_speed, herbivore_hp)
        return result

    def get_predator_entities(self, square_coordinates_stack: list[Coordinates]) -> list[Predator]:
        num_predator: int = self.settings.get_predator_initial_number()
        predator_speed: int = self.settings.predator_speed
        predator_hp: int = self.settings.predator_hp
        predator_damage: int = self.settings.predator_damage
        predator_entities: list[Predator] = []
        for i in range(num_predator):
            predator_entities.append(
                Predator(square_coordinates_stack.pop(),
                         predator_speed, predator_hp, predator_damage)
            )
        return predator_entities
