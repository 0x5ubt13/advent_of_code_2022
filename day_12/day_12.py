#!/usr/bin/python3

from sys import maxsize as ms

class GPS():
    """A simple class to keep coordinates"""

    def __init__(self, y, x):
        """Initialise attributes"""
        self.x          = x
        self.y          = y
        self.up         = self.y - 1
        self.down       = self.y + 1
        self.left       = self.x - 1
        self.right      = self.x + 1
        self.previous   = 0
        self.value      = 0


    def update(self, y, x):
        """Update itself to get up, down, left, and right values"""
        self = self(y, x)


    def print_instance_attributes(self):
        """Implementing a quick check for debugging purposes"""
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)


def get_grids(filename):
    grid = []
    distances_grid = []
    with open(filename, "r") as f:
        for line in f:
            row = []
            distances_row = []
            for char in line.rstrip():
                row.append(char)
                distances_row.append(0)
            grid.append(row)
            distances_grid.append(distances_row)
    return grid, distances_grid


def find_source(source, grid):
    for row in range(len(grid)-1):
        for column in range(len(grid[0])-1):
            if grid[row][column] == source:
                return GPS(column, row)


def find_end(end, grid):
    for row in range(len(grid)-1):
        for column in range(len(grid[0])-1):
            if grid[row][column] == end:
                return GPS(column, row)


def Dijkstras(source, end, grid, distances_grid):
    """Implementing Dijkstra's algorithm to find shortest path between nodes S and E"""
    start_position = find_source(source, grid)
    end = find_end(end, grid)
    queue = []

    # for each vertex v in Graph.Vertices:
    for row in range(len(grid)-1):
        for column in range(len(grid[0])-1):
            v = GPS(row, column)

            # dist[v] ← INFINITY
            if row != start_position.y and column != start_position.x:
                distances_grid[row][column] = ms
                v.value = ms

            # prev[v] ← UNDEFINED
            v.previous = 0

            # add v to Q
            queue.append(v)
    
    # dist[source] ← 0
    start_position.value = 0

    # while Q is not empty:
    while len(queue) != 0:
        

    #     u ← vertex in Q with min dist[u]
    #     remove u from Q
    """
    1  function Dijkstra(Graph, source):
    2      
    3      for each vertex v in Graph.Vertices:
    4          dist[v] ← INFINITY
    5          prev[v] ← UNDEFINED
    6          add v to Q
    7      dist[source] ← 0
    8      
    9      while Q is not empty:
    10          u ← vertex in Q with min dist[u]
    11          remove u from Q
    12          
    13          for each neighbor v of u still in Q:
    14              alt ← dist[u] + Graph.Edges(u, v)
    15              if alt < dist[v]:
    16                  dist[v] ← alt
    17                  prev[v] ← u
    18
    19      return dist[], prev[]

    If we are only interested in a shortest path between vertices source and target, we can terminate the search after line 10 if u = target. Now we can read the shortest path from source to target by reverse iteration:

    1  S ← empty sequence
    2  u ← target
    3  if prev[u] is defined or u = source:          // Do something only if the vertex is reachable
    4      while u is defined:                       // Construct the shortest path with a stack S
    5          insert u at the beginning of S        // Push the vertex onto the stack
    6          u ← prev[u]                           // Traverse from target to source

    """
    

    
    

def solve():
    grid, distances_grid = get_grids("./puzzle_inputs/t12.txt")
    Dijkstras("S", "E", grid, distances_grid)
    

if __name__ == '__main__':
    solve()
