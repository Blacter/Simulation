from map import Map
from entity.creature import Creature
from entity.herbivore import Herbivore
from coordinates import Coordinates


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int, hp: int, attack: int) -> None:
        Creature.__init__(self, coordinates, speed, hp)
        self._attack: int = attack

    def make_move(self, map: Map):
        herbivore_coordinates: Coordinates = self.find_herbivore_in_neighbor_cell(map)
        if self.can_attack(herbivore_coordinates):            
            self.attack(map, herbivore_coordinates)
        else:
            super().make_move(map, herbivore_coordinates, Herbivore)

    def find_herbivore_in_neighbor_cell(self, map: Map) -> Coordinates:
        return map.get_neighbor_entity(self.coordinates, Herbivore)

    def can_attack(self, herbivore_coordinates: Coordinates):
        if herbivore_coordinates is None:
            return False
        return True
    
    def attack(self, map: Map, herbivore_coordinates: Coordinates) -> None:
        herbivore = map.get_entity(herbivore_coordinates)
        herbivore.get_damage(self._attack)
        self.restore_hp(herbivore.last_damage_done)
        
        print(f'log Attacker: {self.coordinates} | Attacked: {herbivore.coordinates} | Damage: {herbivore.last_damage_done}')
        
        if herbivore.hp == 0:
            map.destroy_entity(herbivore_coordinates)

    
    