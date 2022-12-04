def get_data(filename):
    clean_data = []
    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            clean_data.append(line.rstrip())
    
    return clean_data


def solve(lines):
    counter = 0
    for line in lines:
        left, right = line.split(",")[0], line.split(",")[1]
        left_start, left_end = int(left.split("-")[0]), int(left.split("-")[1])
        right_start, right_end = int(right.split("-")[0]), int(right.split("-")[1])

        if right_start >= left_start and right_end <= left_end:
            counter += 1

        elif left_start >= right_start and left_end <= right_end:
            counter += 1

    return f"Part 1 -> {counter}"


def solve_part2(lines):
    counter = 0
    for line in lines:
        left, right = line.split(",")[0], line.split(",")[1]
        left_start, left_end = int(left.split("-")[0]), int(left.split("-")[1])
        right_start, right_end = int(right.split("-")[0]), int(right.split("-")[1])

        stop = False
        for i in range(right_start, right_end + 1):
            if stop == True:
                break

            for j in range(left_start, left_end + 1):
                if i == j:
                    counter += 1
                    stop = True
                    break

    return f"Part 2 -> {counter}"


def main(): 
    data = get_data("./puzzle_inputs/04.txt")
    print(f"{solve(data)} | {solve_part2(data)}")


if __name__ == '__main__':
    main()