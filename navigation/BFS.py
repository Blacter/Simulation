from queue import Queue

from map import Map
from coordinates import Coordinates

from entity.entity import Entity
from entity.grass import Grass

class BFS:
    def __init__(self, map: Map):
        self.__queue = Queue()
        
        self.__map = map        
        self.__dist: dict[Coordinates, int] = {}
        self.__set_empty_dist()
        self.__from: dict[Coordinates, Coordinates] = {}
        self.__set_empty_from()

    def search_path_to_nearest_entity(self, start_node: Coordinates, entity_type: Entity) -> list[Coordinates] | None:
        self.__init_dist(start_node)
        self.__init_from(start_node)
        self.__queue.put(start_node)
        while(not self.__queue.empty()):
            node: int = self.__queue.get()
            if self.__map.is_neighbor_entity_near_coordinates(node, entity_type):
                # nearest_grass_coordinates: Coordinates = self.__map.get_nearest_grass_around_coordinates(node)                
                return BFS.get_path(self.__from, node)
                
            for child in self.__map.get_nearest_empty_squares_around_coordinates(node):
                if self.__dist[child] > self.__dist[node] + 1:
                    self.__queue.put(child)
                    self.__dist[child] = self.__dist[node] + 1
                    self.__from[child] = node
                    
        return BFS.get_path(self.__from, start_node)
    
    def __init_dist(self, start_node: Coordinates):        
        self.__set_empty_dist()
        self.__dist[start_node] = 0
        
    def __set_empty_dist(self):
        self.__dist: dict[Coordinates, int] = {}
        for i in range(self.__map.height):
            for j in range(self.__map.width):
                self.__dist[Coordinates(i, j)] = float('inf')

    def __init_from(self, start_node: Coordinates):
        self.__set_empty_from()
        self.__from[start_node] = Coordinates(-1, -1)
                        
    def __set_empty_from(self):
        self.__from: dict[Coordinates, int] = {}
        for i in range(self.__map.height):
            for j in range(self.__map.width):
                self.__from[Coordinates(i, j)] = None
        
    @staticmethod
    def get_path(from_dict: dict[Coordinates, Coordinates], finish_node: Coordinates) -> list[int]:
        path: list[Coordinates] = []
        v: Coordinates = finish_node
        
        if from_dict[v] is None:
            return None
        
        while v != Coordinates(-1, -1):
            path.append(v)
            v = from_dict[v]
            
        path.reverse()
        return path