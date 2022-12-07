#!/usr/bin/python3

def solve(data):
    # ------------------------------- Part 1 -------------------------------
    # Process the commands and save a map of the filesystem
    level, tree, path = 0, {"/": {"dir_size": 0}}, []
    cwd = tree["/"]

    for line in data:
        # Read terminal data
        output = line.split(" ")
        if output[0] == '$':
            command = output
            if command[1] == "cd":
                # Change dir, manage infra
                new_dir = command[2]
                if new_dir == "/":
                    # Change to root
                    cwd = tree["/"]
                    level = 0

                elif new_dir == "..":
                    # Go up a level
                    level, tree, path, cwd = lvl_up(level, tree, path, cwd)

                else:
                    # Register new dir: init subdict and change to it
                    level += 1
                    path.append(new_dir)
                    try:
                        cwd[new_dir] = {"dir_size": 0}
                    except KeyError:
                        pass
                    cwd = cwd[new_dir]
                
            continue
             
        # Process file in current dir -> size = output[0], name = output[1]
        if output[0] != "dir":
            cwd[output[1]] = int(output[0])
            cwd["dir_size"] += int(output[0])

    # Out of the loop, finish traversing up
    while level > 0:
        level, tree, path, cwd = lvl_up(level, tree, path, cwd)
    
    # Solve part 1
    sizes = recursively_calculate_dir_sizes(tree["/"], 0)
    print("Part 1 ->", sizes)

    # ------------------------------- Part 2 -------------------------------
    unused_space = 70000000 - tree["/"]["dir_size"]
    required_space = 30000000
    size_to_delete = required_space - unused_space

    # Solve part 2
    delete_candidates = recursively_calculate_dir_to_delete(tree, size_to_delete, [])
    
    print(f"Part 2 -> {delete_candidates[0]}")


def recursively_calculate_dir_to_delete(tree, size_to_delete, candidates):
    for file, value in tree.items():
        if type(value) == int:
            if file == "dir_size" and value > size_to_delete:
                candidates.append(value)

        if type(value) == dict:
            cwd = tree[file]
            candidates = recursively_calculate_dir_to_delete(cwd, size_to_delete, candidates)
    
    return sorted(candidates)

    
def recursively_calculate_dir_sizes(tree, sizes):
    for file, value in tree.items():
        if type(value) == int:
            if file == "dir_size" and value < 100000:
                sizes += value

        if type(value) == dict:
            cwd = tree[file]
            sizes = recursively_calculate_dir_sizes(cwd, sizes)
    
    return sizes
    

def lvl_up(level, tree, path, cwd):
    level -= 1
    last_dir = cwd
    path.pop()
    cwd = tree["/"]
    for i in range(level):
        cwd = cwd[path[i]]
    cwd["dir_size"] += last_dir["dir_size"]

    return level, tree, path, cwd


def read_lines(filename):
    clean_data = []
    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            clean_data.append(line.rstrip())
    return clean_data


if __name__ == '__main__':
    solve(read_lines("./puzzle_inputs/07.txt"))
    
