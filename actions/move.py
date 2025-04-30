from map import Map
from coordinates import Coordinates
from coordinates import CoordinatesUtil

from entity.entity import Entity
from entity.grass import Grass
from entity.creature import Creature
from entity.herbivore import Herbivore
from entity.predator import Predator
from actions.init_map import InitMap
from settings import Settings

from actions.entity_generator import EntityGenerator

class Move:
    def __init__(self, map: Map):
        self.map: Map = map
        self.settings: Settings = Settings()
        self.entity_generator: EntityGenerator = EntityGenerator()
    
    def move_all_creatures(self):
        map_grid: list[Coordinates] = self.map.grid
        
        for entity_coordinates in map_grid:
            if isinstance(self.map.get_entity(entity_coordinates), Herbivore):
                creature: Herbivore = self.map.get_entity(entity_coordinates)
                creature.make_move(self.map)
                # print(creature.coordinates.x, creature.coordinates.y, f"{creature.hp = },", type(creature))
                
        for entity_coordinates in self.map.grid:
            if isinstance(self.map.get_entity(entity_coordinates), Predator):
                creature: Predator = self.map.get_entity(entity_coordinates)
                creature.make_move(self.map)
                # print(creature.coordinates.x, creature.coordinates.y, f"{creature.hp = }", type(creature))
                
    def generate_new_entities(self): # FIXME: think about naming.
        self.generate_grass()
        self.generate_herbivore()
                
    def generate_grass(self) -> None:
        if (self.is_need_to_generate_grass()):
            grass_coordinates: list[Coordinates] = self.map.get_random_empty_coordinates()
            grass_entity = self.entity_generator.get_grass_entity(grass_coordinates)
            self.map.set_entity(grass_entity)
            
    def is_need_to_generate_grass(self) -> bool:
        if self.get_number_of_grass_to_generate() > 0:
            return True
        return False
        
    def get_number_of_grass_to_generate(self) -> int:
        return self.settings.get_grass_initial_number() - self.map.get_number_of_entity_on_map(Grass)   
    
    def generate_herbivore(self) -> None:
        if self.is_need_to_generate_herbivore():    
            herbivore_coordinates: list[Coordinates] = self.map.get_random_empty_coordinates()
            herbivore_entity = self.entity_generator.get_herbivore_entity(herbivore_coordinates)
            self.map.set_entity(herbivore_entity)
    
    def is_need_to_generate_herbivore(self) -> bool:
        if self.get_number_of_herbivore_to_generate() > 0:
            return True
        return False
    
    def get_number_of_herbivore_to_generate(self) -> int:
        return self.settings.get_herbivore_initial_number() - self.map.get_number_of_entity_on_map(Herbivore)        
    