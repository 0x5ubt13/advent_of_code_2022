import string

def calculate_score(letter):
    if letter in string.ascii_lowercase:
        return ord(letter) - 96
    
    if letter in string.ascii_uppercase:
        return ord(letter) - 38


def part1(rucksacks):
    score = 0
    for line in rucksacks:
        left, right = line[:len(line) // 2], line[len(line) // 2:]
        for letter in left:
            if letter in right:
                score += calculate_score(letter)
                break

    return f"Part 1 -> {score}"
        

def part2(rucksacks):
    score, badges = 0, []
    for i in range(2, len(rucksacks), 3):
        set1 = {component for component in rucksacks[i-2]}
        set2 = {component for component in rucksacks[i-1]}
        set3 = {component for component in rucksacks[i]}
        badges.append(set1.intersection(set2, set3))
            
    for badge in badges:
        score += calculate_score("".join(badge))

    return f"Part 2 -> {score}"


def main():
    rucksacks = []
    with open("./puzzle_inputs/03.txt", "r") as f:
        for line in f:
            rucksacks.append(line.strip())
        
    print(part1(rucksacks), part2(rucksacks))
        

if __name__ == '__main__':
    main()