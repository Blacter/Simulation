from map import Map
from entity.entity import Entity
from entity.creature import Creature
from entity.grass import Grass
from coordinates import Coordinates


class Herbivore(Creature):
    def __init__(self, coordinates: Coordinates, speed: int, hp: int) -> None:
        super().__init__(coordinates, speed, hp)

    def make_move(self, map):
        grass_coordinates: Coordinates = self.find_grass_in_neighbor_cell(map)
        if self.can_eat(grass_coordinates):
            self.eat(map, grass_coordinates)
        else:
            super().make_move(map, grass_coordinates, Grass)
        
    def find_grass_in_neighbor_cell(self, map: Map) -> Coordinates: # Grass in neighbor square (upper, left, rigth, down | NOT upper-left, upper-right etc.)
        return map.get_neighbor_entity(self.coordinates, Grass)
    
    def can_eat(self, grass_coordinates: Coordinates | None) -> bool:
        if grass_coordinates is None:
            return False
        return True
    
    def eat(self, map: Map, grass_coordinates: Coordinates) -> bool:
        self._hp += map.get_entity(grass_coordinates).hp
        map.destroy_entity(grass_coordinates)
    
    
        
