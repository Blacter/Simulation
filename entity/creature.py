from abc import ABC, abstractmethod

from entity.entity import Entity
from entity.grass import Grass
from coordinates import Coordinates
from map import Map
from navigation.BFS import BFS


class Creature(ABC, Entity):
    def __init__(self, coordinates: Coordinates, speed: int, hp: int) -> None:
        super().__init__(coordinates)
        self.__speed: int = speed
        self._max_hp: int = hp
        self._hp: int = self._max_hp
        self._last_damage_done: int = 0
        self.path: list[Coordinates] | None = None
        self.entity_coordinates_to_go:  Coordinates | None = None

    
    @abstractmethod
    def make_move(self, map: Map, direction: Coordinates, entity_type_to_search: Entity):
        
        # available_move_squares: set[Coordinates] = self.get_available_move_squares(
        #     map)
        # square_to_move = available_move_squares.pop()
        # print(f'{square_to_move = } Creature.py Creature make_move')
        
        bfs: BFS = BFS(map)
        self.path = bfs.search_path_to_nearest_entity(self.coordinates, entity_type_to_search)
        self.entity_coordinates_to_go = map.get_neighbor_entity_coordinates(self.path[-1], entity_type_to_search) # -1 -> последний элемент.
        
        # print(f'{self.entity_coordinates_to_go = }')
        # print(f'{self.path = }')        
                
        new_coordinates: Coordinates = self.path.pop(0)
        if new_coordinates == self.coordinates and len(self.path) != 0:
            new_coordinates = self.path.pop(0)
        map.move_creature(self.coordinates, new_coordinates)
        self.set_new_coordinates(new_coordinates)
    
    @property
    def last_damage_done(self) -> int:
        return self._last_damage_done
    
    @property
    def hp(self) -> int:
        return self._hp
        
    def set_new_coordinates(self, new_coordinates: Coordinates):
        self.coordinates = new_coordinates        

    def get_available_move_squares(self, map: Map) -> set[Coordinates]:
        result_squares: set[Coordinates] = self.get_squares_in_map_borders(map)
        result_squares = self.get_empty_squares(result_squares, map)
        
        return result_squares     

    def get_squares_in_map_borders(self, map) -> set[Coordinates]:
        # Squares around creature:
        # 1|0|7 → y
        # 2|*|6
        # 3|4|5
        # ↓ x
        #
        result: set[Coordinates] = set()
        current_coordinates: Coordinates = self.coordinates

        if current_coordinates.x-1 >= 0:  # 0.
            result.add(Coordinates(
                current_coordinates.x-1, current_coordinates.y))
        if current_coordinates.x-1 >= 0 and current_coordinates.y-1 >= 0:  # 1.
            result.add(Coordinates(current_coordinates.x -
                       1, current_coordinates.y-1))
        if current_coordinates.y-1 >= 0:  # 2.
            result.add(Coordinates(
                current_coordinates.x, current_coordinates.y-1))
        # 3.
        if current_coordinates.x+1 >= 0 and current_coordinates.y-11 < map.width:
            result.add(Coordinates(current_coordinates.x +
                       1, current_coordinates.y-1))
        if current_coordinates.x+1 < map.width:  # 4.
            result.add(Coordinates(
                current_coordinates.x+1, current_coordinates.y))        
        if current_coordinates.x+1 < map.height and current_coordinates.y+1 < map.width: # 5.
            result.add(Coordinates(current_coordinates.x +
                       1, current_coordinates.y+1))
        if current_coordinates.y+1 < map.height:  # 6.
            result.add(Coordinates(
                current_coordinates.x, current_coordinates.y+1))
        # 7.
        if current_coordinates.x-1 < map.height and current_coordinates.y+1 > 0:
            result.add(Coordinates(current_coordinates.x -
                       1, current_coordinates.y+1))

        return result

    def get_empty_squares(self, result_squares: set[Coordinates], map: Map) -> set[Coordinates]:
        return {square for square in result_squares if map.is_empty_square(square)}
    
    def restore_hp(self, hp_to_restore: int):
        if self._hp + hp_to_restore >= self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp += hp_to_restore        
    
    def decrease_hp(self, damage: int):
        self.define_last_damage_done(damage)
        self._hp -= self.last_damage_done
            
    def get_damage(self, damage: int):        
        self.decrease_hp(damage)
        
        
    def define_last_damage_done(self, damage: int) -> int:
        if self._hp <= damage:
            self._last_damage_done = self._hp
        else:            
            self._last_damage_done =  damage