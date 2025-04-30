from abc import ABC, abstractmethod


from settings import Settings
from map import Map
from actions.init_map import InitMap
from actions.move import Move
from coordinates import Coordinates
from entity.entity import Entity
from entity.rock import Rock
from entity.tree import Tree
from entity.grass import Grass
from entity.herbivore import Herbivore
from entity.predator import Predator


class Simulation:
    def __init__(self, settings: Settings) -> None:
        self.settings: Settings = settings
        self.init_map_action: InitMap = InitMap()
        self.map: Map = self.init_map_action.init_map() 
        self.move_action: Move = Move(self.map)
        self.init_actions = []
        self.turn_actions = []

    def next_turn(self):
        self.move_action.move_all_creatures()
        self.move_action.generate_new_entities()

    def start_simulation(self):        
        pass

    def pause_simulation():
        pass
