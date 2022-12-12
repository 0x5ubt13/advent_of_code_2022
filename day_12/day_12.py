import networkx as nx

# grid = []
# with open("./puzzle_inputs/t12.txt") as f:
#     for y in f:
#         y = y.rstrip()
#         row = []
#         for x in y:
#             row.append(ord(x)-96)
#         grid.append(row)
grid = [[(ord(x)-96) for x in y.rstrip()] for y in open("./puzzle_inputs/12.txt")]


def generate_graph(grid):
    G = nx.DiGraph()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            G.add_node((x, y))
            neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for nex, ney in neighbours:
                if 0 <= nex < len(grid[0]) and 0 <= ney < len(grid):
                    if grid[ney][nex] - grid[y][x] <= 1:
                        G.add_edge((x, y), (nex, ney), weight=grid[ney][nex])
    return G


def calc_paths(sourcey, goal):
    G = generate_graph(grid)
    path = nx.shortest_path(G, source=sourcey, target=goal)
    # print(path)
    # risk = sum(grid[y][x] for x, y in path[1:])
    return len(path) - 1


def solve():
    for y, i in enumerate(grid):
        for x, j in enumerate(i):
            if j == (ord("S") - 96):
                grid[y][x] = 0
                sourcey = (x, y)
            elif j == (ord("E")- 96):
                grid[y][x] = 26
                goal = (x, y)

    first_path = calc_paths(sourcey, goal)

    paths = list()
    paths.append(first_path)

    for y, i in enumerate(grid):
        for x, j in enumerate(i):
            if j == (ord("a") - 96):
                sourcey = (x, y)
                try:
                    paths.append(calc_paths(sourcey, goal))
                except:
                    pass
    

    print(f"Part one: {first_path} | Part two: {min(paths)}")


if __name__ == '__main__':
    solve()