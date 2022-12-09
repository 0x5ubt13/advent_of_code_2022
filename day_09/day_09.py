#!/usr/bin/python3

class GPS():
    """A simple class to keep coordinates"""

    def __init__(self, x, y):
        """Initialise attributes"""
        self.x          = x
        self.y          = y
        self.up         = self.y - 1
        self.down       = self.y + 1
        self.left       = self.x - 1
        self.right      = self.x + 1


def check_grid(grid):
    result = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] != ".":
                result += 1
    return result

    
def make_grid(x, y):
    grid = []
    for i in range(x):
        row = []
        for i in range(y):
            row.append(".")
        grid.append(row)
    return grid


def get_data(filename):
    with open(filename, "r") as f:
        return [line.rstrip() for line in f]


def solve_part1(instructions):
    grid = make_grid(350, 350)
    head = GPS(175, 175)
    tail = GPS(175, 175)
    
    # Main loop. Each iteration is a new instruction
    for ins in instructions:
        instruction = ins.split(" ")
        direction = instruction[0]
        distance = int(instruction[1])

        # print(ins)
        for step in range(distance):
            # Steps loop, here the rope moves times distance
            match direction:
                case "U":
                    # If movement is in a different direction, the tail gets on its place
                    # Else, the tail doesn't move

                    # If tail is immediately left or right, stay for 1 step
                    # If tail is not up or in the same position
                    if head.y != tail.y or tail.y != head.up:
                        # If tail is down:
                        if tail.y == head.down: 
                            tail = GPS(head.x, head.y)
                            
                    # The head moves
                    head = GPS(head.x, head.y - 1)
                    
                case "D":
                    # If movement is in a different direction, the tail gets on its place
                    # Else, the tail doesn't move

                    # If tail is not down or in the same position
                    if head.y != tail.y or tail.y != head.down:

                        # If tail is up:
                        if tail.y == head.up: 
                            tail = GPS(head.x, head.y)
                             
                    # The head moves
                    head = GPS(head.x, head.y + 1)
                    
                case "L":
                    # If tail is not left or in the same position
                    if head.x != tail.x or tail.x != head.left:

                        # If tail is right:
                        if tail.x == head.right: 
                            tail = GPS(head.x, head.y)

                    # The head moves
                    head = GPS(head.x - 1, head.y)
                    
                case "R":
                    # If movement is in a different direction, the tail gets on its place
                    # Else, the tail doesn't move

                    # If tail is not right or in the same position
                    if head.x != tail.x or tail.x != head.right:

                        # If tail is left:
                        if tail.x == head.left: 
                            tail = GPS(head.x, head.y)

                    # The head moves
                    head = GPS(head.x + 1, head.y)
                
            # Mark position in the grid as visited
            grid[tail.y][tail.x] = "#"

    print(f"Part 1 -> {check_grid(grid)}")

    # Visualise
    # for x in range(len(grid)):
    #     print("".join(grid[x]))


def move_rope(direction, distance, knots, grid):
# for step in range(distance):
    head    = knots[0]
    second  = knots[1]
    tail    = knots[9]

    if direction == "down":
        for i in range(len(knots)):
            # If movement is in a different direction, the second gets on its place
            # Else, the second doesn't move

            # If second is not down or in the same position
            if head.y != second.y or second.y != head.down:

                # If second is up:
                if second.y == head.up: 
                        # If second is either diagonally left or right, move diagonally. 
                        # if second.x == head.left or second.x == head.right:
                    # print("Moving second down")
                    second = GPS(head.x, head.y)
            
            # First knot always moves in that direction
            head = GPS(head.x, head.y + 1)

    if direction == "up":
        pass
        # if head.y != tail.y or tail.y != head.up:
        #                 # If tail is down:
        #                 if tail.y == head.down: 
        #                     # If tail is either diagonally left or right, move diagonally. 
        #                     # if tail.x == head.left or tail.x == head.right:
        #                     tail = GPS(head.x, head.y)

        # First knot always moves in that direction                    
        head = GPS(head.x, head.y - 1)

        
    return knots, grid


def solve_part2(instructions):
    grid = make_grid(350, 350)
    head = GPS(175, 175)
    knots = []
    for i in range(10):
        knots.append(GPS(175,175))
    
    # Main loop. Each iteration is a new instruction
    for ins in instructions:
        instruction = ins.split(" ")
        direction = instruction[0]
        distance = int(instruction[1])

        for step in range(distance):
            # Steps loop, here the rope moves times distance
            match direction:
                case "U":
                    knots, grid = move_rope("up", distance, knots, grid)
                    
                case "D":
                    knots, grid = move_rope("down", distance, knots, grid)
                    
                case "L":
                    # If tail is not left or in the same position
                    if head.x != tail.x or tail.x != head.left:

                        # If tail is right:
                        if tail.x == head.right: 
                            # If tail is either diagonally left or right, move diagonally. 
                            # if tail.x == head.up or tail.down == head.right:
                            tail = GPS(head.x, head.y)

                    head = GPS(head.x - 1, head.y)
                    
                case "R":
                    # If tail is not right or in the same position
                    if head.x != tail.x or tail.x != head.right:

                        # If tail is left:
                        if tail.x == head.left: 
                                # If tail is either diagonally up or down, move diagonally. 
                                # if tail.x == head.up or tail.down == head.right:
                            # print("Moving tail right")
                            tail = GPS(head.x, head.y)

                    # The head moves
                    # print("Moving head right")
                    head = GPS(head.x + 1, head.y)
                
            # Mark position in the grid as visited
            grid[tail.y][tail.x] = "#"
    

    print(f"Part 2 -> {check_grid(grid)}")

    # Visualise
    # for x in range(len(grid)):
    #     print("".join(grid[x]))


if __name__ == '__main__':
    solve_part1(get_data("./puzzle_inputs/09.txt"))
    solve_part2(get_data("./puzzle_inputs/09.txt"))