#!/usr/bin/python3

def get_data(filename):
    with open(filename, "r") as f:
        return f.readline()


def solve(data, length):
    chars = []
    counter = 0

    for char in data:
        counter += 1
        if char not in chars:
            chars.append(char)
            if len(chars) == length:
                return f"Position {counter}, string -> {''.join(chars)}"
        else:
            for i in range(len(chars)):
                if char == chars[i]:
                    chars = chars[i+1:]
                    chars.append(char)
                    break


if __name__ == '__main__':
    data = get_data("./puzzle_inputs/06.txt")
    print(f"Part 1 -> {solve(data, 4)}")
    print(f"Part 2 -> {solve(data, 14)}")

