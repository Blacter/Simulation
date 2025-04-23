from map import Map
from entity.creature import Creature
from entity.herbivore import Herbivore
from coordinates import Coordinates


class Predator(Creature):
    def __init__(self, coordinates: Coordinates, speed: int, hp: int, attack: int) -> None:
        Creature.__init__(self, coordinates, speed, hp)
        self._attack: int = attack

    def make_move(self, map: Map):
        herbivore_coordinates: Coordinates = self.get_nearest_herbivore_coordinates()
        if self.can_attack(herbivore_coordinates):            
            self.attack(Map[herbivore_coordinates])
        else:
            super().make_move(map, herbivore_coordinates, Herbivore)

    def is_herbivore_near(self, herbivore_coordinates: Coordinates) -> bool:
        pass

    def attack(herbivore: Herbivore) -> None:
        pass

    def find_nearest_herbivore(self, map: Map) -> Coordinates:
        pass
    