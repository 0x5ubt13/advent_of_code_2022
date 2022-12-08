class Coords():
    """A simple class to keep coordinates"""

    def __init__(self, x, y, max_down, max_right):
        """Initialise attributes"""
        self.x          = x
        self.y          = y
        self.up         = self.y - 1
        self.down       = self.y + 1
        self.max_down   = max_down
        self.left       = self.x - 1
        self.right      = self.x + 1
        self.max_right  = max_right
    
    def print_instance_attributes(self):
        """Implementing a quick check for debugging purposes"""
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)


def solve(grid):
    coords = Coords(0, 0, len(grid[0])-1, len(grid)-1)
    visible = 0
    top_scenic_score = 0

    for row in grid:
        for tree in row:
            # Prep tree vars
            visible_north, visible_east, visible_west, visible_south = False, False, False, False
            north_score, south_score, east_score, west_score = 0, 0, 0, 0

            # Check north column
            for i in range(coords.y, 0, -1):
                north_score += 1
                if grid[i-1][coords.x] >= tree:
                    break

                if i - 1 == 0 and grid[i-1][coords.x] < tree:
                    visible_north = True
            
            # Check south column
            for i in range(coords.y, coords.max_down):
                south_score += 1
                if grid[i + 1][coords.x] >= tree:
                    break

                if i+1 == coords.max_down and grid[i + 1][coords.x] < tree:
                    visible_south = True

            # Check west row
            for i in range(coords.x, 0, -1):
                west_score += 1
                if grid[coords.y][i - 1] >= tree:
                    break
                
                if i - 1 == 0 and grid[coords.y][i - 1] < tree:
                    visible_west = True

            # Check east row
            for i in range(coords.x, coords.max_right):
                east_score += 1
                if grid[coords.y][i + 1] >= tree:
                    break

                if i + 1 == coords.max_right and grid[coords.y][i + 1] < tree:
                    visible_east = True

            # Part 2 calculation
            scenic_score = north_score * south_score * east_score * west_score
            if scenic_score > top_scenic_score:
                top_scenic_score = scenic_score

            # Bypass visibility for part 1 for the edges
            if coords.x == 0 or coords.y == 0 or coords.x == coords.max_right or coords.y == coords.max_down:
                visible += 1
                coords.x += 1
                continue 
            
            # If any of them are True, score visibility
            if visible_north == True or visible_east == True or visible_west == True or visible_south == True:
                visible += 1

            # New tree, go right
            coords.x += 1
        # New row, reset x a go down
        coords.y += 1
        coords.x = 0

    print(f"Part 1 -> {visible} | Part 2 -> {top_scenic_score}")


def read_grid(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f:
            row = []
            for number in line.rstrip():
                num = str(number)
                for digit in num:
                    row.append(int(digit))
            grid.append(row)

    return grid


if __name__ == '__main__':
    solve(read_grid("./puzzle_inputs/08.txt"))