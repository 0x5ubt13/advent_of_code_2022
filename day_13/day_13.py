#!/usr/bin/python3

def get_data(filename):
    return [(line.rstrip()) for line in open(filename)]


def get_pairs(data):
    pairs = []
    pair = []
    for line in data:
        if line == "":
            # New pair
            pairs.append(pair)
            pair = []
            continue

        pair.append(line)
    
    return pairs


def recurse(list):
    

def parse_pairs(pairs):
    count = 1
    char_count = 0
    for pair in pairs:
        left_pair = []
        right_pair = []
        iter_left = iter(pair[0])
        iter_right = iter(pair[1])
        
        while True:
            try:
                char = next(iter_left)
                # Ignore first and last square bracket chars
                if (char == '[' and char_count == 0) or (char == ']' and char_count == len(pair[0])-1):
                    char_count += 1
                    continue

                # Get a list for every square bracket open


                char_count += 1
            except StopIteration:
                break  # Iterator exhausted: stop the loop
            else:
                print(char)
        for char in iter_left:
            


            char_count += 1

        print(f"== Pair {count} ==")
        print(f"- Compare {left_pair} vs {right_pair}")
        for i in range(len(left_pair)):
            print(f"\t- Compare {left_pair[i]} vs {right_pair[i]}")
        

        count += 1
    



def solve():
    data = get_data("./puzzle_inputs/t13.txt")
    pairs = get_pairs(data)
    parse_pairs(pairs)
    


if __name__ == '__main__':
    solve()
