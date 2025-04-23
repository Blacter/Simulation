from time import sleep

# from simulation import Map
# from simulation import Action
# from simulation import Coordinates
from simulation import Simulation
from navigation.navigator import Navigator
from render import Render

from settings import Settings
# from simulation import MAP_DEFAULT_HEIGHT
# from simulation import MAP_DEFAULT_WIDTH

if __name__ == '__main__':
    
    controll_symbols = ['', 'r']
    
    
    simulation = Simulation(Settings())    
    render: Render = Render()
    render.render(simulation.map)
    
    user_input: str = ''
    while user_input in controll_symbols:
        # if user_input == 'r':
        #     simulation = Simulation(Settings())
        # else:
        simulation.next_turn()
        render.render(simulation.map)
        # user_input = input()
        sleep(1)
        
    
    # simulation.next_turn()   
    
    # simulation.start_simulation()
    
    # navigator: Navigator = Navigator(simulation.map)
    