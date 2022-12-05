#!/usr/bin/python3

def solve(lines):
    # Init vars
    depot1, depot2 = {}, {}
    for i in range(1, 10):
        depot1[i] = []
        depot2[i] = []

    # Start main loop, first parse crates, then run instructions
    for row in lines:
        # Convert crates diagram
        if row.startswith("m") == False:
            column = 0
            for i in range(len(row)):
                if i % 4 == 0:
                    column += 1
                if row[i].isalpha():
                    depot1[column].insert(0, row[i])
                    depot2[column].insert(0, row[i])
        
        # Run instructions
        else:
            instructions = row.split(" ")
            # Index 1, 3, 5 are instruction numbers
            number_of_crates = int(instructions[1])
            from_column = int(instructions[3])
            to_column = int(instructions[5])

            # Queue system for part 1
            for i in range(number_of_crates):
                crate = depot1[from_column][len(depot1[from_column])-1]
                depot1[to_column].append(crate)
                depot1[from_column].pop()
            
            # Moving whole blocks for part2
            instructions = row.split(" ")
            # Index 1, 3, 5 are instruction numbers
            number_of_crates = int(instructions[1])
            from_column = int(instructions[3])
            to_column = int(instructions[5])

            # Move all at once
            crates = depot2[from_column][len(depot2[from_column]) - number_of_crates:]
            for crate in crates:
                depot2[to_column].append(crate)
            depot2[from_column] = depot2[from_column][:len(depot2[from_column]) - number_of_crates]
                
    part1, part2 = "", ""
    for i in range(1, 10):
        part1 += depot1[i][len(depot1[i])-1]
        if len(depot2[i]) > 0:
            part2 += depot2[i][len(depot2[i]) - 1]

    return part1, part2


def get_data(filename):
    clean_data = []
    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            clean_data.append(line.rstrip())
    
    return clean_data


def main(): 
    part1, part2 = solve(get_data("./puzzle_inputs/05.txt"))
    print(f"Part 1 -> {part1} | Part 2 -> {part2}")


if __name__ == '__main__':
    main()