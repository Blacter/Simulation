from map import Map
from coordinates import Coordinates
from entity.creature import Creature
from entity.herbivore import Herbivore
from entity.predator import Predator

class Move:
    def __init__(self):
        pass
    
    def move_creatures(self, map: Map):
        map_grid: list[Coordinates] = map.grid
        
        for entity_coordinates in map_grid:
            if isinstance(map.get_entity(entity_coordinates), Herbivore):
                creature: Herbivore = map.get_entity(entity_coordinates)
                print(creature.coordinates.x, creature.coordinates.y, "move.py Move move_creatures")
                creature.make_move(map)
                
        for entity_coordinates in map.grid:
            if isinstance(map.get_entity(entity_coordinates), Predator):
                creature: Predator = map.get_entity(entity_coordinates)
                creature.make_move(map)