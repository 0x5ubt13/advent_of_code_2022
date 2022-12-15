grid = []
for i in range(600):
    row = []
    for j in range(600):
        row.append(" ")
    grid.append(row)

with open("./puzzle_inputs/t14.txt", "r") as f:
    for line in f:
        coords = line.rstrip().split(" -> ")
        for coord in coords:
            x = int(coord.split(",")[0])
            y = int(coord.split(",")[1])

            
            