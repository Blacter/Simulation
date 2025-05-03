from time import sleep

from render import Render
from map import Map
from actions.init_map import InitMap
from actions.move import Move


class Simulation:
    def __init__(self) -> None:
        self.init_map_action: InitMap = InitMap()
        self.map: Map = self.init_map_action.init_map() 
        self.move_action: Move = Move(self.map)
        self.init_actions = []
        self.turn_actions = []
        self.render: Render = Render()
        

    def next_turn(self):
        self.move_action.move_all_creatures()
        self.move_action.generate_new_entities()

    def start_simulation(self):        
        while True:
            self.next_turn()
            self.render.render(self.map)
            sleep(1)

    def pause_simulation():
        pass
