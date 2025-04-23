from queue import Queue
from copy import deepcopy

from map import Map
from navigation.adjacency_matrix import AdjacencyMatrix


class Navigator:
    def __init__(self, map: Map):
        self.queue = Queue()
        self.num_cells: int = map.width * map.height
        
    @staticmethod
    def print_visited(visited: list[bool]) -> None:
        print('visited = ', end='')
        for i, is_visited in enumerate(visited):
            if is_visited:
                print( i+1, end=' ')
        print()

    def BFS(self, start_node: int, goal_node: int) -> bool:
        queue_tmp = []
        iter_number = 1
        
        start_node -= 1
        goal_node -= 1
        visited: list[int] = [False] * self.num_cells
        expand_node: list[int] = list()
        self.queue.put(start_node)
        queue_tmp.append(start_node + 1)
        
        while (not self.queue.empty()):
            print(f'#{iter_number}')            
            
            node: int = self.queue.get()
            print(f'node = {node + 1}')
            print(f'{queue_tmp = }')
            
            queue_tmp.pop(0)
            if(node == goal_node):
                return True
            visited[node] = True
            expand_node = self.get_expand_node(node)
            for child in expand_node:
                if visited[child] == False:
                    self.queue.put(child)
                    queue_tmp.append(child+1)
                    visited[child] = True
            print(f'{queue_tmp = }')
            Navigator.print_visited(visited)
            iter_number += 1
        return False
            
    def get_expand_node(self, node) -> list[int]:
        result: list[int] = list()
        for i in range(self.num_cells):
            if self.adjacency_matrix[node][i] == 1:
                result.append(i)
        return result
    

if __name__ == '__main__':
    adjacency_matrix: list[list[int]] = \
        [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0,],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,],
    ]
        
    navigator: Navigator = Navigator(adjacency_matrix)
    res = navigator.BFS(2, 9)
    print(res)


