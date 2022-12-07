def read_lines(filename):
    clean_data = []
    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            clean_data.append(line.rstrip())
    return clean_data


def solve(data):
    # ------------------------------- Part 1 -------------------------------
    tree = {"/": {"dir_size": 0},}
    path = []
    cwd = tree["/"]
    level = 0
    for line in data:
        # Read command
        command = line.split(" ")
        if command[0] == '$':
            if command[1] == "cd":
                # Change dir, manage infra
                new_dir = command[2]
                if new_dir == "/":
                    cwd = tree["/"]
                    level = 0
                    # print("changing back to root")

                elif new_dir == "..":
                    level, path, cwd, tree = lvl_up(level, path, cwd, tree)

                else:
                    level += 1
                    path.append(new_dir)
                    try:
                        cwd[new_dir] = {"dir_size": 0}
                    except KeyError:
                        pass
                    cwd = cwd[new_dir]
                    # print("New dir")

            # elif command[1] == "ls":
            else:
                pass
                # don't do anything
             
        else:
            size = command[0]
            name = command[1]
            # print(cwd)
            if size != "dir":
                cwd[name] = int(size)
                cwd["dir_size"] += int(size)


    while level > 0:
        level, path, cwd, tree = lvl_up(level, path, cwd, tree)
        
    sizes = recursively_calculate_dir_sizes(tree["/"], 0)
    print("Part 1 ->", sizes)

    # ------------------------------- Part 2 -------------------------------
    unused_space = 70000000 - tree["/"]["dir_size"]
    required_space = 30000000
    size_to_delete = required_space - unused_space

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
    

def lvl_up(level, path, cwd, tree):
    level -= 1
    last_dir = cwd
    path.pop()
    cwd = tree["/"]
    for i in range(level):
        cwd = cwd[path[i]]
    cwd["dir_size"] += last_dir["dir_size"]

    return level, path, cwd, tree


if __name__ == '__main__':
    solve(read_lines("./puzzle_inputs/07.txt"))
    
